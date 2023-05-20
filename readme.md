# Scripts and Logs from the project
https://github.com/bachelorTelenor/ScriptsAndLogs

This repo contains Scripts and Logs from the project. This file will give a short description of the different files and directories in this repo.

## Logs
The Logs directory contains all the logs with data collected during the test. The file ```MerakiCombinedLogAllTest.csv``` contains all from the MG21 combined with data from smartphone from all tests. The file ```PhoneCombinedLogAllTests.csv``` contains all the data collected from the smartphone over all tests. This file do not contain data from the MG21, but it has a much greater number data points. 

The directory ```Final logs from test``` contains all the individual logs from all the tools used during testing. They have a directory for each individual test. The directory ```Logs from testing setup``` is some early logs from testing the setup used for the tests. The data from these logs was only used to test and imporve the test setup and is not used in the project as most of them are missing data or has some problems. 

## Scripts
The Scripts directory contains scripts used during the project. Note that most of these is not finished products and was just used as tools during the project. The main script to note here is ```mainTestScript.py``` and ```mainCombineScript.py```. ```mainTestScript.py``` is the script used during testing to collect data from the Meraki API. ```mainTestScript.py``` is a script used to combine logs from the tests. Note that only the part that combines the MG21 logs with the other logs is finished in this script and the part that is supposed to combine only the logs from the smartphone is not implemented here. ```requirements.txt``` contains all the Python libraries used for the scripts with versions. ```.env``` is a file used with some of the scripts to set the password for Elasticsearch and API Key for Meraki. 

The drirectory ```Script used during the project``` contain a collection of script used as tools during the project to process and work with data. They were changed and used as needed and most of them was for a very spesific problem and several of them was just to test somthings. ```Superparameter Test Scripts``` contains some simple scripts to test superparameter propositions with the data collected from the tests. Finaly the ```Data Visualization Scrips``` contains scripts used to visualize data from the tests for the report. 

## Thingy91
The Thingy91 directorry contains some configuration and setup for the Thingy 91 that was going to be used for the project. As decided agains using this device, the content in dircectory is mostly unfinished.