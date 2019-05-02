#create database based on a dataframe
import pandas as pd
import sqlite3 #To write database

def SaveDataFrameAsDB(df, filename='maintable.db'):
    print('saving dataframe to ' + filename)
    cxn = sqlite3.connect(filename)
    df.to_sql("tweets", cxn, index=False, if_exists='replace')

    return 'table.db'

def LoadDatabaseAsDF(dataframes, filename, tables):
    '''
    Returns a list of Pandas DataFrames with names dataframes, extracted from
    tables in database filename.

    Input: dataframes - list of strings with names for the dataframes
    filename - string of filename of the database
    tables - list of strings with names of tables

    Output: list of DataFrames with names dataframes
    '''
    if '.db' not in filename:
        filename = filename + '.db'
        print('appended .db file extentions to filename')

    print('reading from ' + filename)

    cnx = sqlite3.connect(filename)
    dfList = []
    for i in range(len(tables)):
        print('creating dataframe ' + dataframes[i] + 'from table' + tables[i])
        query = "SELECT * FROM " + tables[i]
        exec('{} = pd.read_sql_query(query, cnx)''.format(dataframes[i]))
        exec('dfList.append({})'.format(dataframes[i]))

    return dfList

if __name__ == "__main__":
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    SaveDataFrameAsDB(df)
    df2 = LoadDatabaseAsDF('maintable.db')
    print(df2)
