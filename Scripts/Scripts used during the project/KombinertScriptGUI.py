import os
import customtkinter
import json
import datetime
import csv
from datetime import datetime as dt
from itertools import islice

test = os.listdir("Logs")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

merakiLog = ""
iperfJson = ""
iperfLog = "./logs/iperfLog.csv"
gmonLog = ""
gpsLog = ""

combinedCSV = "./logs/CombinedLog.csv"

iperfStart = 1
gmonStart = 1
gpsStart = 1

def createCombineCsvFile():
    f = open(combinedCSV, 'w', newline='')
    writer = csv.writer(f, delimiter=';')
    csvHeader = ['MERAKIAPIquery', 'MERAKIAPIupdate', 'MERAKIrsrp', 'MERAKIrsrpPos', 'MERAKIrsrq', 'MERAKIrsrqPos',
                 'MERAKIband', 'TestDirection', 'IPERFtimestamp', 'IPERFmbs', 'GMONPLMN', 'GMONSYSTEM', 'GMONXCI', 'GMONxNBID',
                 'GMONLOCAL_CID', 'GMONLAC/TAC', 'GMONPCI/PSC/BSIC', 'GMONARFCN', 'GMONBAND', 'GMONBANDint', 'GMONRSSI',
                 'GMONRSRP', 'GMONRsrpPos', 'GMONRSRQ', 'GMONRsrqPos', 'GMONSNR', 'GMONCQI', 'GMONTA', 'GMONDISTANCE',
                 'GMONDELTA_AZI', 'GMONLAT', 'GMONLON', 'GMONLocation', 'GMONSPEED', 'GMONGPS_ACCURACY', 'GMONUL', 'GMONDL',
                 'GMONBANDWIDTH', 'GMONBANDWIDTHS', 'GMONCA', 'GMONNR_STATE', 'GMONNARFCN', 'GMONNR_BAND', 'GMONNR_PCI',
                 'GMONNR_SS_RSRP', 'GMONNR_SS_RSRQ', 'GMONNR_SS_SINR', 'GMONNR_CSI_RSRP', 'GMONNR_CSI_RSRQ',
                 'GMONNR_CSI_SINR', 'GMONCLF_LABEL', 'GMONCLF_LOC', 'GMONCLF_DESC', 'GMONDATE', 'GMONTIME', 'GMONtimestamp',
                 'GMONROAMING', 'GPStime', 'GPSlat', 'GPSlon', 'GPSLocation', 'GPSelevation', 'GPSaccuracy', 'GPSbearing',
                 'GPSspeed', 'GPSsatellites', 'GPSprovider', 'GPShdop', 'GPSvdop', 'GPSpdop', 'GPSgeoidheight',
                 'GPSageofdgpsdata', 'GPSdgpsid', 'GPSactivity', 'GPSbattery', 'GPSannotation', 'GPStimestamp_ms',
                 'GPStime_offset', 'GPSdistance', 'GPSstarttimestamp_ms', 'GPSprofile_name', 'GPSbattery_charging']
    writer.writerow(csvHeader)
    f.close()


def matchIperf(time):
    bestMatch = datetime.timedelta(hours=99999)
    match = False
    global iperfStart
    tempStart = iperfStart
    with open(iperfLog, 'r') as iperfData_csv:
        for l in islice(csv.reader(iperfData_csv), iperfStart, None):
            iperfTime = l[0]
            iperfdatedatetime = dt.strptime(iperfTime, '%Y-%m-%dT%H-%M-%SZ')
            iperfdatedatetime = iperfdatedatetime + datetime.timedelta(hours=1)
            timeDif = abs(time - iperfdatedatetime)

            if (timeDif < datetime.timedelta(seconds=5)):
                if (timeDif <= bestMatch):
                    bestMatch = timeDif

                    iperfTimestamp = iperfdatedatetime.strftime('%Y-%m-%dT%H:%M:%S+01')
                    iperfMBs = l[1]
            elif bestMatch != datetime.timedelta(hours=99999):
                match = True
                csvRow = [iperfTimestamp, iperfMBs]
                iperfStart = tempStart
                return csvRow, match
            elif time < (iperfdatedatetime + datetime.timedelta(seconds=5)):
                return 0, match
            if not time < (iperfdatedatetime - datetime.timedelta(seconds=2)):
                tempStart += 1
    return 0, match

