#!/usr/bin/env python3

import os

from plugins import plugins as plugins_list

if __name__ == "__main__":
    builds = [os.path.join("builds", build) for build in os.listdir("builds")]
    plugins = [plugin("data") for plugin in plugins_list]

    for build in builds:
        for plugin in plugins:
            plugin.run(build)
