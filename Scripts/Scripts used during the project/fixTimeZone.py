from datetime import datetime as dt
import datetime
import csv

kombinertLog = "./logs/KombinertLogg.csv"
combinedCSV = "./logs/KombinertLogTZ.csv"

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

with open(kombinertLog, 'r') as kombinertLog_csv:
    kombinertData = csv.reader(kombinertLog_csv, delimiter=';')
    next(kombinertData)
    for l in kombinertData:
        MERAKIAPIquery = dt.strptime(l[0], '%Y-%m-%dT%H:%M:%SZ')
        MERAKIAPIquery = MERAKIAPIquery.strftime('%Y-%m-%dT%H:%M:%S+01')
        MERAKIAPIupdate = dt.strptime(l[1], '%Y-%m-%dT%H:%M:%SZ')
        MERAKIAPIupdate = MERAKIAPIupdate.strftime('%Y-%m-%dT%H:%M:%S+01')
        MERAKIrsrp = l[2]
        MERAKIrsrpPos = l[3]
        MERAKIrsrq = l[4]
        MERAKIrsrqPos = l[5]
        MERAKIband = l[6]
        TestDirection = l[7]
        IPERFtimestamp = dt.strptime(l[8], '%Y-%m-%dT%H:%M:%SZ')
        IPERFtimestamp = IPERFtimestamp.strftime('%Y-%m-%dT%H:%M:%S+01')
        IPERFmbs = l[9]
        GMONPLMN = l[10]
        GMONSYSTEM = l[11]
        GMONXCI = l[12]
        GMONxNBID = l[13]
        GMONLOCAL_CID = l[14]
        GMONLACTAC = l[15]
        GMONPCIPSCBSIC = l[16]
        GMONARFCN = l[17]
        GMONBAND = l[18]
        GMONBANDint = l[19]
        GMONRSSI = l[20]
        GMONRSRP = l[21]
        GMONRsrpPos = l[22]
        GMONRSRQ = l[23]
        GMONRsrqPos = l[24]
        GMONSNR = l[25]
        GMONCQI = l[26]
        GMONTA = l[27]
        GMONDISTANCE = l[28]
        GMONDELTA_AZI = l[29]
        GMONLAT = l[30]
        GMONLON = l[31]
        GMONLocation = l[32]
        GMONSPEED = l[33]
        GMONGPS_ACCURACY = l[34]
        GMONUL = l[35]
        GMONDL = l[36]
        GMONBANDWIDTH = l[37]
        GMONBANDWIDTHS = l[38]
        GMONCA = l[39]
        GMONNR_STATE = l[40]
        GMONNARFCN = l[41]
        GMONNR_BAND = l[42]
        GMONNR_PCI = l[43]
        GMONNR_SS_RSRP = l[44]
        GMONNR_SS_RSRQ = l[45]
        GMONNR_SS_SINR = l[46]
        GMONNR_CSI_RSRP = l[47]
        GMONNR_CSI_RSRQ = l[48]
        GMONNR_CSI_SINR = l[49]
        GMONCLF_LABEL = l[50]
        GMONCLF_LOC = l[51]
        GMONCLF_DESC = l[52]
        GMONDATE = l[53]
        GMONTIME = l[54]
        GMONtimestamp = dt.strptime(l[55], '%Y-%m-%dT%H:%M:%SZ')
        GMONtimestamp = GMONtimestamp.strftime('%Y-%m-%dT%H:%M:%S+01')
        GMONROAMING = l[56]
        GPStime = dt.strptime(l[57], '%Y-%m-%dT%H:%M:%S.%fZ')
        GPStime = GPStime.strftime('%Y-%m-%dT%H:%M:%S+01')
        GPSlat = l[58]
        GPSlon = l[59]
        GPSLocation = l[60]
        GPSelevation = l[61]
        GPSaccuracy = l[62]
        GPSbearing = l[63]
        GPSspeed = l[64]
        GPSsatellites = l[65]
        GPSprovider = l[66]
        GPShdop = l[67]
        GPSvdop = l[68]
        GPSpdop = l[69]
        GPSgeoidheight = l[70]
        GPSageofdgpsdatav = l[71]
        GPSdgpsid = l[72]
        GPSactivity = l[73]
        GPSbattery = l[74]
        GPSannotation = l[75]
        GPStimestamp_ms = l[76]
        GPStime_offset = l[77]
        GPSdistance = l[78]
        GPSstarttimestamp_ms = l[79]
        GPSprofile_name = l[80]
        GPSbattery_charging = l[81]

        csvRow = [MERAKIAPIquery, MERAKIAPIupdate, MERAKIrsrp, MERAKIrsrpPos, MERAKIrsrq, MERAKIrsrqPos, MERAKIband,
                  TestDirection, IPERFtimestamp, IPERFmbs, GMONPLMN, GMONSYSTEM, GMONXCI, GMONxNBID, GMONLOCAL_CID,
                  GMONLACTAC, GMONPCIPSCBSIC, GMONARFCN, GMONBAND, GMONBANDint, GMONRSSI, GMONRSRP, GMONRsrpPos,
                  GMONRSRQ, GMONRsrqPos, GMONSNR, GMONCQI, GMONTA, GMONDISTANCE, GMONDELTA_AZI, GMONLAT, GMONLON,
                  GMONLocation, GMONSPEED, GMONGPS_ACCURACY, GMONUL, GMONDL, GMONBANDWIDTH, GMONBANDWIDTHS, GMONCA,
                  GMONNR_STATE, GMONNARFCN, GMONNR_BAND, GMONNR_PCI, GMONNR_SS_RSRP, GMONNR_SS_RSRQ, GMONNR_SS_SINR,
                  GMONNR_CSI_RSRP, GMONNR_CSI_RSRQ, GMONNR_CSI_SINR, GMONCLF_LABEL, GMONCLF_LOC, GMONCLF_DESC, GMONDATE,
                  GMONTIME, GMONtimestamp, GMONROAMING, GPStime, GPSlat, GPSlon, GPSLocation, GPSelevation, GPSaccuracy,
                  GPSbearing, GPSspeed, GPSsatellites, GPSprovider, GPShdop, GPSvdop, GPSpdop, GPSgeoidheight,
                  GPSageofdgpsdatav, GPSdgpsid, GPSactivity, GPSbattery, GPSannotation, GPStimestamp_ms, GPStime_offset,
                  GPSdistance, GPSstarttimestamp_ms, GPSprofile_name, GPSbattery_charging]
        f = open(combinedCSV, 'a', newline='')
        writer = csv.writer(f, delimiter=';')
        writer.writerow(csvRow)
        f.close()
