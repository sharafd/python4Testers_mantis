# -*- coding: utf-8 -*-

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

# Опции командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--cfg", action = "store", default = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cfg.json"))

