#!/usr/bin/env python3

import json
import os

from plugins import plugins as plugins_list

if __name__ == "__main__":
    builds = [build for build in os.listdir("builds") if build != ".gitignore"]
    plugins = [plugin("data") for plugin in plugins_list]

    for build in builds:
        data = {}

        for plugin in plugins:
            print("Running plugin {} on build {}...".format(plugin.name, build))

            result = plugin.run(os.path.join("builds", build))

            if result:
                data[plugin.name] = result

        with open(os.path.join("data", build + ".json"), "w") as build_data:
            json.dump(data, build_data)
