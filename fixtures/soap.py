# -*- coding: utf-8 -*-

from suds.client import Client
from suds import WebFault
import logging

class soapHelper:

    def __init__(self, app):
        self.app = app

    # Проверка логина
    def can_login(selfself, login):
        client = Client("http://192.168.1.25/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)
        try:
            result = client.service.mc_login(login.login, login.password)
            print(result)
            return True
        except WebFault:
            return False
