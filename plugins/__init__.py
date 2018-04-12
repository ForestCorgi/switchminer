plugins = []

from .plugin_info import PluginInfo
plugins.append(PluginInfo)

from .plugin_files import PluginFiles
plugins.append(PluginFiles)

from .plugin_diags import PluginDiags
plugins.append(PluginDiags)
