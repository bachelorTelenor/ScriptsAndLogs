$csvPath = "C:\Users\Vebjorn111\Desktop\Batcheloroppgave\BacheloroppgaveGit\TestLogger\2023.02.15-PilotTest\Kombinerte\Test2Kombinert.csv"
$outputPath = "C:\Users\Vebjorn111\Desktop\Batcheloroppgave\BacheloroppgaveGit\TestLogger\2023.02.15-PilotTest\Kombinerte\Test2KombinertLokasjon.csv"

Add-Content $outputPath "APIQuery;APIUpdate;rsrp;rsrq;Time;Latitude;Longitude;Altitude;time;lat;lon;elevation;accuracy;bearing;speed;satellites;provider;hdop;vdop;pdop;geoidheight;ageofdgpsdata;dgpsid;activity;battery;annotation;timestamp_ms;time_offset;distance;starttimestamp_ms;profile_name;battery_charging;ThingyLokasjon;MobilLokasjon"

Import-Csv $csvPath | ForEach-Object {
    $thingyGPS = "$($_.Latitude),$($_.Longitude)"
    $mobilGPS = "$($_.lat),$($_.lon)"
    Add-Content $outputPath "$($_.APIQuery);$($_.APIUpdate);$($_.rsrp);$($_.rsrq);$($_.Time1);$($_.Latitude);$($_.Longitude);$($_.Altitude);$($_.time);$($_.lat);$($_.lon);$($_.elavation);$($_.accuracy);$($_.bearing);$($_.speed);$($_.stellites);$($_.provider);$($_.hdop);$($_.vdop);$($_.pdop);$($_.geoheight);$($_.ageofgpsdata);$($_.gpsid);$($_.activity);$($_.battery);$($_.annontation);$($_.timestamp_ms);$($_.time_offset);$($_.distance);$($_.starttimestamp_ms);$($_.profile_name);$($_.battery_charging);$($thingyGPS);$($mobilGPS)"
}

