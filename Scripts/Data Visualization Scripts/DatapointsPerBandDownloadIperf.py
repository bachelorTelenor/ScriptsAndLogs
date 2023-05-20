import matplotlib.pyplot as plt
import csv

logPath = "Logs/iperfBand.csv"

# plt.style.use("fivethirtyeight")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+50, y[i], ha='center')


bands = ['800', '900', '1800', '2100']
d800 = []
d900 = []
d1800 = []
d2100 = []

with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if int(row['Band']) == 800:
            d800.append(float(row['Mb/s']))
        elif int(row['Band']) == 900:
            d900.append(float(row['Mb/s']))
        elif int(row['Band']) == 1800:
            d1800.append(float(row['Mb/s']))
        elif int(row['Band']) == 2100:
            d2100.append(float(row['Mb/s']))

d800avg = len(d800)
d900avg = len(d900)
d1800avg = len(d1800)
d2100avg = len(d2100)


averages = [d800avg, d900avg, d1800avg, d2100avg]
plt.grid(zorder=0, axis='y')
plt.bar(bands, averages, zorder=3)

addlabels(bands, averages)

plt.title("Datapoints per band")
plt.xlabel("Frequency bands (MHz)")
plt.ylabel("Number of dataponts")

plt.tight_layout()
plt.show()
# plt.savefig("Graph/DatapointsPerBandDownloadAllData.svg")
