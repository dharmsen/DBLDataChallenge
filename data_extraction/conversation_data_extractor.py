import os
import json
import pandas as pd

class conversation_extractor:
    '''
    Converts multiple JSON files to a DataFrame with
    specified features
    '''
    def __init__(self, directory, features):
        self.features = features
        self.generator = self.json_readr()
        self.cwd =  os.getcwd()
        self.directory = directory
        self.items = os.listdir(directory)

    def json_readr(self):
        '''
        Iterates over lines and
        creates a Python generator object
        out of JSON files
        '''
        i = 1
        for file in self.items:
            if not file.endswith('.json'): continue
            print(f'Loading file {i}/{len(self.items)}: {file}')
            n = 1
            for line in open(self.directory + file, mode='r'):
                try:
                    yield json.loads(line)
                except json.decoder.JSONDecodeError:
                    print(f'--JSONDecodeError at file: [{file}], line: [{n}]--')
                n += 1
            i += 1

    def add_content(self):
        '''
        Creates a list of lists for constructing
        the DataFrame
        '''
        i = 1
        rows = []
        for row in self.generator:
            try:
                rows.append([row[x] if isinstance(x, str) else row[x[0]][x[1]] for x in self.features])
            except KeyError:
                # TODO Look into and fix KeyErrors
                print('KeyError')
            i += 1
        return rows

    def make_dataframe(self):
        '''
        Combines the features and content into a DataFrame
        '''
        content = self.add_content()
        print(content)
        dataframe = pd.DataFrame(content, columns=self.features)
        return dataframe
