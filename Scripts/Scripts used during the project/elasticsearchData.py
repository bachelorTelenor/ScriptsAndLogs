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


dataCSV = "Logs/KombinertLogg.csv"
dataCSVmobil = "Logs/KombinertLoggMobil.csv"

with open(dataCSV, 'r') as data_csv:
    elasticData = csv.reader(data_csv, delimiter=';')
    next(elasticData)
    for row in elasticData:
        client.index(
            index='alltests',
            document={
                "MERAKIAPIquery": row[0],
                "MERAKIAPIupdate": row[1],
                "MERAKIrsrp": row[2],
                "MERAKIrsrpPos": row[3],
                "MERAKIrsrq": row[4],
                "MERAKIrsrqPos": row[5],
                "MERAKIband": row[6],
                "TestDirection": row[7],
                "IPERFtimestamp": row[8],
                "IPERFmbs": row[9],
                "GMONPLMN": row[10],
                "GMONSYSTEM": row[11],
                "GMONXCI": row[12],
                "GMONxNBID": row[13],
                "GMONLOCAL_CID": row[14],
                "GMONLAC/TAC": row[15],
                "GMONPCI/PSC/BSIC": row[16],
                "GMONARFCN": row[17],
                "GMONBAND": row[18],
                "GMONBANDint": row[19],
                "GMONRSSI": row[20],
                "GMONRSRP": row[21],
                "GMONRsrpPos": row[22],
                "GMONRSRQ": row[23],
                "GMONRsrqPos": row[24],
                "GMONSNR": row[25],
                "GMONCQI": row[26],
                "GMONTA": row[27],
                "GMONLAT": row[30],
                "GMONLON": row[31],
                "GMONLocation": row[32],
                "GMONSPEED": row[33],
                "GMONGPS_ACCURACY": row[34],
                "GMONUL": row[35],
                "GMONDL": row[36],
                "GMONBANDWIDTH": row[37],
                "GMONBANDWIDTHS": row[38],
                "GMONCA": row[39],
                "GMONNR_STATE": row[40],
                "GMONCLF_LABEL": row[50],
                "GMONCLF_LOC": row[51],
                "GMONCLF_DESC": row[52],
                "GMONDATE": row[53],
                "GMONTIME": row[54],
                "GMONtimestamp": row[55],
                "GMONROAMING": row[56],
                "GPStime": row[57],
                "GPSlat": row[58],
                "GPSlon": row[59],
                "GPSLocation": row[60],
                "GPSelevation": row[61],
                "GPSaccuracy": row[62],
                "GPSbearing": row[63],
                "GPSspeed": row[64],
                "GPSsatellites": row[65],
                "GPSprovider": row[66],
                "GPShdop": row[67],
                "GPSvdop": row[68],
                "GPSpdop": row[69],
                "GPSgeoidheight": row[70],
                "GPSbattery": row[74],
                "GPStimestamp_ms": row[76],
                "GPStime_offset": row[77],
                "GPSdistance": row[78],
                "GPSstarttimestamp_ms": row[79],
                "GPSprofile_name": row[80],
                "GPSbattery_charging": row[81]
            })

