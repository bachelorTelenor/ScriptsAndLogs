from datetime import datetime as dt
import datetime
import csv

merakiCSV = "./Logs/meraki.csv"
kobinertCSV = "./Logs/MerakiLogKombinertBand.csv"

f = open(kobinertCSV, 'w', newline='')
writer = csv.writer(f)
csvHeader = ['MERAKIAPIquery', 'MERAKIAPIupdate', 'MERAKIrsrp', 'MERAKIrsrq', 'MERAKIband', 'TestDirection']
writer.writerow(csvHeader)
f.close()

with open(merakiCSV, 'r') as merakiData_csv:
    merakiData = csv.reader(merakiData_csv)
    next(merakiData)
    for row in merakiData:
        merakiTime = row[1]
        merakiTime = dt.strptime(merakiTime, '%Y-%m-%dT%H:%M:%SZ')
        merakiTime = merakiTime + datetime.timedelta(hours=1)
        merakiTimeCSV = merakiTime.strftime('%Y-%m-%dT%H:%M:%SZ')
        band = 1800
        if merakiTime <= datetime.datetime(2023, 3, 13, 8, 54, 48):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 0, 48):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 2, 29):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 14, 7):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 37, 27):
            band = 2100
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 44, 30):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 56, 47):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 9, 57, 28):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 10, 1, 51):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 10, 2, 0):
            band = 2100
        elif merakiTime <= datetime.datetime(2023, 3, 13, 10, 23, 59):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 10, 35, 0):
            band = 800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 10, 37, 49):
            band = 1800
        elif merakiTime <= datetime.datetime(2023, 3, 13, 10, 40, 59):
            band = 800
        else:
            band = 2100

        merakiCSVrow = [row[0], merakiTimeCSV, row[2], row[3], band, row[4]]
        f = open(kobinertCSV, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(merakiCSVrow)
        f.close()
