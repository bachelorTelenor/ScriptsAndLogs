

minRsrp = -140
maxRsrp = -80

minRsrq = -17
maxRsrq = -7

rsrp = -97
rsrq = -10

rsrpWeight = 1
rsrqWeight = 1

# Bare rsrp og rsrq
Score = ((rsrp - minRsrp) / (maxRsrp - minRsrp)) * ((rsrq - minRsrq) / (maxRsrq - minRsrq))
# Legge på weight for å vurdere verdiene forskjellig
Score2 = (rsrpWeight * ((rsrp - minRsrp) / (maxRsrp - minRsrp))) * (rsrpWeight * ((rsrq - minRsrq) / (maxRsrq - minRsrq)))
# Kan legge til andre variabler som download speed også
# Kan justere med forskjellig weight på de forskjellige verdiene
print(Score)
print(Score2)
