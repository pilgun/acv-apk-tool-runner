import json
import logging
import os

import config


class JsonWriter:
    def __init__(self, *projects):
        self.projects = projects
        self.json_path = os.path.join(config.results_dir, 'projects.json')
        self.document = self.read()

    def save_to_json(self):
        msg = 'SAVE TO JSON'
        projects_count = len(self.projects)
        if projects_count == 1:
            msg = '{}: '.format(self.projects[0].name) + msg
        else:
            msg += '{} PROJECTS'.format(projects_count)
        logging.info(msg)
        for project in self.projects:
            record = {"path": project.path, "name": project.name, "gradle_version": project.gradle_version}
            self.document["projects"].append(record)
            logging.debug(self.document)
        self.write()

    def read(self):
        document = {"projects": []}
        if os.path.exists(self.json_path):
            with open(self.json_path) as projects_file:
                document = json.load(projects_file)
        return document

    def write(self):
        with open(self.json_path, 'w') as projects_file:
            json.dump(self.document, projects_file, indent=2)
