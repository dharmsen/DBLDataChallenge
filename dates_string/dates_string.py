import os
import datetime
import csv
#import time

DATA_FILEPATH = "C://Users/20181884//Documents//Y1Q4/DBL//airlines_complete"

def getDates(fp):
    dates_epoch = []
    dates_string = []
    file_names = []
    for item in os.listdir(DATA_FILEPATH):
        epoch = int(float(item.replace(".json", "").replace("airlines-", ""))/1000)

        file_names.append(item)
        dates_epoch.append(epoch)
        dates_string.append(datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d'))

    return file_names, dates_string

def saveFile(file_names, dates_string):
    with open('dates_string.csv', 'w', encoding='utf8', newline="") as output:
        writer = csv.writer(output, delimiter=',')
        for row in zip(file_names, dates_string):
            writer.writerow(row)

def findEarliestDate(list):
    earliest = datetime.datetime.strptime(list[0],'%Y-%m-%d')
    for date in list:
        if datetime.datetime.strptime(date,'%Y-%m-%d') <= earliest:
            earliest = datetime.datetime.strptime(date,'%Y-%m-%d')
    return earliest

def firstMonthFileNames(file_names, dates, amountofdays=31):
    earliest = findEarliestDate(dates)
    last_date = earliest + datetime.timedelta(days=amountofdays)
    in_time_frame = []
    for instance in zip(file_names, dates):
        loop_date = datetime.datetime.strptime(instance[1], '%Y-%m-%d')
        if loop_date <= last_date:
            in_time_frame.append(instance[0])

    return in_time_frame

if __name__ == '__main__':
    a, b = getDates(DATA_FILEPATH)
    saveFile(a, b)
    print("FileNames of First 31 days:")
    print("\n")
    print(firstMonthFileNames(a, b))
