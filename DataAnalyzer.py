#%% MODULE BEGINS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module_name = '<DataAnalyzer>'

'''
Version: <0.2>

Description:
    <***>

Authors:
    <Adam>

Date Created     :  <04-16-2024>
Date Last Updated:  <04-27-2024>

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
import pandas as pd

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
        self.xvalues = pd.DataFrame({})
    #

    # Create a Histogram
    def make_histogram(self, data, column_name=None, range=None, density=False):
        plt.clf()

        try:
            # Default value if no 'column_name' is given
            if column_name is None:
                column_name = self.config_constants['def_yvalues']

            log_message(f'Creating a histogram using "data[{column_name}]"')

            bins = set_bins(data)
            log_message(f'bins = {bins}')

            # Extract the column data from the DataFrame
            column_data = data[column_name]

            # Plot the histogram
            plt.hist(column_data, bins=bins, range=range, density=density)

            # Add labels and title
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.title('Histogram of ' + column_name)

            # Add additional features/information here if needed

            # Save the histogram plot
            plt.savefig(os.path.join('OUTPUT/', 'Histogram_Plot.png'))
            log_message('Histogram saved to "OUTPUT/Histogram_Plot.png"')

            # Display the histogram
            plt.show()
            log_message('Histogram created')
        except Exception as e:
            log_message(f'\n---------------------------\nAn error occurred: {str(e)}\n---------------------------')
            print(f'\nAn error occurred: {str(e)}')
        #
    #

    # Create a Line Plot
    def make_line_plot(self, data, x_values=None, y_values=None, xlabel='', ylabel='', title=''):
        plt.clf()

        if x_values is None:
            x_values = data[self.config_constants['def_xvalues']]
            y_values = data[self.config_constants['def_yvalues']]
            xlabel = self.config_constants['def_xlabel']
            ylabel = self.config_constants['def_ylabel']
            title = self.config_constants['def_title']
        #

        log_message('Creating a line plot')

        plt.plot(x_values, y_values)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)

        # Save the line plot
        plt.savefig(os.path.join('OUTPUT/', 'Line_Plot.png'))
        log_message('Line plot saved to "OUTPUT/Line_Plot.png"')

        # Display the plot
        plt.show()
        log_message('Line plot created')
    #

    # Search for a value in the data
    def query_data(self, data, condition):
        if not condition.strip():
            return data
        #
        
        log_message(f'Searching for "{condition}" in data..')

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
