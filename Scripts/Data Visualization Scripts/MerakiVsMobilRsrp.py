import matplotlib.pyplot as plt
import csv
from datetime import datetime as dt

logPath = "Logs/KombinertLog.csv"

# plt.style.use("fivethirtyeight")

time = []
rsrp = []
gmonrsrp = []


with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        time.append(dt.strptime(row['MERAKIAPIupdate'], '%Y-%m-%dT%H:%M:%S+01'))
        rsrp.append(int(row['MERAKIrsrp']))
        gmonrsrp.append(int(row['GMONRSRP']))

plt.grid(zorder=0)
plt.plot(time, rsrp, label='Meraki RSRP', zorder=3)
plt.plot(time, gmonrsrp, label='Mobil RSRP', zorder=3)

plt.title("Meraki RSRP vs Mobil RSRP")
plt.xlabel("Time")
plt.ylabel("RSRP")
plt.legend()

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AvrageDownload.svg")
