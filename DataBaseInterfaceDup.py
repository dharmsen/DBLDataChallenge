#create database based on a dataframe
import pandas as pd
import sqlite3 #To write database

def SaveDataFrameAsDB(dataframes, filename='maintable.db', tables):
    '''
    Returns a database of tables with names tables extracted from dataframes to
    filename

    Input: dataframes - list of DataFrames
    filename - string of filename of the database
    tables - list of strings with names of tables to add to database

    Output : filename of database
    '''
    cxn = sqlite3.connect(filename)
    for i in range(len(dataframes)):
        print('saving dataframe ' + str(i) + ' to ' + filename)
        dataframes[i].to_sql(tables[i], cxn, index=False, if_exists='replace')

    return filename

def LoadDatabaseAsDF(dataframes, filename, tables, n_rows=None):
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
    if n_rows != None:
        for i in range(len(tables)):
            print('creating dataframe ' + dataframes[i] + 'from table' + tables[i])
            query = "SELECT * FROM " + tables[i] + f'LIMIT {n_rows}'
            exec('{} = pd.read_sql_query(query, cnx)''.format(dataframes[i]))
            exec('dfList.append({})'.format(dataframes[i]))
    else:
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