def matchGmon(time):
    bestMatch = datetime.timedelta(hours=99999)
    match = False
    global gmonStart
    tempStart = gmonStart
    with open(gmonLog, 'r') as gmonData_csv:
        for l in islice(csv.reader(gmonData_csv, delimiter=';'), gmonStart, None):
            gmonTime = f'{l[39]}T{l[40]}Z'
            gmontimeDatetime = dt.strptime(gmonTime, '%Y/%m/%dT%H:%M:%SZ')
            timeDif = abs(time - gmontimeDatetime)

            if (timeDif < datetime.timedelta(seconds=5)):
                if (timeDif <= bestMatch):
                    bestMatch = timeDif

                    PLMN = l[0]
                    SYSTEM = l[1]
                    XCI = l[2]
                    xNBID = l[3]
                    LOCAL_CID = l[4]
                    LACTAC = l[5]
                    PCIPSCBSIC = l[6]
                    ARFCN = l[7]
                    BAND = l[8]
                    BANDint = (BAND[0:4]).replace(' ', '')
                    RSSI = l[9]
                    RSRPRSCP = l[10]
                    RsrpPos = abs(int(l[10]))
                    RSRQECIO = l[11]
                    RsrqPos = abs(int(l[11]))
                    SNR = l[12]
                    CQI = l[13]
                    TA = l[14]
                    DISTANCE = l[15]
                    DELTA_AZI = l[16]
                    LAT = l[17]
                    LON = l[18]
                    location = f'{LAT},{LON}'
                    SPEED = l[19]
                    GPS_ACCURACY = l[20]
                    UL = l[21]
                    DL = l[22]
                    BANDWIDTH = l[23]
                    BANDWIDTHS = l[24]
                    CA = l[25]
                    NR_STATE = l[26]
                    NARFCN = l[27]
                    NR_BAND = l[28]
                    NR_PCI = l[29]
                    NR_SS_RSRP = l[30]
                    NR_SS_RSRQ = l[31]
                    NR_SS_SINR = l[32]
                    NR_CSI_RSRP = l[33]
                    NR_CSI_RSRQ = l[34]
                    NR_CSI_SINR = l[35]
                    CLF_LABEL = l[36]
                    CLF_LOC = l[37]
                    CLF_DESC = l[38]
                    DATE = l[39]
                    TIME = l[40]
                    timestamp = gmontimeDatetime.strftime('%Y-%m-%dT%H:%M:%S+01')
                    ROAMING = l[41]
            elif bestMatch != datetime.timedelta(hours=99999):
                match = True
                csvRow = [PLMN, SYSTEM, XCI, xNBID, LOCAL_CID, LACTAC, PCIPSCBSIC, ARFCN, BAND, BANDint, RSSI,
                          RSRPRSCP, RsrpPos, RSRQECIO, RsrqPos, SNR, CQI, TA, DISTANCE, DELTA_AZI, LAT, LON,
                          location, SPEED, GPS_ACCURACY, UL, DL, BANDWIDTH, BANDWIDTHS, CA, NR_STATE, NARFCN,
                          NR_BAND, NR_PCI, NR_SS_RSRP, NR_SS_RSRQ, NR_SS_SINR, NR_CSI_RSRP, NR_CSI_RSRQ,
                          NR_CSI_SINR, CLF_LABEL, CLF_LOC, CLF_DESC, DATE, TIME, timestamp, ROAMING]
                gmonStart = tempStart
                return csvRow, match
            elif time < (gmontimeDatetime + datetime.timedelta(seconds=5)):
                return 0, match
            if not time < (gmontimeDatetime - datetime.timedelta(seconds=2)):
                tempStart += 1
    return 0, match

