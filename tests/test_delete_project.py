# -*- coding: utf-8 -*-

# Добавление нового проекта

from model import Project
from func import commonFunctions

common = commonFunctions.Common()

project = Project(name="For Delete Test", status = "development", view_status = "public", description = "-")

# Тест - удаление проекта
def test_delete_project(app):
    app.project.open_add_project_page()
    if not app.project.is_project_exist(project):
        # проекта нет - надо создать
        app.project.add_project(project)
    # Запоминаем список проектов
    app.project.open_add_project_page()

    old_projects = app.project.get_project_list()

    app.project.delete_project_by_name(project)
    # Получаем новый список проектов
    new_projects = app.project.get_project_list()
    old_projects.remove(project)

    assert old_projects.sort() == new_projects.sort()
