# -*- coding: utf-8 -*-

#  Проверка корректности логина

from model import LoginPage

# Логин и пароль берутся из конфигурационного файла
def test_login_ok(app):
    assert app.session.get_logged_user() == "administrator"

# Прoверка через SOAP
def test_login_soap(app):
    login = LoginPage("administrator", "root")
    assert app.soap.can_login(login)