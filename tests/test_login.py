# -*- coding: utf-8 -*-

#  Проверка корректности логина
# Логин и пароль берутся из когфигурационного файла

def test_login_ok(app):
    assert app.session.get_logged_user() == "administrator"