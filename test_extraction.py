from conversation_data_extractor import conversation_extractor
from DataBaseInterface import SaveDataFrameAsDB, LoadDatabaseAsDF

if __name__ == '__main__':
    extractor = conversation_extractor('test_file.json', features=['id', 'text',
                                                                   'lang', 'created_at',
                                                                   'in_reply_to_status_id',
                                                                   'in_reply_to_user_id',
                                                                   'in_reply_to_screen_name'])
    dataframe = extractor.make_dataframe()
    print(dataframe.head(2))
    print(f'Shape: {dataframe.shape}')
    print('\n')

    print('dumping dataframe in database test_file.db')
    SaveDataFrameAsDB(dataframe, filename='test_file.db')

    print('\n')
    print('loading dataframe again as sanitycheck')
    df2 = LoadDatabaseAsDF('test_file.db')
    print(df2.head(2))
    print(f'Shape: {df2.shape}')
