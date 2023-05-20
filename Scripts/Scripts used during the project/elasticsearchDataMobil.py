import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import csv

# Laster inn .env filen
load_dotenv()

ElasticSearchPass = os.getenv('ELASTIC_PASSWORD')
ElasticSearchIP = os.getenv('IP_ADDRESS')

client = Elasticsearch(
    ElasticSearchIP,
    ca_certs="./http_ca.crt",
    basic_auth=("elastic", ElasticSearchPass)
)


dataCSV = "Logs/KombinertLoggMobil.csv"

with open(dataCSV, 'r') as data_csv:
    elasticData = csv.reader(data_csv, delimiter=';')
    next(elasticData)
    for row in elasticData:
        client.index(
            index='alltestsmobil',
            document={
                "TestDirection": row[0],
                "GMONPLMN": row[1],
                "GMONSYSTEM": row[2],
                "GMONXCI": row[3],
                "GMONxNBID": row[4],
                "GMONLOCAL_CID": row[5],
                "GMONLAC/TAC": row[6],
                "GMONPCI/PSC/BSIC": row[7],
                "GMONARFCN": row[8],
                "GMONBAND": row[9],
                "GMONBANDint": row[10],
                "GMONRSSI": row[11],
                "GMONRSRP": row[12],
                "GMONRsrpPos": row[13],
                "GMONRSRQ": row[14],
                "GMONRsrqPos": row[15],
                "GMONSNR": row[16],
                "GMONCQI": row[17],
                "GMONTA": row[18],
                "GMONLAT": row[21],
                "GMONLON": row[22],
                "GMONLocation": row[23],
                "GMONSPEED": row[24],
                "GMONGPS_ACCURACY": row[25],
                "GMONUL": row[26],
                "GMONDL": row[27],
                "GMONBANDWIDTH": row[28],
                "GMONBANDWIDTHS": row[29],
                "GMONCA": row[30],
                "GMONNR_STATE": row[31],
                "GMONCLF_LABEL": row[41],
                "GMONCLF_LOC": row[42],
                "GMONCLF_DESC": row[43],
                "GMONDATE": row[44],
                "GMONTIME": row[45],
                "GMONtimestamp": row[46],
                "GMONROAMING": row[47],
                "GPStime": row[48],
                "GPSlat": row[49],
                "GPSlon": row[50],
                "GPSLocation": row[51],
                "GPSelevation": row[52],
                "GPSaccuracy": row[53],
                "GPSspeed": row[55],
                "GPSsatellites": row[56],
                "GPSprovider": row[57],
                "GPShdop": row[58],
                "GPSvdop": row[59],
                "GPSpdop": row[60],
                "GPSgeoidheight": row[61],
                "GPSbattery": row[65],
                "GPStimestamp_ms": row[67],
                "GPStime_offset": row[68],
                "GPSdistance": row[69],
                "GPSstarttimestamp_ms": row[70],
                "GPSprofile_name": row[71],
                "GPSbattery_charging": row[72]
            })

