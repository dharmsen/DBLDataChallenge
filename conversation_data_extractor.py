import os
import json
import pandas as pd


class conversation_extractor:
    '''
    Converts a single JSON file to DataFrame with
    specified features
    '''
    def __init__(self, directory, features):
        self.features = features
        self.generator = self.json_readr()
        self.directory = directory
        self.items = os.listdir(directory)[:5]

    def json_readr(self):
        '''
        Iterates over lines and
        creates a Python generator object
        out of a JSON file
        '''
        i = 1
        for file in self.items:
            if not file.endswith('.json'): continue
            print(f'Loading file {i}/{len(self.items)}: {file}')
            for line in open(self.directory + file, mode='r'):
                try:
                    yield json.loads(line)
                except json.decoder.JSONDecodeError: #or UnicodeDecodeError:
                    # TODO handle this
                    pass
            i += 1


    def add_content(self):
        '''
        Creates a list of lists for constructing
        the dataframe
        '''
        rows = []
        for row in self.generator:
            try:
                rows.append([row[x] if isinstance(x, str) else row[x[0]][x[1]] for x in self.features])
            except KeyError:
                # TODO Look into and fix KeyError with 'id'
                pass
        return rows

    def make_dataframe(self):
        '''
        Combines the features and content into a dataframe
        '''
        content = self.add_content()
        print(content)
        dataframe = pd.DataFrame(content, columns=self.features)
        return dataframe
