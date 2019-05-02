#create database based on a dataframe
import pandas as pd
import sqlite3 #To write database

def SaveDataFrameAsDB(df, filename='maintable.db'):
    print('saving dataframe to ' + filename)
    cxn = sqlite3.connect(filename)
    df.to_sql("tweets", cxn, index=False, if_exists='replace')

    return 'table.db'

def LoadDatabaseAsDF(filename, n_rows=None):

    if '.db' not in filename:
        filename = filename + '.db'
        print('appended .db file extentions to filename')

    print('reading from ' + filename)

    cnx = sqlite3.connect(filename)
    if n_rows != None:
        df = pd.read_sql_query(f"SELECT * FROM tweets LIMIT {n_rows}", cnx)
    else:
        df = pd.read_sql_query("SELECT * FROM tweets", cnx)
    return df

if __name__ == "__main__":
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    SaveDataFrameAsDB(df)
    df2 = LoadDatabaseAsDF('maintable.db')
    print(df2)
