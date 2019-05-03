from DataBaseInterface import LoadDatabaseAsDF
import pandas as pd
import csv
from datetime import datetime
import numpy as np

df = LoadDatabaseAsDF('full_conversation_database.db', ['tweets',])
print(df.shape)

def TweetEntry(row):
    tweetid = int(row['id_str'])
    userid = int(row["(\'user\', \'id_str\')"])

    return (tweetid, userid)

def SaveProgress(conversations_dict, wanted_dict, id):
    fp = 'full_db_conversations_' + str(id) + '.csv'
    with open(fp, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in conversations_dict.items():
           writer.writerow([key, value])

    fp2 = 'wanted_dict_at_'+str(id)+'.csv'
    with open(fp2, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in wanted_dict.items():
           writer.writerow([key, value])

conversations = {}
wanted = {}
startTime = datetime.now()
error_count = 0

for item, row in df[::-1].iterrows():
    if ((int(item) % 10000) == 0):
        print('At row ' + str(item))
        print('There are ' + str(conversation_id) + ' conversations so far')
        print('There are ' + str(len(wanted)) + ' wanted tweets so far')
        print('running time.. ' + str(datetime.now() - startTime))
        print('=============================================================')
    if ((int(item) % 250000) == 0):
        SaveProgress(conversations, wanted, item)

    if int(row['id_str']) in wanted:
        conversation_id = wanted[int(row['id_str'])]
        try:
            current_entry = conversations[conversation_id]
            current_entry.append(TweetEntry(row))
            conversations[conversation_id] = current_entry
            del wanted[int(row['id_str'])]
        except AttributeError:
            print('nonetype error at ' + str(item))
            error_count += 1

        if not np.isnan(row['in_reply_to_status_id']):
                wanted[row['in_reply_to_status_id']] = conversation_id
    elif not np.isnan(row['in_reply_to_status_id']):
        conversations_count = len(conversations)
        conversations[conversations_count] = [TweetEntry(row),]
        wanted[int(row['in_reply_to_status_id'])] = conversations_count

SaveProgress(conversations, wanted, 'final')

print('At row ' + str(item))
print('There are ' + str(conversation_id) + 'conversations FINAL')
print('There are ' + str(len(conversations)) + 'wanted tweets FINAL')
print('running time.. ' + str(datetime.now() - startTime))
print('=============================================================')
print('error count ' + str(error_count))
