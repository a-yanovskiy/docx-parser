#!/usr/bin/python3

import docx, os

def get_paths():
    paths = []
    folder = os.getcwd()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('docx') and not file.startswith('~'):
                paths.append(os.path.join(root, file))
    return paths



for path in get_paths():
    doc = docx.Document(path)