#%% MODULE BEGINS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module_name = '<DataAnalyzer>'

'''
Version: <0.2>

Description:
    <***>

Authors:
    <Adam>

Date Created     :  <04-16-2024>
Date Last Updated:  <04-24-2024>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import Config
import importlib.util
from logger import log_message
import matplotlib.pyplot as plt
import numpy as np
import os

#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Gets all variables in the 'Config.py' file and stores them in a dictionary
def configuration(self):
    log_message('Getting config constants from "Config.py"')

    # Load the Config module
    spec = importlib.util.spec_from_file_location('Config', 'Config.py')
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)

    log_message('Creating a dictionary using config constants')

    # Create a dictionary to store the variables
    config_constants = {
        name: getattr(config, name) for name in dir(config) if not name.startswith('__')
    }

    log_message('Completed getting/setting config constants')
    return config_constants

#%% FUNCTIONS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_bins(data):
    log_message('Calculating bin size..')
    # Sturges' Formula
    return int(np.ceil(np.log2(len(data)) + 1))
#

#%% CLASS BEGINS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataAnalyzer():
    log_message(f'"{module_name}" module begins')

    # Constructor
    def __init__(self):
        # Store config constants in a dictionary
        self.config_constants = configuration(self)
    #

    # Create a Histogram
    def make_histogram(self, data, column_name, range=None, density=False):
        # Clear any previous plots from the same figure
        plt.clf()

        log_message(f'Creating a histogram using "data[{column_name}]"')

        bins = set_bins(data)
        log_message(f'bins = {bins}')

        # Extract the column data from the DataFrame
        column_data = data[column_name]

        # Plot the histogram
        plt.figure(figsize=(8,6))
        plt.hist(column_data, bins=bins, range=range, density=density)

        # Add labels and title
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.title('Histogram of ' + column_name)

        # Add additional features/information here if needed

        # Save the histogram plot
        plt.savefig(os.path.join('OUTPUT/', 'histogram.png'))
        log_message('Histogram saved to "OUTPUT/histogram.png"')

        # Display the histogram
        plt.show()
        log_message('Histogram created')
    #

    # Create a Line Plot
    def make_line_plot(self, x_values, y_values, xlabel='', ylabel='', title=''):
        # Clear any previous plots from the same figure
        plt.clf()

        log_message('Creating a line plot')
        
        plt.figure(figsize=(8,6))

        plt.plot(x_values, y_values)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

        plt.grid(True)

        # Save the line plot
        plt.savefig(os.path.join('OUTPUT/', 'line-plot.png'))
        log_message('Line plot saved to "OUTPUT/line-plot.png"')

        # Display the plot
        plt.show()
        log_message('Line plot created')
    #

    # Search for a value in the data
    def query_data(self, data, condition):
        if not condition.strip():
            return data
        #
        
        log_message(f'Searching for  {condition}  in data..')

        # Split the query condition into column name, operator, and value
        column_name, operator, value = condition.split()

        # Retrieve the column data from the dataframe
        column_data = data[column_name]

        # Apply the condition to filter the data
        if operator == '>':
            filtered_data = data[column_data > int(value)]
        elif operator == '<':
            filtered_data = data[column_data < int(value)]
        elif operator == '>=':
            filtered_data = data[column_data >= int(value)]
        elif operator == '<=':
            filtered_data = data[column_data <= int(value)]
        else:
            log_message('ValueError("Invalid operator. Use >, <, >=, or <=")')
            raise ValueError('Invalid operator. Use >, <, >=, or <=')
        
        log_message('Search complete')
        
        # Return the filtered data
        return filtered_data
    #
#
