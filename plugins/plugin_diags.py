import os

from glob import glob

from .plugin import Plugin

diags_dir_base = "AppleInternal/Diags/bin"
diags_patterns = ["diag*.img3", "diag*.img4", "diag*.im4p"]

class PluginDiags(Plugin):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        self.name = "diags"

    def run(self, build_dir):
        diags_list = []
        diags_dir = os.path.join(build_dir, diags_dir_base)

        if not os.path.isdir(diags_dir):
            return None

        for pattern in diags_patterns:
            for result in glob(os.path.join(diags_dir, pattern)):
                name = os.path.basename(result)

                diag_info = {
                    "name": name
                }

                if name.find("-") != -1:
                    device = name.split(".")[0].split("-")[1]
                    diag_info["device"] = device

        return diags_list
