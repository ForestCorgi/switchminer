import json
import magic
import os
import platform

from .plugin import Plugin
from .utils import path_to_dict

default_magic_db = "/usr/share/file/magic.mgc"

class PluginFiles(Plugin):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        self.name = "files"
        self.id = "files"

    def run(self, build_dir):
        with magic.Magic(["./plugins/magic.db.mgc", default_magic_db]) as m:
            file_structure = path_to_dict(build_dir, m)

        file_structure["name"] = "/"

        return file_structure
