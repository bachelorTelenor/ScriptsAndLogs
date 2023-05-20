import matplotlib.pyplot as plt
import csv
from datetime import datetime as dt

logPath = "Logs/iperfband2.csv"

# plt.style.use("fivethirtyeight")

time = []
download = []



with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        time.append(dt.strptime(row['Timestamp'], '%Y-%m-%dT%H:%M:%SZ'))
        download.append(float(row['Mb/s']))

plt.grid(zorder=0)
plt.plot(time, download, label='Download Speed', zorder=3)

plt.title("Download Speed")
plt.xlabel("Time")
plt.ylabel("Download speed (Mb/s)")
# plt.legend()

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AvrageDownload.svg")
