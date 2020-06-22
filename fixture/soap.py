from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def project_id(self, username, password, project):
        client = Client('http://localhost/mantisbt-2.24.1/mantisbt-2.24.1/api/soap/mantisconnect.php?wsdl')
        return client.service.mc_project_get_id_from_name(username, password, project.name)