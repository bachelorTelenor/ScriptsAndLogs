import matplotlib.pyplot as plt
import numpy as np
import csv

logPath = "Logs/CombinedLog.csv"

# plt.style.use("fivethirtyeight")

rsrp = []
download = []
band = []

with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        rsrp.append(int(row['MERAKIrsrp']))
        download.append(float(row['IPERFmbs']))
        band.append(int(row['MERAKIband']))


f, (ax, ax2, ax3) = plt.subplots(3, 1, sharex=True)


ax.grid(zorder=0)
ax2.grid(zorder=0)
ax3.grid(zorder=0)
ax2.plot(rsrp, zorder=3, label='RSRP', color="#ff7f0e")
ax.plot(download, zorder=3, label='Mb/s')
ax3.plot( band, zorder=3, label='Band', color="#de5253")


# plt.title("RSRP in 800-band")
# plt.ylabel("RSRP")
# plt.ylim([-140, -70])
ax.legend(loc='upper right', fontsize='x-large')
ax2.legend(loc='upper right', fontsize='x-large')
ax3.legend(loc='upper right', fontsize='x-large')

plt.tight_layout()
plt.show()
# plt.savefig("Graph/AvrageDownload.svg")
