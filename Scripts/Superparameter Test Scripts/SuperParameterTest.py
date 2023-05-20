import csv

logPath = "Logs/CombinedLogUpload.csv"

d1 = []
d1Rsrp = []
d1Rsrq = []
d1Speed = []
d1Band = []
d2 = []
d2Rsrp = []
d2Rsrq = []
d2Speed = []
d2Band = []
d3 = []
d3Rsrp = []
d3Rsrq = []
d3Speed = []
d3Band = []
d4 = []
d4Rsrp = []
d4Rsrq = []
d4Speed = []
d4Band = []
d5 = []
d5Rsrp = []
d5Rsrq = []
d5Speed = []
d5Band = []


minRsrp = -140
maxRsrp = -70

minRsrq = -17
maxRsrq = -6

rsrpWeight = 1
rsrqWeight = 1


with open(logPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        if int(row['MERAKIrsrp']) < -111 or int(row['MERAKIrsrq']) < -16:
            rsrp = int(row['MERAKIrsrp'])
            rsrq = int(row['MERAKIrsrq'])
            Score = (rsrpWeight * ((rsrp - minRsrp) / (maxRsrp - minRsrp))) * (rsrqWeight * ((rsrq - minRsrq) / (maxRsrq - minRsrq)))
            Score = round(Score, 2)
            d1.append(Score)
            d1Rsrp.append(rsrp)
            d1Rsrq.append(rsrq)
            d1Speed.append(round(float(row['IPERFmbs']), 2))
            d1Band.append(int(row['MERAKIband']))
        elif int(row['MERAKIrsrp']) < -102 or int(row['MERAKIrsrq']) < -13:
            rsrp = int(row['MERAKIrsrp'])
            rsrq = int(row['MERAKIrsrq'])
            Score = (rsrpWeight * ((rsrp - minRsrp) / (maxRsrp - minRsrp))) * (rsrqWeight * ((rsrq - minRsrq) / (maxRsrq - minRsrq)))
            Score = round(Score, 2)
            d2.append(Score)
            d2Rsrp.append(rsrp)
            d2Rsrq.append(rsrq)
            d2Speed.append(round(float(row['IPERFmbs']), 2))
            d2Band.append(int(row['MERAKIband']))
        elif int(row['MERAKIrsrp']) < -92 or int(row['MERAKIrsrq']) < -10:
            rsrp = int(row['MERAKIrsrp'])
            rsrq = int(row['MERAKIrsrq'])
            Score = (rsrpWeight * ((rsrp - minRsrp) / (maxRsrp - minRsrp))) * (rsrqWeight * ((rsrq - minRsrq) / (maxRsrq - minRsrq)))
            Score = round(Score, 2)
            d3.append(Score)
            d3Rsrp.append(rsrp)
            d3Rsrq.append(rsrq)
            d3Speed.append(round(float(row['IPERFmbs']), 2))
            d3Band.append(int(row['MERAKIband']))
        elif int(row['MERAKIrsrp']) < -83 or int(row['MERAKIrsrq']) < -7:
            rsrp = int(row['MERAKIrsrp'])
            rsrq = int(row['MERAKIrsrq'])
            Score = (rsrpWeight * ((rsrp - minRsrp) / (maxRsrp - minRsrp))) * (rsrqWeight * ((rsrq - minRsrq) / (maxRsrq - minRsrq)))
            Score = round(Score, 2)
            d4.append(Score)
            d4Rsrp.append(rsrp)
            d4Rsrq.append(rsrq)
            d4Speed.append(round(float(row['IPERFmbs']), 2))
            d4Band.append(int(row['MERAKIband']))
        else:
            rsrp = int(row['MERAKIrsrp'])
            rsrq = int(row['MERAKIrsrq'])
            Score = (rsrpWeight * ((rsrp - minRsrp) / (maxRsrp - minRsrp))) * (rsrqWeight * ((rsrq - minRsrq) / (maxRsrq - minRsrq)))
            Score = round(Score, 2)
            d5.append(Score)
            d5Rsrp.append(rsrp)
            d5Rsrq.append(rsrq)
            d5Speed.append(round(float(row['IPERFmbs']), 2))
            d5Band.append(int(row['MERAKIband']))

mind1 = min(d1)
maxd1 = max(d1)
mind1Index = d1.index(mind1)
maxd1Index = d1.index(maxd1)

mind2 = min(d2)
maxd2 = max(d2)
mind2Index = d2.index(mind2)
maxd2Index = d2.index(maxd2)

mind3 = min(d3)
maxd3 = max(d3)
mind3Index = d3.index(mind3)
maxd3Index = d3.index(maxd3)

mind4 = min(d4)
maxd4 = max(d4)
mind4Index = d4.index(mind4)
maxd4Index = d4.index(maxd4)

mind5 = min(d5)
maxd5 = max(d5)
mind5Index = d5.index(mind5)
maxd5Index = d5.index(maxd5)

print(f"1 Bar:\n"
      f"    Min: {mind1} Rsrp: {d1Rsrp[mind1Index]} Rsrq: {d1Rsrq[mind1Index]} Speed: {d1Speed[mind1Index]} Band: {d1Band[mind1Index]}\n"
      f"    Max: {maxd1} Rsrp: {d1Rsrp[maxd1Index]} Rsrq: {d1Rsrq[maxd1Index]} Speed: {d1Speed[maxd1Index]} Band: {d1Band[maxd1Index]}\n"
      f"2 Bar:\n"
      f"    Min: {min(d2)} Rsrp: {d2Rsrp[mind2Index]} Rsrq: {d2Rsrq[mind2Index]} Speed: {d2Speed[mind2Index]} Band: {d2Band[mind2Index]}\n"
      f"    Max: {max(d2)} Rsrp: {d2Rsrp[maxd2Index]} Rsrq: {d2Rsrq[maxd2Index]} Speed: {d2Speed[maxd2Index]} Band: {d2Band[maxd2Index]}\n\n"
      f"3 Bar:\n"
      f"    Min: {min(d3)} Rsrp: {d3Rsrp[mind3Index]} Rsrq: {d3Rsrq[mind3Index]} Speed: {d3Speed[mind3Index]} Band: {d3Band[mind3Index]}\n"
      f"    Max: {max(d3)} Rsrp: {d3Rsrp[maxd3Index]} Rsrq: {d3Rsrq[maxd3Index]} Speed: {d3Speed[maxd3Index]} Band: {d3Band[maxd3Index]}\n\n"
      f"4 Bar:\n"
      f"    Min: {min(d4)} Rsrp: {d4Rsrp[mind4Index]} Rsrq: {d4Rsrq[mind4Index]} Speed: {d4Speed[mind4Index]} Band: {d4Band[mind4Index]}\n"
      f"    Max: {max(d4)} Rsrp: {d4Rsrp[maxd4Index]} Rsrq: {d4Rsrq[maxd4Index]} Speed: {d4Speed[maxd4Index]} Band: {d4Band[maxd4Index]}\n\n"
      f"5 Bar:\n"
      f"    Min: {min(d5)} Rsrp: {d5Rsrp[mind5Index]} Rsrq: {d5Rsrq[mind5Index]} Speed: {d5Speed[mind5Index]} Band: {d5Band[mind5Index]}\n"
      f"    Max: {max(d5)} Rsrp: {d5Rsrp[maxd5Index]} Rsrq: {d5Rsrq[maxd5Index]} Speed: {d5Speed[maxd5Index]} Band: {d5Band[maxd5Index]}\n\n"
      f"")
