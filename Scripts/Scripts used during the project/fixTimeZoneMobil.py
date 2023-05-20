from datetime import datetime as dt
import datetime
import csv

kombinertLog = "./logs/KombinertLoggMobil.csv"
combinedCSV = "./logs/KombinertLogMobilTZ.csv"

f = open(combinedCSV, 'w', newline='')
writer = csv.writer(f, delimiter=';')
csvHeader = ['TestDirection', 'GMONPLMN', 'GMONSYSTEM', 'GMONXCI', 'GMONxNBID',
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

with open(kombinertLog, 'r') as kombinertLog_csv:
    kombinertData = csv.reader(kombinertLog_csv, delimiter=';')
    next(kombinertData)
    for l in kombinertData:
        TestDirection = l[0]
        GMONPLMN = l[1]
        GMONSYSTEM = l[2]
        GMONXCI = l[3]
        GMONxNBID = l[4]
        GMONLOCAL_CID = l[5]
        GMONLACTAC = l[6]
        GMONPCIPSCBSIC = l[7]
        GMONARFCN = l[8]
        GMONBAND = l[9]
        GMONBANDint = l[10]
        GMONRSSI = l[11]
        GMONRSRP = l[12]
        GMONRsrpPos = l[13]
        GMONRSRQ = l[14]
        GMONRsrqPos = l[15]
        GMONSNR = l[16]
        GMONCQI = l[17]
        GMONTA = l[18]
        GMONDISTANCE = l[19]
        GMONDELTA_AZI = l[20]
        GMONLAT = l[21]
        GMONLON = l[22]
        GMONLocation = l[23]
        GMONSPEED = l[24]
        GMONGPS_ACCURACY = l[25]
        GMONUL = l[26]
        GMONDL = l[27]
        GMONBANDWIDTH = l[28]
        GMONBANDWIDTHS = l[29]
        GMONCA = l[30]
        GMONNR_STATE = l[31]
        GMONNARFCN = l[32]
        GMONNR_BAND = l[33]
        GMONNR_PCI = l[34]
        GMONNR_SS_RSRP = l[35]
        GMONNR_SS_RSRQ = l[36]
        GMONNR_SS_SINR = l[37]
        GMONNR_CSI_RSRP = l[38]
        GMONNR_CSI_RSRQ = l[39]
        GMONNR_CSI_SINR = l[40]
        GMONCLF_LABEL = l[41]
        GMONCLF_LOC = l[42]
        GMONCLF_DESC = l[43]
        GMONDATE = l[44]
        GMONTIME = l[45]
        GMONtimestamp = dt.strptime(l[46], '%Y-%m-%dT%H:%M:%SZ')
        GMONtimestamp = GMONtimestamp.strftime('%Y-%m-%dT%H:%M:%S+01')
        GMONROAMING = l[47]
        GPStime = dt.strptime(l[48], '%Y-%m-%dT%H:%M:%S.%fZ')
        GPStime = GPStime.strftime('%Y-%m-%dT%H:%M:%S+01')
        GPSlat = l[49]
        GPSlon = l[50]
        GPSLocation = l[51]
        GPSelevation = l[52]
        GPSaccuracy = l[53]
        GPSbearing = l[54]
        GPSspeed = l[55]
        GPSsatellites = l[56]
        GPSprovider = l[57]
        GPShdop = l[58]
        GPSvdop = l[59]
        GPSpdop = l[60]
        GPSgeoidheight = l[61]
        GPSageofdgpsdata = l[62]
        GPSdgpsid = l[63]
        GPSactivity = l[64]
        GPSbattery = l[65]
        GPSannotation = l[66]
        GPStimestamp_ms = l[67]
        GPStime_offset = l[68]
        GPSdistance = l[69]
        GPSstarttimestamp_ms = l[70]
        GPSprofile_name = l[71]
        GPSbattery_charging = l[72]

        csvRow = [TestDirection, GMONPLMN, GMONSYSTEM, GMONXCI, GMONxNBID, GMONLOCAL_CID, GMONLACTAC, GMONPCIPSCBSIC,
                  GMONARFCN, GMONBAND, GMONBANDint, GMONRSSI, GMONRSRP, GMONRsrpPos, GMONRSRQ, GMONRsrqPos, GMONSNR,
                  GMONCQI, GMONTA, GMONDISTANCE, GMONDELTA_AZI, GMONLAT, GMONLON, GMONLocation, GMONSPEED,
                  GMONGPS_ACCURACY, GMONUL, GMONDL, GMONBANDWIDTH, GMONBANDWIDTHS, GMONCA, GMONNR_STATE, GMONNARFCN,
                  GMONNR_BAND, GMONNR_PCI, GMONNR_SS_RSRP, GMONNR_SS_RSRQ, GMONNR_SS_SINR, GMONNR_CSI_RSRP,
                  GMONNR_CSI_RSRQ, GMONNR_CSI_SINR, GMONCLF_LABEL, GMONCLF_LOC, GMONCLF_DESC, GMONDATE, GMONTIME,
                  GMONtimestamp, GMONROAMING, GPStime, GPSlat, GPSlon, GPSLocation, GPSelevation, GPSaccuracy,
                  GPSbearing, GPSspeed, GPSsatellites, GPSprovider, GPShdop, GPSvdop, GPSpdop, GPSgeoidheight,
                  GPSageofdgpsdata, GPSdgpsid, GPSactivity, GPSbattery, GPSannotation, GPStimestamp_ms, GPStime_offset,
                  GPSdistance, GPSstarttimestamp_ms, GPSprofile_name, GPSbattery_charging]
        f = open(combinedCSV, 'a', newline='')
        writer = csv.writer(f, delimiter=';')
        writer.writerow(csvRow)
        f.close()
