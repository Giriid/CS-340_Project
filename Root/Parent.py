#%% MODULE BEGINS
module_name = '<Parent>'

'''
Version: <0.1>

Description:
    <***>

Authors:
    <Adam>

Date Created     :  <04-16-2024>
Date Last Updated:  <04-17-2024>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS
import matplotlib.pyplot as plt


#%% CLASS BEGINS
class Parent():
    # Constructor
    def __init__(self, config_constants):
        # Store config constants in a dictionary
        self.config_constants = config_constants
    #

    # Create a Histogram
    def make_histogram(self, data, column_name):
        # Extract the column data from the DataFrame
        column_data = data[column_name]

        # Plot the histogram
        plt.hist(column_data, bins=10)

        # Add labels and title
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.title('Histogram of ' + column_name)

        # Display the plot
        plt.show()
    #

    # Create a Line Plot
    def make_line_plot(self, x_values, y_values, xlabel='', ylabel='', title=''):
        plt.figure(figsize=(8,6))

        plt.plot(x_values, y_values)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

        plt.grid(True)


        # Display the plot
        plt.show()
    #

    # Search for a value in the data
    def query_data(self, data, condition):
        filtered_data = data.query(condition)
        return filtered_data
    #
#
