#%% MODULE BEGINS
module_name = '<DataProcessor>'

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
import DataAnalyzer
from logger import log_message
import itertools
import pandas as pd
import os

#%% CLASS BEGINS               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataProcessor(DataAnalyzer.DataAnalyzer):
    log_message(f'"{module_name}" module begins')

    # Constructor
    def __init__(self):
        self.data = None
        self.config_constants = DataAnalyzer.DataAnalyzer().config_constants
        self.filepath = self.config_constants['filepath']
    #

    # Read the data and store it in a DataFrame
    def read_data(self):
        log_message(f'Reading data at: {self.filepath}')
        self.data = pd.read_csv(self.filepath)
    #

    # Visualize the stored data
    def visualize_data(self, data, condition):
        log_message(f'Visualizing data using "condition={condition}"')
        
        # If there is no condition, then will display all data
        if not condition.strip():
            log_message(f'No condition given in "visualize_data(self, data, condition)"')
            log_message('Visualizing with default values')


            #------------------------------------------------------------------------------------
            # NEEDS TO BE MOVED TO PARENT CLASS!!!!!!!!!!!
            # Set to default values. Default values can be changed in Config file
            return (
                self.make_histogram(
                    data,
                    self.config_constants['def_yvalues'],
                ),
                self.make_line_plot(
                    data[self.config_constants['def_xvalues']],
                    data[self.config_constants['def_yvalues']],
                    xlabel=self.config_constants['def_xlabel'],
                    ylabel=self.config_constants['def_ylabel'],
                    title=self.config_constants['def_title'],
                ))
            #
            #------------------------------------------------------------------------------------
        #
        
        column_name, operator, value = condition.split()
        
        log_message(f'"column_name={column_name}"')

        # Construct the title of the plot using the query condition
        title = f'Filtered Data: {condition}'

        self.make_histogram(data, column_name)

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
        log_message(f'Searching data for "{condition}"')
        filtered_data = super().query_data(self.data, condition)

        filtered_data.to_csv(os.path.join('OUTPUT/', f'filtered_data.csv'))
        log_message(f'Saved filtered data to "OUTPUT/filtered_data.csv"')

        return filtered_data
    #
    
    # Calculate and diplay the stats of the stored data
    def calculate_stats(self, column1, column2):
        if self.data is None:
            print('No data available to calculate statistics.')
            log_message('No data available to calculate statistics')
            return
        #

        # Get joint counts
        log_message('Getting joint counts..')
        joint_counts = self.data.groupby([column1, column2]).size()
        print(f'\nJoint Counts:\n{joint_counts}')

        # Get joint probabilities
        log_message('Getting joint probabilites..')
        joint_prob = self.data.groupby([column1, column2]).size() / len(self.data)
        print(f'\nJoint Probabilites:\n{joint_prob}')

        # Get conditional probabilities
        log_message('Getting conditional probabilities..')
        cond_prob = self.data.groupby([column1, column2]).size() / self.data.groupby([column1]).size()
        print(f'\nConditional Probabilities:\n{cond_prob}')

        # Get statistics of data
        log_message('Getting data statistics..')
        stats = self.data.describe()
        print(f'\nStatistics:\n{stats}')

        # Concatenate all dataframes
        all_stats = pd.concat([joint_counts, joint_prob, cond_prob, stats], axis=1)

        # Save all_stats to a csv file
        all_stats.to_csv(os.path.join('OUTPUT/', f'{column1}-{column2}_all_statistics.csv'))
        log_message(f'Saved data statistics to "OUTPUT/{column1}-{column2}_all_statistics.csv"')
    #

    # Generate
    def categorical_analysis(self, column_name, count=None):
        # Create a DataFrame to store the analysis
        categorical_analysis = pd.DataFrame(columns=['unique_values', 'permutations', 'combinations'])
        
        # Obtain unique values
        log_message('Generating unique values..')
        unique_values = self.data[column_name].unique()
        categorical_analysis['unique_values'] = unique_values

        if count is not None:
            # Generate permutations
            log_message('Generating permutations..')
            permutations = list(itertools.permutations(unique_values, count))
            categorical_analysis['permutations'] = permutations
        
            # Generate combinations
            log_message('Generating combinations..')
            combinations = list(itertools.combinations(unique_values, count))
            categorical_analysis['combinations'] = combinations
        #
        
        # Save the analysis to a csv file
        categorical_analysis.to_csv(os.path.join('OUTPUT/', f'{column_name}_analysis.csv'), index=False)
        log_message(f'Saved categorical analysis to "OUTPUT/{column_name}_analysis.csv')
        return categorical_analysis
    #
#
