import json
import pandas as pd


class conversation_extractor:
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
            yield json.loads(line)

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
        rows = []
        for _ in self.generator:
            rows.append(self.features)
        return rows

    def make_dataframe(self, content=[]):
        dataframe = pd.DataFrame(columns=self.features)
        if len(content) == 0:
            pass
        else:
            assert len(content) == len(self.features), 'length of content and features are not equal'
            content = self.add_content()
            for row in content:
                dataframe.append(row)
        return dataframe


#if __name__ == '__main__':
#    pass
