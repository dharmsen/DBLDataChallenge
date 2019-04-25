import json
import pandas as pd


class conversation_extractor:
    '''
    Converts a single JSON file to DataFrame with
    specified features
    '''
    def __init__(self, path, features):
        self.path = path
        self.features = features
        self.generator = self.json_readr()

    def json_readr(self):
        '''
        Iterates over lines and
        creates a Python generator object
        out of a JSON file
        '''
        for line in open(self.path, mode='r'):
            try:
                yield json.loads(line)
            except json.decoder.JSONDecodeError:
                # for now
                pass

    def add_content(self):
        '''
        Creates a list of lists for constructing
        the dataframe
        '''
        rows = []
        for row in self.generator:
            try:
                rows.append([row[x] for x in self.features])
            except KeyError:
                # TODO Look into and fix KeyError with 'id'
                pass
        return rows

    def make_dataframe(self):
        '''
        Combines the features and content into a dataframe
        '''
        content = self.add_content()
        dataframe = pd.DataFrame(content, columns=self.features)
        return dataframe


