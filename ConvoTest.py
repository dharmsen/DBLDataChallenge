import DataBaseInterfaceDup
import pandas as pd
import csv

tweets_df = DataBaseInterfaceDup.LoadDatabaseAsDF('10_jsons.db', ['tweets',])[0]

conversations_df = pd.read_csv('10_jsons_convo.csv')

print(type(df1))
DataBaseInterfaceDup.SaveDataFrameAsDB([tweets_df, conversations_df], ['tweets', 'conversations'])

print(len(DataBaseInterfaceDup.LoadDatabaseAsDF('full.db', ['tweets','conversations'])))
