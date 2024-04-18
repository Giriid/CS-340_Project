#%% MODULE BEGINS
module_name = '<DataProcessor>'

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
import pandas as pd

from DataAnalyzer import DataAnalyzer
from Config import Config

#%% CLASS BEGINS
class DataProcessor(DataAnalyzer):
    # Constructor
    def __init__(self):
        super().__init__(Config())

        self.dataframe = None
        self.filepath = Config.filepath
    #

    # Read the data and store it in a DataFrame
    def read_data(self):
        self.dataframe = pd.read_csv(self.filepath)
    #

    # Visualize the stored data
    def visualize_data(self, data, condition):
        if not condition.strip():
            return self.make_line_plot(
                data['Year'],
                data['Total_Athletes'],
                xlabel='Year',
                ylabel='Total Athletes',
                title='Total Attending Athletes at the Summer Games')
        
        column_name, operator, value = condition.split()

        # Construct the title of the plot using the query condition
        title = f'Filtered Data: {condition}'

        # Display Line Plot
        x_values = data['Year']
        y_values = data[column_name]

        self.make_line_plot(x_values, y_values, xlabel='Year', ylabel=column_name, title=title)
    #

    # Query data for searching and displaying
    def query_data(self, condition):
        '''
        Search for a value in the data based on a condition.

        Parameters:
        - condition (str): The condition for filtering the data.

        Returns:
        - filtered_data (DataFrame): The filtered DataFrame based on the condition.
        '''
        filtered_data = super().query_data(self.dataframe, condition)

        return filtered_data
    #
    
    # Calculate and diplay the stats of the stored data
    def calculate_stats(self):
        # Get joint counts
        #def getJointCounts():

        #
        # Get joint probabilities
        #def getJointProb():
            
        #

        # Get conditional probabilities
        #def getCondProb():
            
        #

        # Get statistics of data
        #def getStats():
            
        #
        pass
    #
#
