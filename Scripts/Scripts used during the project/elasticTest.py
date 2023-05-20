from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "demodemo"

# Create the client instance
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="./certs/ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Successful response!
client.info()
