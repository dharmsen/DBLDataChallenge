import os
from zipfile import ZipFile

def unzip(file):
    '''
    Unzip file and save unzipped file in a directory 'unzipped'
    '''
    with ZipFile(file, 'r') as f:
        f.extractall('unzipped')

def unzip_all(dir):
    '''
    Unzips all files in a given directory
    Saves unzipped files in a directory 'unzipped'
    '''
    for file in os.listdir(dir):
        unzip(file)