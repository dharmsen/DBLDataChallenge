import json
import pandas as pd
import numpy as np


class conversation_extractor:
    def __init__(self, path, features):
        self.path = path
        self.features = features
        self.generator = self.json_readr()
        self.dataframe = self.make_dataframe()

    def json_readr(self):
        '''
        Iterates over lines and
        creates a Python generator object
        out of a JSON file
        '''
        for line in open(self.path, mode='r'):
            yield json.loads(line)

    def set_features(self, features):
        self.features = features

    def set_features(self):
        return self.features

    def get_dataframe(self):
        return self.dataframe

    # def read_tweets(self):
    #     tweets = []
    #     for tweet in self.generator:
    #         tweets.append(type(tweet))
    #     return tweets

    # def get_columns(self, features):
    #     list_of_lists = []
    #     for feat in features:
    #         feature_list = []
    #         for item in self.generator:
    #             feature_list.append(item[feat])
    #         list_of_lists.append(feature_list)
    #     return list_of_lists

    def add_content(self):
        count = list(np.arange(0,10))
        for counting, entry in zip(count, self.generator):
            row_content = []
            row_content.append(entry['id'])
            print(self.make_dataframe(content=row_content))
            self.dataframe.append(self.make_dataframe(content=row_content))

    def make_dataframe(self, content=[]):
        '''
        Create dataframe
        '''

        if len(content) == 0:
            dataframe = pd.DataFrame(columns=self.features)
        else:
            assert len(content) == len(self.features), 'length of content and features are not equal'
            dataframe = pd.DataFrame(content, columns=self.features)
        return dataframe


if __name__ == '__main__':
        fp = "C://Users//20181884//Documents//Y1Q4//DBL//airlines_complete//airlines-1464602228450//airlines-1464602228450.json"
        converter = conversation_extractor(fp, ['id'])
        converter.add_content()
        print(converter.get_dataframe())
