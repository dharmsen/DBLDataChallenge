# DBL-DataChallenge

## WORKING WITH test_file.db 
OUTDATED
test_file.db is one json extracted. If you work in this directory, this is the code you have to add to get the database in a pandas dataframe, with which you can do whatever you want.
```
import sys
import pandas as pd

sys.path.insert(0, '/data_extraction/')
from DataBaseInterface import LoadDatabaseAsDF

dataframe = LoadDatabaseAsDF('test_file.db')
```

## test_extraction.py
script that puts test_file.json into a database.

## dates_string.py
(Lourens) Noted that all filenames had a large integer, suspected these are epochs,
this script finds all filenames, reformats the epoch to human date, saves them to dates_string.txt
Additionally, has a method that returns the filenames of the files in the first 31 days.

## dates_string.txt
(Lourens) Result from dates_string.py

## /small_datasets/conversations_10_jsons.py
Contains conversations with at least one reply from 10 jsons. 
### Column description
- conversation_id: We will use this to specify which conversation we are talking about.
- raw_tweets_info: Just there for reference. Not useful to use for analysis.
- conversation_length: The amount of tweets that are in the conversation.
- tweet_ids: a list of tweet ids ('id_str in the database) of the conversation. 
- user_ids: A list of all the user ids ("('user', 'id_str')" in the database) that are involved in the conversation.
### accessing the tweet_ids and user_ids
The tweet_ids and user_ids are in a string format but can be converted using the built-in eval() function in Python.
Example:
```
# --------- Load in dataframe ---------------------
import sys
import pandas as pd

sys.path.insert(0, '/data_extraction/')
from DataBaseInterface import LoadDatabaseAsDF

df = LoadDatabaseAsDF('test_file.db')
# ---------------------------------------------------
# ----------- Get all tweet ids of a conversation ----
sample_conv_tweet_ids = eval(df['tweet_ids'][0])
# sample_conv_tweet_ids is now a list of all tweet ids for one conversation (the first)

# ----------- Get all user ids of a conversation ----
sample_conv_user_ids = eval(df['user_ids'][0])
# sample_conv_user_ids is now a list of all user ids for one conversation (the first)
```
