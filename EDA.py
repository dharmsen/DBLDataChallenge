##OPEN THE DATASET

from DataBaseInterface import LoadDatabaseAsDF
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns  # also improves the look of plots
sns.set()  # set Seaborn defaults
import numpy as np

dataframe = LoadDatabaseAsDF('test_file.db')


print (dataframe.head())
print (dataframe.describe())

#Show all the column's names
print(list(dataframe.columns))

######EXPLANATION OF ALL COLUMNS

#id_str is the unique id of the tweet
#text is the tweet itself
#lang is the language of the tweet
#created_at is where the tweet was created in UTC time
#example : "created_at":"Wed Aug 27 13:08:45 +0000 2008"
#in_reply_to_status_id if tweet is a reply, has the id of the OG tweet
#in_reply_to_user_id if tweet is a reply, has the id of OG tweeter
#in_reply_to_screen_name if tweet is a repy, has the name of OG tweeter
#user is a dict that contains info on the tweeter



##SHOW SOME DATA
print(dataframe[['text', 'lang']].head(50))

#It makes sense to show how many languages we have
#searching for the code to make a pie chart/histogram of all languages

#Visualize the lengths of tweets
listy = []
for tweet in range(len(dataframe['text'])):
    listy.append(len(dataframe['text'][tweet]))


plt.plot(listy, marker="o", linestyle='')
plt.show()
plt.plot(listy)
plt.show()

#Check how many tweets are replies (if in_reply_to_status_id is not null)
Are_Replies = dataframe['in_reply_to_status_id'].notnull()

##This Code wont work yet, Im trying to plot the amount of replies

plt.plot(dataframe[Are_Replies])
plt.show()