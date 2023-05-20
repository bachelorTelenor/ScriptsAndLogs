import matplotlib.pyplot as plt
import csv

logPath = "Logs/CombinedLogUpload.csv"

# plt.style.use("fivethirtyeight")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+0.01, y[i], ha='center')


bands = ['800', '1800']
d800 = []
d900 = []
d1800 = []
d2100 = []


with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIband']) == 800:
            d800.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 1800:
            d1800.append(float(row['IPERFmbs']))


d800avg = min(i for i in d800 if i > 0.0)
d1800avg = min(i for i in d1800 if i > 0.0)

averages = [d800avg, d1800avg]
plt.grid(zorder=0, axis='y')
plt.bar(bands, averages, zorder=3)

plt.title("Minimum speed per band")
plt.xlabel("Frequency bands (MHz)")
plt.ylabel("Download Mb/s")

addlabels(bands, averages)

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AverageDownload.svg")
