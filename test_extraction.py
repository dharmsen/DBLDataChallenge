import os
from conversation_data_extractor import conversation_extractor
from DataBaseInterface import SaveDataFrameAsDB, LoadDatabaseAsDF

if __name__ == '__main__':
    directory = 'test_directory/'
    items = os.listdir(directory)
    extractor = conversation_extractor(directory=directory, features=['id_str', 'text',
                                                                   'lang', 'created_at',
                                                                   'in_reply_to_status_id',
                                                                   'in_reply_to_user_id',
                                                                   'in_reply_to_screen_name',
                                                                   ('user', 'id_str')])
    dataframe = extractor.make_dataframe()
    print(dataframe.head(2))
    print(f'Shape: {dataframe.shape}')
    print('\n')

    print('dumping dataframe in database test_file.db')
    SaveDataFrameAsDB(dataframe, filename='test_file2.db')

    print('\n')
    print('loading dataframe again as sanitycheck')
    df2 = LoadDatabaseAsDF('test_file2.db')
    print(df2.head(2))
    print(f'Shape: {df2.shape}')
