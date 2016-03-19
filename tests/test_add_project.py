# -*- coding: utf-8 -*-

# Добавление нового проекта

from model import Project
from func import commonFunctions

common = commonFunctions.Common()

project = Project(name=common.random_ascii_string(15), description = common.random_digits(8))

# Тест - создание проекта
def test_add_new_project(app):
    app.project.open_add_project_page()
    # Запоминаем список проектов
    old_projects = app.project.get_project_list()
    # Добавляем новый проект
    app.project.add_project(project)
    # Полкчаем новый список проектов
    new_projects = app.project.get_project_list()
    old_projects.append(project)

    assert old_projects.sort()  == new_projects.sort()
