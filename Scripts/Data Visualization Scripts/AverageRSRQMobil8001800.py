import matplotlib.pyplot as plt
import csv

logPath = "Logs/KombinertLoggMobil1.csv"

# plt.style.use("fivethirtyeight")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]-0.3, y[i], ha='center')


bands = ['800', '1800']
d800 = []
d900 = []
d1800 = []
d2100 = []

with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['GMONBANDint']) == 800:
            d800.append(float(row['GMONRSRQ']))
        elif int(row['GMONBANDint']) == 1800:
            d1800.append(float(row['GMONRSRQ']))

d800avg = sum(d800) / len(d800)
d800avg = round(d800avg, 2)
d1800avg = sum(d1800) / len(d1800)
d1800avg = round(d1800avg, 2)


averages = [d800avg, d1800avg]
plt.grid(zorder=0, axis='y')
plt.bar(bands, averages, zorder=3)
plt.ylim([0, -17])

addlabels(bands, averages)

plt.title("Average Mobil RSRQ per band 01.03 - 17.03")
plt.xlabel("Frequency bands (MHz)")
plt.ylabel("RSRQ")

plt.tight_layout()
# plt.show()
plt.savefig("Graph/AvrageRsrqMobil8001800_0103_1703.svg")
