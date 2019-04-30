from DataBaseInterface import LoadDatabaseAsDF
import pandas as pd

df = LoadDatabaseAsDF('10_jsons.db')
parent_tweetid = df[df['in_reply_to_status_id'].isna()]['id_str']
parent_userid = df[df['in_reply_to_status_id'].isna()]['(\'user\', \'id_str\')']

print(df.shape)

df_final = pd.DataFrame(index=parent_tweetid, columns=['parent_user_id', 'responses'])
df_final.reset_index(level=0, inplace=True)
df_final['parent_user_id'] = parent_userid
print(df_final.shape)

df_replies = df[~(df['in_reply_to_status_id'].isna())]
print(df_final.head())
print(df_replies.head())

for item in list(df_replies['in_reply_to_status_id']):
    # print(item in list(df_final['id_str']))
    #print(list(df_final['id_str']))
    if item in list(df_final['id_str']):
        print('hey')
        tweet_entry = (df_replies[df_replies['in_reply_to_status_id']==item]['id_str'],
            df_replies[df_replies['in_reply_to_status_id']==item]['(\'user\', \'id_str\')'],
            df_replies[df_replies['in_reply_to_status_id']==item]['in_reply_to_status_id'])
        current_response = df_final['responses'][item]
        current_response.append(tweet_entry)
        df_final.at['item', current_response]
    # else:
        # print('parent not in there')

print(df_final[~(df_final['responses'].isna())].head(5))
