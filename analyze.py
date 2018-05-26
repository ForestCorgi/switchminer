#!/usr/bin/env python3

import json
import os
import sys

from plugins import plugins as plugins_list

if __name__ == "__main__":
    builds = [build for build in os.listdir("builds") if build != ".gitignore"]
    plugins = [plugin("data") for plugin in plugins_list]

    if(len(builds) == 0):
        print("SwitchMiner was unable to find any builds!")
        print("Please note that builds have to be extracted into the 'builds' folder of this directory")
        sys.exit(0)

    for build in builds:
        data = {}

        for plugin in plugins:
            print("Running plugin {} on build {}...".format(plugin.name, build))

            result = plugin.run(os.path.join("builds", build), data)

            if result != None:
                data[plugin.id] = result

        with open(os.path.join("data", build + ".json"), "w") as build_data:
            json.dump(data, build_data)
