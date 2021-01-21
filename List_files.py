import pathlib
from os import listdir
from os.path import isfile, join

def get_files(my_path):
    # path = input('Paths: ')
    filename = [f for f in listdir(path=my_path) if isfile(join(my_path,f))]