def matchGps(time):
    bestMatch = datetime.timedelta(hours=99999)
    global gpsStart
    tempStart = gpsStart
    match = False
    with open(gpsLog, 'r') as gpsData_csv:
        for l in islice(csv.reader(gpsData_csv), gpsStart, None):
            gpsTime = l[0]
            gpstimedatetime = dt.strptime(gpsTime, '%Y-%m-%dT%H:%M:%S.%fZ')
            gpstimedatetime = gpstimedatetime + datetime.timedelta(hours=2)
            timeDif = abs(time - gpstimedatetime)

            if (timeDif < datetime.timedelta(seconds=5)):
                if (timeDif <= bestMatch):
                    bestMatch = timeDif

                    time1 = gpstimedatetime.strftime('%Y-%m-%dT%H:%M:%S+01')
                    lat = l[1]
                    lon = l[2]
                    location = f'{lat},{lon}'
                    elevation = l[3]
                    accuracy = l[4]
                    bearing = l[5]
                    speed = l[6]
                    satellites = l[7]
                    provider = l[8]
                    hdop = l[9]
                    vdop = l[10]
                    pdop = l[11]
                    geoidheight = l[12]
                    ageofdgpsdata = l[13]
                    dgpsid = l[14]
                    activity = l[15]
                    battery = l[16]
                    annotation = l[17]
                    timestamp_ms = l[18]
                    time_offset = l[19]
                    distance = l[20]
                    starttimestamp_ms = l[21]
                    profile_name = l[22]
                    battery_charging = l[23]
            elif bestMatch != datetime.timedelta(hours=99999):
                match = True
                csvRow = [time1, lat, lon, location, elevation, accuracy, bearing, speed, satellites, provider, hdop,
                          vdop, pdop, geoidheight, ageofdgpsdata, dgpsid, activity, battery, annotation,
                          timestamp_ms, time_offset, distance, starttimestamp_ms, profile_name, battery_charging]
                gpsStart = tempStart
                return csvRow, match
            elif time < (gpstimedatetime + datetime.timedelta(seconds=5)):
                return 0, match
            if not time < (gpstimedatetime - datetime.timedelta(seconds=2)):
                tempStart += 1
    return 0, match

def JsonToCsv():
    jsonfile = iperfJson
    csvpath = iperfLog

    f = open(csvpath, 'w', newline='')
    writer = csv.writer(f)
    csvHeader = ['Timestamp', 'Mb/s']
    writer.writerow(csvHeader)
    f.close()

    with open(jsonfile) as data_file:
        data = json.load(data_file)
        starttime = data['start']['timestamp']['timesecs']
        timestamp = datetime.datetime.fromtimestamp(starttime)
        timestamp = timestamp - datetime.timedelta(hours=1)
        orginialStart = timestamp
        for l in data["intervals"]:
            timestampPrint = timestamp.strftime("%Y-%m-%dT%H-%M-%SZ")
            Mbs = str(round((l['sum']['bits_per_second'] / 1024 / 1024), 2))
            csvRow = [timestampPrint, Mbs]
            f = open(csvpath, 'a', newline='')
            writer = csv.writer(f)
            writer.writerow(csvRow)
            f.close()
            timedelta = l['sum']['start']
            timestamp = orginialStart + datetime.timedelta(0, timedelta)


