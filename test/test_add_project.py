from model.project import Project
import random


def test_add_project(app):
    #TestData
    name = 'name' + str(random.randrange(0,50))
    description = 'description' + str(random.randrange(0,50))
    project = Project(name=name, description=description)
    #Steps test keys
    old_project_list = app.project.get_project_list()
    app.project.add_new_project(project)
    old_project_list.append(project)
    new_project_list = app.project.get_project_list()
    assert sorted(old_project_list, key=Project.sorted_by_name) == sorted(new_project_list, key=Project.sorted_by_name)
    assert app.soap.project_id('administrator', 'root', project) != 0