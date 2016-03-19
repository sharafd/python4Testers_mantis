# -*- coding: utf-8 -*-

# Проекты

from model import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    # Открытие страницы добавления проекта
    def open_add_project_page(self):
        if len(self.app.wd.find_elements_by_xpath("//input[@class='button' and @value='Add Project']")) > 0:
         # сюда попадаем, если вообще нет проектов
            pass
        elif len(self.app.wd.find_elements_by_link_text("Manage Projects")) == 0:
            self.app.wd.get(self.app.baseurl + "/manage_proj_page.php")

    # Открытие страницы c проектами
    def open_projects_list_page(self):
        if len(self.app.wd.find_elements_by_xpath("//input[@class='button-small' and @value='Create New Project']")) == 0:
        #     self.app.wd.find_element_by_link_text("Manage").click()
        #     self.app.wd.find_element_by_link_text("Manage Projects").click()
            self.app.wd.get(self.app.baseurl + "/manage_proj_page.php")


    # Добавление нового проекта
    def add_project(self, project):
        # нажимаем 'Create New Project'
        self.app.wd.get(self.app.baseurl + "/manage_proj_create_page.php")
        # Создаем проект
        if project.name is not None:
            self.app.wd.find_element_by_name("name").click()
            self.app.wd.find_element_by_name("name").clear()
            self.app.wd.find_element_by_name("name").send_keys(project.name)
     #   if not self.app.wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[3]/td[2]/select//option[2]").is_selected():
     #       self.app.wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[3]/td[2]/select//option[2]").click()
     #   if not self.app.wd.find_element_by_name("inherit_global").is_selected():
     #     self.app.wd.find_element_by_name("inherit_global").click()
     #  if not self.app.wd.find_element_by_xpath("//table[@class='width75']//select[normalize-space(.)='publicprivate']//option[2]").is_selected():
     #      self.app.wd.find_element_by_xpath("//table[@class='width75']//select[normalize-space(.)='publicprivate']//option[2]").click()
        if project.description is not None:
            self.app.wd.find_element_by_name("description").click()
            self.app.wd.find_element_by_name("description").clear()
            self.app.wd.find_element_by_name("description").send_keys(project.description)
        self.app.wd.find_element_by_css_selector("input.button").click()

        self.open_projects_list_page()

        self.projects_cache = None

    # Cписок проектов
    def get_project_list(self):
        self.app.wd.get(self.app.baseurl + "/manage_proj_page.php")
        if self.project_cache is None:
          self.project_cache = []
          for element in self.app.wd.find_elements_by_xpath("//table[@class='width100']/tbody/tr[starts-with(@class, 'row-') and not(contains(@class, '-category'))]"):
              cells = element.find_elements_by_tag_name("td")
              name = cells[0].text
              status = cells[1].text
              view_status = cells[3].text
              description = cells[4].text
              self.project_cache.append(Project(name = name.strip(), status = status.strip(), view_status = view_status.strip(), description = description.strip()))
        return list(self.project_cache)