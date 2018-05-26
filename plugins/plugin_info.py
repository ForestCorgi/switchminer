import os
import plistlib
import re

from .plugin import Plugin

version_plist_base = "System/Library/CoreServices/SystemVersion.plist"
buildit_name_base = "usr/share/buildit/.releaseName"
system_log_base = "private/var/log/system.log"

class PluginInfo(Plugin):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        self.id = "info"
        self.name = self.id

    def run(self, build_dir, build_data):
        with open(os.path.join(build_dir, version_plist_base), "rb") as version_plist:
            plist_build_info = plistlib.load(version_plist, fmt=plistlib.FMT_XML)

        build_info = {
            "build": plist_build_info["ProductBuildVersion"],
            "copyright": plist_build_info["ProductCopyright"],
            "product": plist_build_info["ProductName"],
            "version": plist_build_info["ProductVersion"],
            "type": plist_build_info["ReleaseType"]
        }

        buildit_name = os.path.join(build_dir, buildit_name_base)
        system_log = os.path.join(build_dir, system_log_base)

        if os.path.isfile(buildit_name):
            with open(buildit_name, "r") as release_name:
                build_info["codename"] = release_name.read()
        elif os.path.isfile(system_log):
            with open(system_log, "r") as system_log_file:
                for line in system_log_file:
                    if line.find("hfs: mounted ") != -1 and line.find("root_device") != -1:
                        build_codename = line.split("hfs: mounted ")[1].split(".")[0]
                        build_info["codename"] = build_codename[:re.search("\d", build_codename).start()]
                        break

        return build_info
