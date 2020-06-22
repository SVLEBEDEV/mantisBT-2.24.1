from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def project_id(self, username, password, project):
        client = Client('http://localhost/mantisbt-2.24.1/mantisbt-2.24.1/api/soap/mantisconnect.php?wsdl')
        return client.service.mc_project_get_id_from_name(username, password, project.name)

    def get_projects(self, username, password):
        list_projects = []
        client = Client('http://localhost/mantisbt-2.24.1/mantisbt-2.24.1/api/soap/mantisconnect.php?wsdl')
        projects = client.service.mc_projects_get_user_accessible(username, password)
        for project in projects:
            list_projects.append(Project(id = project.id, name=project.name, description=project.description))
        return list_projects
