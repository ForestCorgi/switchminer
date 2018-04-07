import magic
import os

from io import StringIO

from .plugin import Plugin

magic_db = StringIO("0   string 3gmI   Apple IMG3")

class PluginFiles(Plugin):
    def run(self, build_dir):
        files_list = {}
        dirs_list = []
        with magic.Magic(["./plugins/magic.db.mgc", "/usr/share/file/magic.mgc"]) as m:
            for root, dirs, files in os.walk(build_dir):
                adjusted = root.replace(build_dir, "")
                dirs_list.append(adjusted)

                print("Processing {}".format(adjusted))

                for file in files:
                    full = os.path.join(root, file)

                    files_list[full] = m.id_filename(full)
