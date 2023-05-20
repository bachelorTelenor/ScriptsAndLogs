import csv
from datetime import datetime as dt
import datetime

GPSLoggerCSV = "GPSLoggerKombinert.csv"

with open(GPSLoggerCSV, 'r') as gpsData_csv:
    gpsData = csv.reader(gpsData_csv)
    next(gpsData)
    for l in gpsData:
        gpsTime = l[0]
        gpstimedatetime = dt.strptime(gpsTime, '%Y-%m-%dT%H:%M:%S.%fZ')
        print(type(gpstimedatetime))
