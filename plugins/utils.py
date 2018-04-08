import os

def path_to_dict(path, m):
    d = {"name": os.path.basename(path)}

    if os.path.isdir(path):
        d["type"] = "directory"
        d["children"] = [path_to_dict(os.path.join(path, x), m) for x in os.listdir(path)]
    else:
        d["type"] = "file"
        d["magic"] = m.id_filename(path)

    return d
