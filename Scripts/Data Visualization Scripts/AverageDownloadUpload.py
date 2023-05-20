import matplotlib.pyplot as plt
import csv
import numpy as np

download = "Logs/download.csv"
upload = "Logs/upload.csv"

# plt.style.use("fivethirtyeight")

bands = ['800', '900', '1800', '2100']

x_indexes = np.arange(len(bands))
width = 0.3

d800 = []
d900 = []
d1800 = []
d2100 = []

with open(download) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIband']) == 800:
            d800.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 900:
            d900.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 1800:
            d1800.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 2100:
            d2100.append(float(row['IPERFmbs']))

d800avg = sum(d800) / len(d800)
d800avg = round(d800avg, 2)
d900avg = sum(d900) / len(d900)
d900avg = round(d900avg, 2)
d1800avg = sum(d1800) / len(d1800)
d1800avg = round(d1800avg, 2)
d2100avg = sum(d2100) / len(d2100)
d2100avg = round(d2100avg, 2)

averagesDown = [d800avg, d900avg, d1800avg, d2100avg]

d8002 = []
d9002 = []
d18002 = []
d21002 = []

with open(upload) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIband']) == 800:
            d8002.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 900:
            d9002.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 1800:
            d18002.append(float(row['IPERFmbs']))
        elif int(row['MERAKIband']) == 2100:
            d21002.append(float(row['IPERFmbs']))

d8002avg = sum(d8002) / len(d8002)
d8002avg = round(d8002avg, 2)
d9002avg = sum(d9002) / len(d9002)
d9002avg = round(d9002avg, 2)
d18002avg = sum(d18002) / len(d18002)
d18002avg = round(d18002avg, 2)
d21002avg = sum(d21002) / len(d21002)
d21002avg = round(d21002avg, 2)

averagesUp = [d8002avg, d9002avg, d18002avg, d21002avg]
plt.grid(zorder=0)
plt.bar(x_indexes - (width / 2), averagesDown, width=width, label="Download", zorder=3)
plt.bar(x_indexes + (width / 2), averagesUp, width=width, label="Upload", zorder=3)

plt.title("Average download and Upload speed per band")
plt.xlabel("Frequency bands (MHz)")
plt.ylabel("Mb/s")
plt.legend()
plt.xticks(ticks=x_indexes, labels=bands)

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AvrageDownload.svg")
