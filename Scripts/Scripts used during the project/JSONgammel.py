import json
import datetime
import csv

jsonfile = "iperf3Client_kl14_04.json"
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
        Mbs = str(round((l['streams'][0]['bits_per_second']/1024/1024), 2))
        csvRow = [timestampPrint, Mbs]
        f = open(csvpath, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(csvRow)
        f.close()
        timedelta = l['streams'][0]['start']
        timestamp = orginialStart + datetime.timedelta(0, timedelta)
