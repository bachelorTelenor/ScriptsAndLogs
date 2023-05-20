import matplotlib.pyplot as plt
import csv

logPath = "Logs/CombinedLog.csv"

# plt.style.use("fivethirtyeight")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]-0.3, y[i], ha='center')


bands = ['800', '900', '1800', '2100']
d800 = []
d900 = []
d1800 = []
d2100 = []

with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIband']) == 800:
            d800.append(float(row['MERAKIrsrq']))
        elif int(row['MERAKIband']) == 900:
            d900.append(float(row['MERAKIrsrq']))
        elif int(row['MERAKIband']) == 1800:
            d1800.append(float(row['MERAKIrsrq']))
        elif int(row['MERAKIband']) == 2100:
            d2100.append(float(row['MERAKIrsrq']))

d800avg = sum(d800) / len(d800)
d800avg = round(d800avg, 2)
d900avg = sum(d900) / len(d900)
d900avg = round(d900avg, 2)
d1800avg = sum(d1800) / len(d1800)
d1800avg = round(d1800avg, 2)
d2100avg = sum(d2100) / len(d2100)
d2100avg = round(d2100avg, 2)

averages = [d800avg, d900avg, d1800avg, d2100avg]
plt.grid(zorder=0, axis='y')
plt.bar(bands, averages, zorder=3)
plt.ylim([0, -14])

addlabels(bands, averages)

plt.title("Average RSRQ per band")
plt.xlabel("Frequency bands (MHz)")
plt.ylabel("RSRQ")

plt.tight_layout()
# plt.show()
plt.savefig("Graph/AverageRsrqBandMG21.svg")
