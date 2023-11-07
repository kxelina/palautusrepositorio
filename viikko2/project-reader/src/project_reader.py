from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
       
        tomli_dict=(tomli.loads(content))
        name = tomli_dict["tool"]["poetry"]["name"]
        descripition = tomli_dict["tool"]["poetry"]["description"]
        dependencies = tomli_dict["tool"]["poetry"]["dependencies"]
        dev_dependencies = tomli_dict["tool"]["poetry"]["group"]["dev"]["dependencies"]
        licenses = tomli_dict["tool"] ["poetry"]["license"]
        authors = tomli_dict["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, descripition, licenses, authors, dependencies, dev_dependencies)
