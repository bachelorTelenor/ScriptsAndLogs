import matplotlib.pyplot as plt
import csv

logPath = "Logs/KombinertLog.csv"

# plt.style.use("fivethirtyeight")

d1800 = []
d800 = []

with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIband']) == 1800:
            d1800.append(int(row['MERAKIrsrp']))
        elif int(row['MERAKIband']) == 800:
            d800.append(int(row['MERAKIrsrp']))

plt.grid(zorder=0)
plt.plot(d1800, zorder=3, label="1800")
plt.plot(d800, zorder=3, label="800")

plt.title("RSRP in 1800 and 800 band")
plt.ylabel("RSRP")
plt.ylim([-120, -70])
plt.legend()

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AvrageDownload.svg")
