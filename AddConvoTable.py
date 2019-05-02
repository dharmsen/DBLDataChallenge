from DataBaseInterface import LoadDatabaseAsDF
import pandas as pd

df = LoadDatabaseAsDF('10_jsons.db')
print(df.shape)

parent_tweetid = df[df['in_reply_to_status_id'].isna()]['id_str'].astype('int64')
parent_userid = df[df['in_reply_to_status_id'].isna()]['(\'user\', \'id_str\')'].astype('int64')
assert len(list(parent_tweetid)) == len(list(parent_userid)), 'no equal in length'
responses = [[] for n in range(0, len(list(parent_tweetid)))]

df_final = pd.DataFrame({'parent_tweetid' : parent_tweetid, 'parent_user_id': parent_userid, 'responses' :  responses})
print(df_final.columns)
print(df_final.shape)


df_replies = df[~df['in_reply_to_status_id'].isna()]
print(df_replies.shape)

unadded_children = []
added_tweets = []
for tweet_id,reply_id in zip(list(df_replies['id_str'].astype('int64')),list(df_replies['in_reply_to_status_id'].astype('int64'))):
     if reply_id in list(df_final['parent_tweetid']):
        reply_tweet = df_replies[df_replies['id_str'].astype('int64')==tweet_id].iloc[0]
        tweet_entry = ((int(reply_tweet['id_str'])),
            int(reply_tweet['(\'user\', \'id_str\')']),
            int(reply_tweet['in_reply_to_status_id']))
        current_response = df_final[df_final['parent_tweetid'].astype('int64')==reply_id].iloc[0]['responses']
        current_response.append(tweet_entry)
        df_final[df_final['parent_tweetid']==reply_id].iloc[0]['responses'] = current_response
        added_tweets.append((tweet_id,reply_id))
     else:
        unadded_children.append((tweet_id, reply_id))

print(df_final.shape)
print('added tweets: ' + str(len(added_tweets)))
print('unadded tweets: ' + str(len(unadded_children)))

# while len(unadded_children) > 0:
#     for child_tweetid, child_replyid in unadded_children:
#         for parent_tweetid, parent_replyid in added_tweets:
#             if child_replyid == parent_replyid:
#                 unadded_children


df_final.to_csv('convo_10_jsons.csv')
