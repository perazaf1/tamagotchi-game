import os

def abs_path(relative_path):
    # Get the absolute path of the given relative path
    path = os.path.abspath(relative_path)
    return path
