import os
import pathlib
from os import listdir
from os.path import isfile, join

p = pathlib.Path().absolute()
filelist = [f for f in listdir(path=p) if isfile(join(p,f))]
count = 1
for i in filelist:
    if '.jpg' in i:
        os.rename(i,'{}.jpg'.format(str(count)))
        count +=1