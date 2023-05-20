from datetime import datetime as dt
import datetime



merakiCSV = "TestLog2023-02-24T13-52-08Z.csv"
iperfCSV = "iperf3Client_kl14_04.csv"

merakidate = "2023-02-24T14:05:57Z"
iperfdate = "2023-02-24T14-05-59Z"

merakidatedatetime = dt.strptime(merakidate, '%Y-%m-%dT%H:%M:%SZ')
iperfdatedatetime = dt.strptime(iperfdate, '%Y-%m-%dT%H-%M-%SZ')

print(abs(merakidatedatetime - iperfdatedatetime))

fdate = datetime.date(1999, 9, 9)
sdate = datetime.date(2022, 12, 25)
print(abs(fdate - sdate))


'''
hent inn csv med merakidata
For hver linje i meraki, ta date og gjør til date time
Loop igjennom iperfdata og finn nermeste datetime der
Skriv en linje med kobinert data til csv 
Vurder å legge til en maksimum tidsforskjell for å tilate data
'''