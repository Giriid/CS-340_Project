#   • Read data from a csv file.
#   • Store into a dataframe.
#   • Utilize configuration constants
#   • Visualize distributions in each column using
#       • Violin plot
#       • Whisker-box plot
#       • Scatter plot
#   • Query data for searching and display
#       • A set of numeric and string values
#           • Using Boolean indexing
#   • Calculate and display
#       • joint counts
#       • joint probabilities
#       • conditional probabilities
#       • mean, median, std
#   • For a categorical attribute do the following and display
#       • Obtain unique values
#       • Generate permutations
#       • Generate combinations

#%% MODULE BEGINS
module_name = '<Child>'

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

from Parent import Parent
from Config import Config

#%% CLASS BEGINS
class Child(Parent):
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
