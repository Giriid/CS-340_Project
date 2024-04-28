#%% MODULE BEGINS
module_name = '<DataProcessor>'

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
import DataAnalyzer
import itertools
from logger import log_message
import os
import pandas as pd

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
    def visualize_data(self, data, condition=None):
        log_message(f'Visualizing data using "condition={condition}"')

        if condition is not None: # If a condition is passed
            column_name, operator, value = condition.split()

            # Histogram
            self.make_histogram(data, column_name)
            
            # Line plot
            title = f'Filtered Data: {condition}'
            x_values = data[self.config_constants['def_xvalues']]
            y_values = data[column_name]
            self.make_line_plot(
                data,
                x_values,
                y_values,
                xlabel=self.config_constants['def_xlabel'],
                ylabel=column_name,
                title=title
            )
        else: # If no condition is passed
            # Histogram
            self.make_histogram(data)

            # Line plot
            self.make_line_plot(data)
        #
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
        all_stats.to_csv(os.path.join('OUTPUT/', f'Statistics.csv'))
        log_message('Saved data statistics to "OUTPUT/Statistics.csv"')
    #

    # Generate categorical analysis
    def categorical_analysis(self, column_name):
        # Obtain unique values
        log_message('Generating unique values..')
        unique_values = self.data[column_name].unique()
        print(unique_values)

        # Generate permutations of unique values
        log_message('Generating permutations of unique values..')

        if len(unique_values) > 10:
            log_message('Number of unique values is large, limiting amount of permutations..')
            unique_values_subset = unique_values[:10]
            permutations = list(itertools.permutations(unique_values_subset))
        else:
            permutations = list(itertools.permutations(unique_values))
        #
        print(permutations)

        # Generate combinations of unique values
        log_message('Generating combinations of unique values..')

        combinations = []
        
        if len(unique_values) > 10:
            log_message('Number of unique values is large, limiting amount of combinations..')
            unique_values_subset = unique_values[:10]
            for r in range(1, min(len(unique_values), self.config_constants['max_unique_values']) + 1):
                subset_combinations = list(itertools.combinations(unique_values_subset, r))
                combinations.extend(subset_combinations)
            #
        else:
            for r in range(1, len(unique_values) + 1):
                combinations.extend(itertools.combinations(unique_values, r))
        #
        print(combinations)

        # Create DataFrame to store analysis
        analysis_df = pd.DataFrame({
            'Unique_Values': [unique_values],
            'Permutations': [permutations],
            'Combinations': [combinations]
        })

        # Save the analysis to a CSV file
        analysis_df.to_csv(os.path.join('OUTPUT/', f'Analysis.csv'))
        log_message('Saved categorical analysis to "OUTPUT/Analysis.csv"')
    #
#
