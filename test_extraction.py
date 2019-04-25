from conversation_data_extractor import conversation_extractor

if __name__ == '__main__':
    extractor = conversation_extractor('test_file.json', ['id', 'id_str'])
    print(extractor.features)
    dataframe = extractor.make_dataframe(content=[])
    print(dataframe)