import matplotlib.pyplot as plt
import csv

logPath = "Logs/CombinedLogDownload.csv"

# plt.style.use("fivethirtyeight")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+0.6, y[i], ha='center')


bands = ['1', '2', '3', '4', '5']
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []


with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIrsrp']) < -111 or int(row['MERAKIrsrq']) < -16:
            d1.append(float(row['IPERFmbs']))
        elif int(row['MERAKIrsrp']) < -102 or int(row['MERAKIrsrq']) < -13:
            d2.append(float(row['IPERFmbs']))
        elif int(row['MERAKIrsrp']) < -92 or int(row['MERAKIrsrq']) < -10:
            d3.append(float(row['IPERFmbs']))
        elif int(row['MERAKIrsrp']) < -83 or int(row['MERAKIrsrq']) < -7:
            d4.append(float(row['IPERFmbs']))
        else:
            d5.append(float(row['IPERFmbs']))

d1avg = sum(d1) / len(d1)
d1avg = round(d1avg, 2)
d2avg = sum(d2) / len(d2)
d2avg = round(d2avg, 2)
d3avg = sum(d3) / len(d3)
d3avg = round(d3avg, 2)
d4avg = sum(d4) / len(d4)
d4avg = round(d4avg, 2)
if d5:
    d5avg = sum(d5) / len(d5)
    d5avg = round(d5avg, 2)
else:
    d5avg = 0

averages = [d1avg, d2avg, d3avg, d4avg, d5avg]
plt.grid(zorder=0, axis='y')
plt.bar(bands, averages, zorder=3)

plt.title("Average Download Speed per Signal Bar")
plt.xlabel("Signal Bars")
plt.ylabel("Download Mb/s")

addlabels(bands, averages)

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AverageDownloadPerSignalBarRSRQ.svg")
