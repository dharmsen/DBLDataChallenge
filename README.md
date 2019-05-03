# DBL-DataChallenge

## IMPORTING DATABASES AS DATAFRAME
1. Download a database file from drive.
2. create your script/notebook in the same folder as the DataBaseInterface.py file and the .db file you've downloaded.
3. choose whether you want to import tweets and conversations in two dataframes, or just one. You do this with the second argument that is a list of the table names.

* The LoadDatabaseAsDF returns a list of  two dataframes if you enter ```['tweets', 'conversations']```.
* The LoadDatabaseAsDF returns one dataframe if you enter ```['tweets',]```.
* The LoadDatabaseAsDF returns one dataframe if you enter ```['tweets',]```.

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

```
df = pd.read_csv('ALL_CONVERSATIONS_WRANGLED.csv')
```
