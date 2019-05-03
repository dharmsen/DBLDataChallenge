# DBL-DataChallenge

## IMPORTING DATABASES AS DATAFRAME
1. Download a database file from drive.
2. create your script/notebook in the same folder as the DataBaseInterface.py file and the .db file you've downloaded.
3. choose whether you want to import tweets and conversations in two dataframes, or just one. You do this with the second argument that is a list of the table names.

* The LoadDatabaseAsDF returns a list of  two dataframes if you enter ```['tweets', 'conversations']```.
* The LoadDatabaseAsDF returns one dataframe if you enter ```['tweets',]```.
* The LoadDatabaseAsDF returns one dataframe if you enter ```['conversations',]```.

NOTE: the conversations table in the db is not very informative, if you want to have quicker insight in the conversations, check out the section "importing conversation CSV's" below.

You can select how many rows you want returned by adding the extra n_rows argument. Recommended would be to do this when coding so the running times are quicker and then for the final run / visualization import the entirety by removing the n_rows= argument.

The following code imports 500000 rows of both tables and assigns the dataframes to the variables tweets_df and conversations_df.

```
import pandas as pd
from DataBaseInterface import LoadDatabaseAsDF

dflists = LoadDatabaseAsDF('ALL_DATA_32_FEATURES.db', ['tweets', 'conversations'], n_rows=500000)
tweets_df = dflists[0]
conversations_df = dflists[1]
```

## IMPORTING CONVERSATION CSV'S
You can also import the conversation files from the csvs in the repo. Make sure you create your script/notebook in the same folder as the DataBaseInterface.py file and the .csv file.

The code below is very simple and should be self-explanatory.
```
df = pd.read_csv('ALL_CONVERSATIONS_WRANGLED.csv')
```

### accessing the tweet_ids and user_ids
The tweet_ids and user_ids are in a string format but can be converted to a list using the built-in eval() function in Python. Example:
```
# ----------- Get all tweet ids of a conversation ----
sample_conv_tweet_ids = eval(df['tweet_ids'][0])
# sample_conv_tweet_ids is now a list of all tweet ids for one conversation (the first)

# ----------- Get all user ids of a conversation ----
sample_conv_user_ids = eval(df['user_ids'][0])
# sample_conv_user_ids is now a list of all user ids for one conversation (the first)
```

### Column description
- conversation_id: We will use this to specify which conversation we are talking about.
- raw_tweets_info: Just there for reference. Not useful to use for analysis.
- conversation_length: The amount of tweets that are in the conversation.
- tweet_ids: a list of tweet ids ('id_str in the database) of the conversation.
- user_ids: A list of all the user ids ("('user', 'id_str')" in the database) that are involved in the conversation.
