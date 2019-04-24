import os
import datetime
import csv
#import time

DATA_FILEPATH = "C://Users/20181884//Documents//Y1Q4/DBL//airlines_complete"

def getDates(fp):
    dates = []
    dates_string = []
    file_names = []
    for item in os.listdir(DATA_FILEPATH):
        epoch = int(float(item.replace(".json", "").replace("airlines-", ""))/1000)

        file_names.append(item)
        dates.append(datetime.datetime.fromtimestamp(epoch))
        dates_string.append(datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d'))

    return file_names, dates_string

def saveFile(file_names, dates_string):
    with open('dates_string.csv', 'w', encoding='utf8', newline="") as output:
        writer = csv.writer(output, delimiter=',')
        for row in zip(file_names, dates_string):
            writer.writerow(row)

if __name__ == '__main__':
    a, b = getDates(DATA_FILEPATH)
    saveFile(a, b)
