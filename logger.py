#%% MODULE BEGINS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module_name = '<logger>'

'''
Version: <0.1>

Description:
    <***>

Authors:
    <Adam>

Date Created     :  <04-24-2024>
Date Last Updated:  <04-24-2024>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import datetime as dt

#%% CONSTANTS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
datetime_format = '%m-%d-%Y %H:%M:%S'

#%% MAIN CODE               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Logs actions in the 'Output/app.log' file
def log_message(message):
    timestamp = dt.datetime.now().strftime(datetime_format)
    log_entry = f'{timestamp} - {message}\n'
    with open('Output/app.log', 'a') as log_file:
        log_file.write(log_entry)
#
