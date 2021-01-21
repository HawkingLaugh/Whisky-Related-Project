from PIL import Image
import pytesseract
import cv2
import os
from Get_files_from_path import listup_files
import glob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def OCR_data(file):
    src = file
    img = cv2.imread(src, 0)

    ret, binary = cv2.threshold(img, 195,350, cv2.THRESH_BINARY)
    name = pytesseract.image_to_string(binary)
    # cv2.imshow('GRAY',binary)
    # cv2.waitKey(0)

    spl = name.split('\n')
    file_name = file.split('.')[0]
    fout = open('{}.txt'.format(file_name), 'w+', encoding='utf-8')
    for i in spl:
        if i != '':
            fout.write(i)
            fout.write('\n')
        else:
            continue

# def read_label():

# all data's [0] is numeric, filename to do the naming job
# [name] = code with\n = 

if __name__ == "__main__":
    path = listup_files(input('Path: '))
    for i in path:
        OCR_data(i)