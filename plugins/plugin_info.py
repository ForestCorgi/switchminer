import os
import plistlib

from .plugin import Plugin

version_plist_base = os.path.join("System", "Library", "CoreServices", "SystemVersion.plist")
release_name_base = os.path.join("usr", "share", "buildit", ".releaseName")

class PluginInfo(Plugin):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        self.name = "info"

    def run(self, build_dir):
        with open(os.path.join(build_dir, version_plist_base), "rb") as version_plist:
            plist_build_info = plistlib.load(version_plist, fmt=plistlib.FMT_XML)

        build_info = {
            "build": plist_build_info["ProductBuildVersion"],
            "copyright": plist_build_info["ProductCopyright"],
            "product": plist_build_info["ProductName"],
            "version": plist_build_info["ProductVersion"],
            "type": plist_build_info["ReleaseType"]
        }

        with open(os.path.join(build_dir, release_name_base), "r") as release_name:
            build_info["codename"] = release_name.read()

        return build_info