def combineLogs():
    JsonToCsv()
    createCombineCsvFile()
    with open(merakiLog, 'r') as merakiData_csv:
        merakiData = csv.reader(merakiData_csv)
        next(merakiData)
        for row in merakiData:
            merakiTime = row[1]
            merakiTime = dt.strptime(merakiTime, '%Y-%m-%dT%H:%M:%SZ')
            merakiTimeCSV = merakiTime.strftime('%Y-%m-%dT%H:%M:%S+01')
            merakiTime2 = row[0]
            merakiTime2 = dt.strptime(merakiTime2, '%Y-%m-%dT%H:%M:%SZ')
            merakiTimeCSV2 = merakiTime2.strftime('%Y-%m-%dT%H:%M:%S+01')
            merakiCSVrow = [merakiTimeCSV2, merakiTimeCSV, row[2], abs(int(row[2])), row[3], abs(int(row[3])), row[4], row[5]]
            iperfCSVrow = matchIperf(merakiTime)
            gmonCSVrow = matchGmon(merakiTime)
            gpsCSVrow = matchGps(merakiTime)
            # print(f"Iperf = {iperfCSVrow[1]}, gmon = {gmonCSVrow[1]}, gps = {gpsCSVrow[1]}, time = {merakiTime}")
            if iperfCSVrow[1] and gmonCSVrow[1] and gpsCSVrow[1]:
                merakiCSVrow.extend(iperfCSVrow[0])
                merakiCSVrow.extend(gmonCSVrow[0])
                merakiCSVrow.extend(gpsCSVrow[0])
                f = open(combinedCSV, 'a', newline='')
                writer = csv.writer(f, delimiter=';')
                writer.writerow(merakiCSVrow)
                f.close()

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Meraki")
        self.add("Mobil")

        # --------- Meraki Tab ------------
        # Meraki log select
        self.lableMeraki = customtkinter.CTkLabel(master=self.tab("Meraki"), text="Meraki Log")
        self.lableMeraki.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.comboboxMeraki = customtkinter.CTkComboBox(master=self.tab("Meraki"), values=test)
        self.comboboxMeraki.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Iperf log select
        self.lableIperf = customtkinter.CTkLabel(master=self.tab("Meraki"), text="Iperf Log (JSON)")
        self.lableIperf.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.comboboxIperf = customtkinter.CTkComboBox(master=self.tab("Meraki"), values=test)
        self.comboboxIperf.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # GPSLogger log select
        self.lableGPSLogger = customtkinter.CTkLabel(master=self.tab("Meraki"), text="GPSLogger Log")
        self.lableGPSLogger.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.comboboxGPSLogger = customtkinter.CTkComboBox(master=self.tab("Meraki"), values=test)
        self.comboboxGPSLogger.grid(row=2, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Gmon log select
        self.lableGmon = customtkinter.CTkLabel(master=self.tab("Meraki"), text="Gmon Log")
        self.lableGmon.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.comboboxGmon = customtkinter.CTkComboBox(master=self.tab("Meraki"), values=test)
        self.comboboxGmon.grid(row=3, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        self.button = customtkinter.CTkButton(master=self.tab("Meraki"), command=self.button_callback, text="Combine")
        self.button.grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky="ew")


        # --------- Mobil Tab ------------
        # GPSLogger log select
        self.lableGPSLogger2 = customtkinter.CTkLabel(master=self.tab("Mobil"), text="GPSLogger Log")
        self.lableGPSLogger2.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.comboboxGPSLogger2 = customtkinter.CTkComboBox(master=self.tab("Mobil"), values=test)
        self.comboboxGPSLogger2.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Gmon log select
        self.lableGmon2 = customtkinter.CTkLabel(master=self.tab("Mobil"), text="Gmon Log")
        self.lableGmon2.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.comboboxGmon2 = customtkinter.CTkComboBox(master=self.tab("Mobil"), values=test)
        self.comboboxGmon2.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        self.button2 = customtkinter.CTkButton(master=self.tab("Mobil"), command=self.button_callback2, text="Combine")
        self.button2.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="ew")

    # --------- Funksjoner ------------
    def button_callback(self):
        global iperfJson
        global merakiLog
        global gmonLog
        global gpsLog
        iperfJson = f"./logs/{self.comboboxIperf.get()}"
        merakiLog = f"./logs/{self.comboboxMeraki.get()}"
        gmonLog = f"./logs/{self.comboboxGmon.get()}"
        gpsLog = f"./logs/{self.comboboxGPSLogger.get()}"
        combineLogs()


    def button_callback2(self):
        test2 = f"GPS: {self.comboboxGPSLogger2.get()}\nGmon: {self.comboboxGmon2.get()}"
        print(test2)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Combine and upload logs")

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()

