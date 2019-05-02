from DataBaseInterface import LoadDatabaseAsDF
import pandas as pd
import csv

df = LoadDatabaseAsDF('10_jsons.db')
print(df.shape)

def TweetEntry(row):
    tweetid = int(row['id_str'])
    userid = int(row["(\'user\', \'id_str\')"])

    return (tweetid, userid)

conversations = {}
conversations_count = 0
wanted = {}
for item, row in df.iterrows():
    if int(row['id_str']) in wanted:
        print('id was in wanted ' + str(item))
        conversation_id = wanted[int(row['id_str'])]
        try:
            current_entry = conversations[conversation_id]
            current_entry.append(TweetEntry(row))
            conversations[conversation_id] = current_entry
            print('list: ' + str(conversation_id) + ' ' + str(conversations[conversation_id]))
        except AttributeError:
            print('nonetype error at ' + str(item))

        if isinstance(row['in_reply_to_status_id'], float):
            wanted[row['in_reply_to_status_id']] = conversation_id
    elif isinstance(row['in_reply_to_status_id'], float):
        conversations[conversations_count] = [TweetEntry(row),]
        wanted[row['in_reply_to_status_id']] = conversations_count
        conversations_count += 1

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in conversations.items():
       writer.writerow([key, value])
