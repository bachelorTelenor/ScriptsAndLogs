import requests
from requests.auth import HTTPBasicAuth
from elasticsearch import Elasticsearch, helpers
import csv


ELASTIC_PASSWORD = "demodemo"
dataCSV = "Logs/KombinertLogg.csv"
dataCSVmobil = "Logs/KombinertLoggMobil.csv"

# Create the client instance
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="./certs/ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

testscenario_idex = {
    "properties": {
        "GMONARFCN": {
        "type": "long"
        },
        "GMONBAND": {
        "type": "keyword"
        },
        "GMONBANDWIDTH": {
        "type": "long"
        },
        "GMONBANDWIDTHS": {
        "type": "keyword"
        },
        "GMONBANDint": {
        "type": "long"
        },
        "GMONCA": {
        "type": "long"
        },
        "GMONCLF_DESC": {
        "type": "text"
        },
        "GMONCLF_LABEL": {
        "type": "keyword"
        },
        "GMONCLF_LOC": {
        "type": "keyword"
        },
        "GMONCQI": {
        "type": "long"
        },
        "GMONDATE": {
        "type": "keyword"
        },
        "GMONDL": {
        "type": "long"
        },
        "GMONGPS_ACCURACY": {
        "type": "long"
        },
        "GMONLAC/TAC": {
        "type": "long"
        },
        "GMONLAT": {
        "type": "double"
        },
        "GMONLOCAL_CID": {
        "type": "long"
        },
        "GMONLON": {
        "type": "double"
        },
        "GMONLocation": {
        "type": "geo_point"
        },
        "GMONNR_STATE": {
        "type": "keyword"
        },
        "GMONPCI/PSC/BSIC": {
        "type": "long"
        },
        "GMONPLMN": {
        "type": "long"
        },
        "GMONROAMING": {
        "type": "keyword"
        },
        "GMONRSRP": {
        "type": "long"
        },
        "GMONRSRQ": {
        "type": "long"
        },
        "GMONRSSI": {
        "type": "long"
        },
        "GMONRsrpPos": {
        "type": "long"
        },
        "GMONRsrqPos": {
        "type": "long"
        },
        "GMONSNR": {
        "type": "double"
        },
        "GMONSPEED": {
        "type": "long"
        },
        "GMONSYSTEM": {
        "type": "long"
        },
        "GMONTA": {
        "type": "long"
        },
        "GMONTIME": {
        "type": "keyword"
        },
        "GMONUL": {
        "type": "long"
        },
        "GMONXCI": {
        "type": "long"
        },
        "GMONtimestamp": {
        "type": "date",
        "format": "iso8601"
        },
        "GMONxNBID": {
        "type": "long"
        },
        "GPSLocation": {
        "type": "geo_point"
        },
        "GPSaccuracy": {
        "type": "double"
        },
        "GPSbattery": {
        "type": "long"
        },
        "GPSbattery_charging": {
        "type": "keyword"
        },
        "GPSbearing": {
        "type": "double"
        },
        "GPSdistance": {
        "type": "double"
        },
        "GPSelevation": {
        "type": "double"
        },
        "GPSgeoidheight": {
        "type": "long"
        },
        "GPShdop": {
        "type": "double"
        },
        "GPSlat": {
        "type": "double"
        },
        "GPSlon": {
        "type": "double"
        },
        "GPSpdop": {
        "type": "double"
        },
        "GPSprofile_name": {
        "type": "keyword"
        },
        "GPSprovider": {
        "type": "keyword"
        },
        "GPSsatellites": {
        "type": "long"
        },
        "GPSspeed": {
        "type": "double"
        },
        "GPSstarttimestamp_ms": {
        "type": "date",
        "format": "epoch_millis"
        },
        "GPStime": {
        "type": "date",
        "format": "iso8601"
        },
        "GPStime_offset": {
        "type": "date",
        "format": "iso8601"
        },
        "GPStimestamp_ms": {
        "type": "date",
        "format": "epoch_millis"
        },
        "GPSvdop": {
        "type": "double"
        },
        "IPERFmbs": {
        "type": "double"
        },
        "IPERFtimestamp": {
        "type": "date",
        "format": "iso8601"
        },
        "MERAKIAPIquery": {
        "type": "date",
        "format": "iso8601"
        },
        "MERAKIAPIupdate": {
        "type": "date",
        "format": "iso8601"
        },
        "MERAKIband": {
        "type": "long"
        },
        "MERAKIrsrp": {
        "type": "long"
        },
        "MERAKIrsrpPos": {
        "type": "long"
        },
        "MERAKIrsrq": {
        "type": "long"
        },
        "MERAKIrsrqPos": {
        "type": "long"
        },
        "TestDirection": {
        "type": "keyword"
        }
    }
}

