import DataBaseInterface
import pandas as pd
import csv
import sqlite3

conversations_df = pd.read_csv('full_db_conversations_final.csv')

cxn = sqlite3.connect('all_features_database.db')
conversations_df.to_sql('conversations', cxn, index=False, if_exists='replace')
