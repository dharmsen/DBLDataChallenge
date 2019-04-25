# DBL-DataChallenge

## WORKING WITH test_file.db
test_file.db is one json extracted. If you work in this directory, this is the code you have to add to get the database in a pandas dataframe, with which you can do whatever you want.
```
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

## unpacking_and_loading.py
Useful functions for extracting zip files and for loading JSON files.
The load functions will store the JSON file as a Python Generator.
