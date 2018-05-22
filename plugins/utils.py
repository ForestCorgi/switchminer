import os
import pyblake2
import sys

def hash_file(path):
    with open(path, "rb") as file:
        return pyblake2.blake2b(data=file.read(), digest_size=20).hexdigest()

def path_to_dict(path, m):
    d = {"name": os.path.basename(path)}

    if os.path.isdir(path):
        d["type"] = "directory"
        d["children"] = [path_to_dict(os.path.join(path, x), m) for x in os.listdir(path)]
    else:
        d["type"] = "file"
        d["magic"] = m.id_filename(path)
        d["hash"] = hash_file(path)

    return d
