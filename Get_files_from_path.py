import glob
import os

def listup_files(path):
    if path.split('\\')[-1] == '\\':
        path = path + '*'
    else:
        path = path + r'\*'
    return [os.path.abspath(p) for p in glob.glob(path)]