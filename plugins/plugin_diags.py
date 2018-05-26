import os

from glob import glob

from .plugin import Plugin
from .utils import hash_file

diags_dir_base = "AppleInternal/Diags/bin"
diags_patterns = {"img3": "*.img3", "img4": "*.img4", "im4p": "*.im4p"}

class PluginDiags(Plugin):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        self.name = "diags"
        self.id = self.name

    def run(self, build_dir, build_data):
        diags_list = []
        diags_dir = os.path.join(build_dir, diags_dir_base)

        if not os.path.isdir(diags_dir):
            return None

        for pattern_type in diags_patterns:
            for result in glob(os.path.join(diags_dir, diags_patterns[pattern_type])):
                name = os.path.basename(result)

                diag_info = {
                    "name": name,
                    "type": pattern_type,
                    "hash": hash_file(result)
                }

                if pattern_type != "img4":
                    device = name.split(".")[0].split("-")[1].lower().capitalize()
                    diag_info["device"] = device

                diags_list.append(diag_info)

        return diags_list
