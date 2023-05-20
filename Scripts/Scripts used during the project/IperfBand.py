from datetime import datetime as dt
import datetime
import csv

merakiCSV = "./Logs/iperf.csv"
kobinertCSV = "./Logs/iperfBand.csv"

f = open(kobinertCSV, 'w', newline='')
writer = csv.writer(f)
csvHeader = ['Timestamp', 'Mb/s', 'Band']
writer.writerow(csvHeader)
f.close()

with open(merakiCSV, 'r') as merakiData_csv:
    merakiData = csv.reader(merakiData_csv)
    next(merakiData)
    for row in merakiData:
        merakiTime = row[0]
        merakiTime = dt.strptime(merakiTime, '%Y-%m-%dT%H-%M-%SZ')
        merakiTime = merakiTime + datetime.timedelta(hours=1)
        merakiTimeCSV = merakiTime.strftime('%Y-%m-%dT%H:%M:%SZ')
        band = 1800
        if merakiTime <= datetime.datetime(2023, 4, 26, 8, 0, 46):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 8, 12, 14):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 8, 23, 5):
            band = 900
        elif merakiTime <= datetime.datetime(2023, 4, 26, 8, 38, 15):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 8, 54, 38):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 9, 1, 45):
            band = 2100
        elif merakiTime <= datetime.datetime(2023, 4, 26, 9, 12, 35):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 9, 18, 33):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 9, 18, 56):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 9, 30, 36):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 4, 26, 9, 32, 46):
            band = 2100
        else:
            band = 1800

        merakiCSVrow = [merakiTimeCSV, row[1], band]
        f = open(kobinertCSV, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(merakiCSVrow)
        f.close()