client.indices.create(index='alltests', mappings=testscenario_idex)

testscenario_idex = {
    "properties": {
        "GMONARFCN": {
        "type": "long"
        },
        "GMONBAND": {
        "type": "keyword"
        },
        "GMONBANDWIDTH": {
        "type": "long"
        },
        "GMONBANDWIDTHS": {
        "type": "keyword"
        },
        "GMONBANDint": {
        "type": "long"
        },
        "GMONCA": {
        "type": "long"
        },
        "GMONCLF_DESC": {
        "type": "text"
        },
        "GMONCLF_LABEL": {
        "type": "keyword"
        },
        "GMONCLF_LOC": {
        "type": "keyword"
        },
        "GMONCQI": {
        "type": "long"
        },
        "GMONDATE": {
        "type": "keyword"
        },
        "GMONDL": {
        "type": "long"
        },
        "GMONGPS_ACCURACY": {
        "type": "long"
        },
        "GMONLAC/TAC": {
        "type": "long"
        },
        "GMONLAT": {
        "type": "double"
        },
        "GMONLOCAL_CID": {
        "type": "long"
        },
        "GMONLON": {
        "type": "double"
        },
        "GMONLocation": {
        "type": "geo_point"
        },
        "GMONNR_STATE": {
        "type": "keyword"
        },
        "GMONPCI/PSC/BSIC": {
        "type": "long"
        },
        "GMONPLMN": {
        "type": "long"
        },
        "GMONROAMING": {
        "type": "keyword"
        },
        "GMONRSRP": {
        "type": "long"
        },
        "GMONRSRQ": {
        "type": "long"
        },
        "GMONRSSI": {
        "type": "long"
        },
        "GMONRsrpPos": {
        "type": "long"
        },
        "GMONRsrqPos": {
        "type": "long"
        },
        "GMONSNR": {
        "type": "double"
        },
        "GMONSPEED": {
        "type": "long"
        },
        "GMONSYSTEM": {
        "type": "long"
        },
        "GMONTA": {
        "type": "long"
        },
        "GMONTIME": {
        "type": "keyword"
        },
        "GMONUL": {
        "type": "long"
        },
        "GMONXCI": {
        "type": "long"
        },
        "GMONtimestamp": {
        "type": "date",
        "format": "iso8601"
        },
        "GMONxNBID": {
        "type": "long"
        },
        "GPSLocation": {
        "type": "geo_point"
        },
        "GPSaccuracy": {
        "type": "double"
        },
        "GPSbattery": {
        "type": "long"
        },
        "GPSbattery_charging": {
        "type": "keyword"
        },
        "GPSbearing": {
        "type": "double"
        },
        "GPSdistance": {
        "type": "double"
        },
        "GPSelevation": {
        "type": "double"
        },
        "GPSgeoidheight": {
        "type": "long"
        },
        "GPShdop": {
        "type": "double"
        },
        "GPSlat": {
        "type": "double"
        },
        "GPSlon": {
        "type": "double"
        },
        "GPSpdop": {
        "type": "double"
        },
        "GPSprofile_name": {
        "type": "keyword"
        },
        "GPSprovider": {
        "type": "keyword"
        },
        "GPSsatellites": {
        "type": "long"
        },
        "GPSspeed": {
        "type": "double"
        },
        "GPSstarttimestamp_ms": {
        "type": "date",
        "format": "epoch_millis"
        },
        "GPStime": {
        "type": "date",
        "format": "iso8601"
        },
        "GPStime_offset": {
        "type": "date",
        "format": "iso8601"
        },
        "GPStimestamp_ms": {
        "type": "date",
        "format": "epoch_millis"
        },
        "GPSvdop": {
        "type": "double"
        },
        "TestDirection": {
        "type": "keyword"
        }
    }
}

client.indices.create(index='alltestsmobil', mappings=testscenario_idex)

with open(dataCSV, 'r') as data_csv:
    reader = csv.DictReader(data_csv, delimiter=';')
    helpers.bulk(client, reader, index='alltests')

with open(dataCSVmobil, 'r') as data_csv2:
    reader2 = csv.DictReader(data_csv2, delimiter=';')
    helpers.bulk(client, reader2, index='alltestsmobil')

url = 'http://localhost:5601/api/saved_objects/_import?createNewCopies=true'
myheader = {"kbn-xsrf": "true"}
myfiles = {'file': open('export.ndjson', 'rb')}
basic = HTTPBasicAuth('elastic', 'demodemo')

x = requests.post(url, headers=myheader, files=myfiles, auth=basic)

print(x.text)
