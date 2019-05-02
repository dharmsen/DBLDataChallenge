import DataBaseInterfaceDup
import pandas as pd
import csv

df1 = DataBaseInterfaceDup.LoadDatabaseAsDF('10_jsons.db', ['tweets',])[0]

df2 = pd.read_csv('10_jsons_convo.csv')

print(type(df1))
DataBaseInterfaceDup.SaveDataFrameAsDB([df1, df2], ['tweets', 'conversations'])

print(len(DataBaseInterfaceDup.LoadDatabaseAsDF('maintable.db', ['tweets','conversations'])))
