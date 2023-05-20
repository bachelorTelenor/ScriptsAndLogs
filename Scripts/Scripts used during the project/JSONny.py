import json
import datetime
import csv

jsonfile = "./Logs/iperf11.48.26.04.23.json"
csvpath = jsonfile.replace(".json", ".csv")

f = open(csvpath, 'w', newline='')
writer = csv.writer(f)
csvHeader = ['Timestamp', 'Mb/s']
writer.writerow(csvHeader)
f.close()

with open(jsonfile) as data_file:
    data = json.load(data_file)
    starttime = data['start']['timestamp']['timesecs']
    timestamp = datetime.datetime.fromtimestamp(starttime)
    timestamp = timestamp - datetime.timedelta(hours=1)
    orginialStart = timestamp
    for l in data["intervals"]:
        timestampPrint = timestamp.strftime("%Y-%m-%dT%H-%M-%SZ")
        Mbs = str(round((l['sum']['bits_per_second']/1024/1024), 2))
        csvRow = [timestampPrint, Mbs]
        f = open(csvpath, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(csvRow)
        f.close()
        timedelta = l['sum']['start']
        timestamp = orginialStart + datetime.timedelta(0, timedelta)
