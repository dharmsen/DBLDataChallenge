#create database based on a dataframe
import pandas as pd
import sqlite3 #To write database

def SaveDataFrameAsDB(dataframes, tables, filename='maintable.db'):
    '''
    Saves dataframes as tables to a database specified by filename, and returns
    the filename.

    Input: dataframes - list of DataFrames
    tables - list of strings with names of tables to add to database
    filename (optional, default='maintable.db') - string of filename of the database

    Output : filename of database
    '''
    if '.db' not in filename:
        filename = filename + '.db'
        print('appended .db file extentions to filename')

    cxn = sqlite3.connect(filename)
    print(type(dataframes))
    for df, table in zip(dataframes,tables):
        df.to_sql(table, cxn, index=False, if_exists='replace')

    return filename

def LoadDatabaseAsDF(filename, tables, n_rows=None):
    '''
    Returns a list of Pandas DataFrames (with optionally n_rows amount of rows
    from table), extracted from tables in database filename.

    Input: filename - string of filename of the database
    tables - list of strings with names of tables
    n_rows (optional, default=None) - number of rows to extract from table

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
            print('creating dataframe from table ' + tables[i])
            query = "SELECT * FROM " + tables[i] + f' LIMIT {n_rows}'
            df = pd.read_sql_query(query, cnx)
            dfList.append(df)
    else:
        for i in range(len(tables)):
            print('creating dataframe from table ' + tables[i])
            query = "SELECT * FROM " + tables[i]
            df = pd.read_sql_query(query, cnx)
            dfList.append(df)

    if len(dfList) == 1:
        return dfList[0]
    else:
        return dfList

if __name__ == "__main__":
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    SaveDataFrameAsDB(df)
    df2 = LoadDatabaseAsDF('maintable.db')
    print(df2)
