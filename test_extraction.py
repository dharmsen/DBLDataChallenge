from conversation_data_extractor import conversation_extractor

if __name__ == '__main__':
    extractor = conversation_extractor('test_file.json', features=['id', 'text',
                                                                   'lang', 'created_at',
                                                                   'in_reply_to_status_id',
                                                                   'in_reply_to_user_id',
                                                                   'in_reply_to_screen_name'])
    dataframe = extractor.make_dataframe()
    print(dataframe.head(2))
    print(f'Shape: {dataframe.shape}')
