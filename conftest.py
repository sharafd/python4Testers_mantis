# -*- coding: utf-8 -*-

import importlib
import jsonpickle
import os, json
import pytest

from fixtures import *

from model import LoginPage

fixture = None
configuration = None
login = LoginPage(login = None, password = None)

# Чтение кoнфигурационного файла
def load_config(file):
  global configuration

  if configuration is None:
    with open(file) as config_file:
        configuration  = json.load(config_file)

  return configuration

# Фикстура для WebDriver
@pytest.fixture
def app(request):
    global login
    global fixture
    # Чтение кoнфигурационного файла
    web_config = load_config(request.config.getoption("--cfg"))['web']
    webadmin_config = load_config(request.config.getoption("--cfg"))['webadmin']
    # Создание фикстуры
    if fixture is None or not fixture.isValid():
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser, baseurl = web_config['baseurl'])
        login = LoginPage(login = webadmin_config['username'], password = webadmin_config['password'])

    fixture.session.open_login_page()
    fixture.session.ensure_login(login, webadmin_config['username'])
    return fixture

@pytest.fixture(scope="session", autouse="True")
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

# Фикстура для mysql
@pytest.fixture(scope="session")
def db(request):
    # Чтение кoнфигурационного файла
    db_config = load_config(request.config.getoption("--cfg"))['db']
    dbfixture= DbFixture(host = db_config['host'], database = db_config['name'],
          user = db_config['user'], password = db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture
def checkUI(request):
    return request.config.getoption("--checkUI")

# Опции командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--cfg", action = "store", default = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cfg.json"))
    parser.addoption("--checkUI", action = "store_true")

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

# Загрузка тестовых данных из файла
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


