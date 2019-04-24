import os
import datetime
import csv
#import time

DATA_FILEPATH = "C://Users/20181884//Documents//Y1Q4/DBL//airlines_complete"

dates = []
dates_string = []
file_names = []
for item in os.listdir(DATA_FILEPATH):
    epoch = int(float(item.replace(".json", "").replace("airlines-", ""))/1000)

    file_names.append(item)
    dates.append(datetime.datetime.fromtimestamp(epoch))
    dates_string.append(datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d'))

with open('dates_string.csv', 'w', encoding='utf8', newline="") as output:
    writer = csv.writer(output, delimiter=',')
    for row in zip(file_names, dates, dates_string):
        writer.writerow(row)
