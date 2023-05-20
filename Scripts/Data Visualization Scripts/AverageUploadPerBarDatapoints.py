import matplotlib.pyplot as plt
import csv

logPath = "Logs/CombinedLogUpload.csv"

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

d1avg = len(d1)
d2avg = len(d2)
d3avg = len(d3)
d4avg = len(d4)
d5avg = len(d5)


averages = [d1avg, d2avg, d3avg, d4avg, d5avg]
plt.grid(zorder=0, axis='y')
plt.bar(bands, averages, zorder=3)

plt.title("Datapoints per Signal Bar Upload")
plt.xlabel("Signal Bars")
plt.ylabel("Datapoints")

addlabels(bands, averages)

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AverageUploadPerSignalBarRSRQ.svg")
