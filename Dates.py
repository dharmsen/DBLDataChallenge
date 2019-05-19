import pandas as pd
from DataBaseInterface import LoadDatabaseAsDF

dflists = LoadDatabaseAsDF('ALL_DATA_32_FEATURES.db', ['tweets', 'conversations'], n_rows=500000)
tweets_df = dflists[0]
conversations_df = dflists[1]

#Original Code to put dates in new columns
tweets_df['weekday'] = tweets_df.created_at.str[:3]
tweets_df['month'] = tweets_df.created_at.str[4:7]
tweets_df['day'] = tweets_df.created_at.str[8:10]
tweets_df['hour'] = tweets_df.created_at.str[12:13]
tweets_df.head()
dates_df = tweets_df[['id_str', 'weekday', 'month', 'day', 'hour']]

#Open the Convo table
df = pd.read_csv('ALL_CONVERSATIONS_WRANGLED.csv')

#####Shadiah's try to merge columns on convo table######

# Make list with all id's from conversation table
useful_list = list(df['tweet_ids'])
parents_too = [str(item[1:19]) for item in useful_list]

# Make list of all id's from Dates table
dates_list = list(dates_df['id_str'])

empty = []
# For every single aidee(id) in the list of convo id's
# Try to see on what index the dates id appears in the convo id list
for aidee in range(len(list(parents_too[:1000]))):
    try:
        the_index = parents_too.index(dates_list[aidee])
        index_df = pd.DataFrame(columns=['Order'])
        empty.append(the_index)
    except ValueError:
        the_index = -1

# index_df.loc[the_index].append(dates_df.iloc[:,2], ignore_index =True)
# make a dataframe that contains these id's in order(not necessary)
# other_ids_df = pd.DataFrame(empty)
# other_ids_df.columns = ['parent_id']
###############################################################

#Carlo's code to make date columns
created_ats = []
# Check every tweet in the database
for row in tweets_df:
    for parent in parents_too:
        # If the tweet id is equal to the parent in conversation
        if row['id_str'] == parent:
            created_ats.append(row['created_at'])

# Make a created_at column for every conversation
df['created_at'] = created_ats

# Seperate created_at column and create new columns with the technique you used prevously
df['weekday'] = df.created_at.str[:3]
df['month'] = df.created_at.str[4:7]
df['day'] = df.created_at.str[8:10]
df['hour'] = df.created_at.str[12:13]