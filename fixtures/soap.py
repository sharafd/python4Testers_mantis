# -*- coding: utf-8 -*-

from suds.client import Client
from suds import WebFault
import logging

class soapHelper:

    def __init__(self, app):
        self.app = app

    # Проверка логина
    def can_login(self, login):
        client = Client("http://192.168.1.25/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)
        try:
            client.service.mc_login(login.login, login.password)
            return True
        except WebFault:
            return False

    def get_available_projects(self, login):
        project_list = []
        client = Client("http://192.168.1.25/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)
        try:
            projects = client.service.mc_projects_get_user_accessible(login.login, login.password)

            for project in projects:
                project_list.append(project)

        except WebFault:
            pass

        return project_list