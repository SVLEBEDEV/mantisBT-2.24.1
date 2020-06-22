from model.project import Project
import random


def test_del_project(app):
    if len(app.soap.get_projects('administrator', 'root')) == 0:
        # TestData
        name = 'name' + str(random.randrange(0, 50))
        description = 'description' + str(random.randrange(0, 50))
        project = Project(name=name, description=description)
        # Steps test keys
        app.project.add_new_project(project)
    old_project_list = app.soap.get_projects('administrator', 'root')
    app.project.delete_project_by_id(old_project_list[0])
    new_project_list = app.soap.get_projects('administrator', 'root')
    project = old_project_list[0]
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.sorted_by_id) == sorted(new_project_list, key=Project.sorted_by_id)