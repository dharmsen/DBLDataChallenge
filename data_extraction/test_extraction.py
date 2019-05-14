import os
from data_extraction.conversation_data_extractor import conversation_extractor
from data_extraction.DataBaseInterface import SaveDataFrameAsDB, LoadDatabaseAsDF

if __name__ == '__main__':
    directory = 'test_directory/'
    print(os.path.abspath(directory))
    #items = os.listdir(directory)
    conversation_features = ['id_str', 'text',
                             'lang', 'created_at',
                             'in_reply_to_status_id_str',
                             'in_reply_to_user_id_str',
                             'in_reply_to_screen_name',
                             ('user', 'id_str')]
    incoming_outcoming_features = ['id_str', 'created_at', 'in_reply_to_user_id_str', ('entities', 'symbols')]
    metadata_features= ('entities', 'hashtags'), ('entities', 'symbols')
    base_features = ['created_at', 'favorite_count', 'id_str',
                     'in_reply_to_status_id_str', 'in_reply_to_user_id_str',
                     'in_reply_to_screen_name', 'lang', 'retweet_count',
                     'retweeted', 'text', 'timestamp_ms', 'truncated']
    user_features = [('user', x) for x in ['created_at', 'default_profile',
                                         'description', 'favourites_count',
                                         'follow_request_sent', 'followers_count',
                                         'following', 'friends_count', 'geo_enabled',
                                         'id_str', 'lang', 'listed_count',
                                         'location', 'name', 'notifications',
                                         'protected', 'screen_name',
                                         'statuses_count', 'time_zone', 'url',
                                         'utc_offset', 'verified']]

    extractor = conversation_extractor(directory=directory, features=incoming_outcoming_features)
    dataframe = extractor.make_dataframe()
    print(dataframe.head(2))
    print(f'Shape: {dataframe.shape}')
    print('\n')

    print('dumping dataframe in database incoming_outcoming_database.db')
    SaveDataFrameAsDB(dataframe, filename='incoming_outcoming_database.db')

    print('\n')
    print('loading dataframe again as sanitycheck')
    df2 = LoadDatabaseAsDF('incoming_outcoming_database.db')
    print(df2.head(2))
    print(f'Shape: {df2.shape}')
