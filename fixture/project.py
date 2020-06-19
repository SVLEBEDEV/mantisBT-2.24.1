from time import sleep
from model.project import Project
import random


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_management_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href="/mantisbt-2.24.1/mantisbt-2.24.1/manage_overview_page.php"]').click()

    def go_to_project_management_page(self):
        wd = self.app.wd
        self.go_to_management_page()
        wd.find_element_by_css_selector('a[href="/mantisbt-2.24.1/mantisbt-2.24.1/manage_proj_page.php"]').click()

    def add_new_project(self, project):
        wd = self.app.wd
        self.go_to_project_management_page()
        wd.find_element_by_css_selector('button[class ="btn btn-primary btn-white btn-round"]').click()
        wd.find_element_by_id('project-name').click()
        wd.find_element_by_id('project-name').clear()
        wd.find_element_by_id('project-name').send_keys(project.name)
        wd.find_element_by_id('project-description').click()
        wd.find_element_by_id('project-description').clear()
        wd.find_element_by_id('project-description').send_keys(project.description)
        wd.find_element_by_css_selector('input[value="Добавить проект"]').click()
        sleep(3)

    def get_project_list(self):
        wd = self.app.wd
        project_list=[]
        self.go_to_project_management_page()
        for project in wd.find_elements_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
            name = project.find_elements_by_css_selector('td')[0].text
            description = project.find_elements_by_css_selector('td')[4].text
            project_list.append(Project(name=name, description=description))
        return project_list

    def open_first_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/a").click()

    def delete_first_project(self):
        wd = self.app.wd
        self.open_first_project()
        wd.find_element_by_css_selector('input[value="Удалить проект"]').click()
        wd.find_element_by_css_selector('input[value="Удалить проект"]').click()



