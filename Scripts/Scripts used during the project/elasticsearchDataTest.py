import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch, helpers
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


dataCSV = "Logs/KombinertLoggTest.csv"

with open(dataCSV, 'r') as data_csv:
    reader = csv.DictReader(data_csv, delimiter=';')
    helpers.bulk(client, reader, index='timezonetest')

