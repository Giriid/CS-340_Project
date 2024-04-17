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
            raise ValueError('Invalid operator. Use >, <, >=, or <=')
        
        # Return the filtered data
        return filtered_data
    #
#
