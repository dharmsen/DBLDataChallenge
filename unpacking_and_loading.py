import os
import json
from zipfile import ZipFile

def json_readr(file):
    '''
    Iterates over lines and
    creates a Python generator object 
    out of a JSON file
    '''
    for line in open(file, mode='r'):
        yield json.loads(line)

def unzip(file):
    '''
    Unzip file and save unzipped file in a directory 'unzipped'
    '''
    with ZipFile(file, 'r') as f:
        f.extractall('unzipped')

def unzip_all(directory):
    '''
    Unzips all files in a given directory
    Saves unzipped files in a directory 'unzipped'
    '''
    for file in os.listdir(directory):
        # Make directory if not already made
        try:
            os.mkdir('unzipped')
        except:
            pass
        # Extract file
        if file.endswith('.zip'):
            path = os.path.abspath(f'{directory}/{file}')
            unzip(path)

class Reader(object):
    '''
    Useful wrapper for iterating
    over Python Generator
    '''
    def __init__(self, g):
        self.g = g

    def read(self, n=0):
        try:
            return next(self.g)
        except StopIteration:
            return ''

if __name__ == '__main__':
    #unzip('airlines_complete/airlines-1472662091753.json.zip')
	#unzip_all('airlines_complete')
    pass
