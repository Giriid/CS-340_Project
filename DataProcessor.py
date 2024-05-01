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
import csv
import DataAnalyzer
from itertools import permutations
from itertools import combinations
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
        unique_values = set(self.data[column_name].unique())
        print(f'\nUnique Values:\n{unique_values}')
        
        '''
        Generate permutations of unique values
            Since the time complexity of generating permutations is O(n!),
                - n is the number of elements in the input iterable
                the amount of permutations have been limited to the
                value of  max_unique_values  in the Config.py file
        '''
        log_message('Generating permutations of unique values..')
        permutation_values = list(permutations(unique_values, self.config_constants['max_unique_values']))
        print(f'Permutations:\n{permutation_values}')
        
        '''
        Generate combinations of unique values
            Since the time complexity of generating combinations is O(nCr),
                - n is the number of elements in the input iterable
                - r is the size of each combination
                - C = (n / r) = (n! / (r!(n - r)!))
                the amount of combinations have been limited to the value
                of  max_unique_values  in the Config.py file
        '''
        log_message('Generating combinations of unique values..')
        combination_values = list(combinations(unique_values, self.config_constants['max_unique_values']))
        print(f'Combinations:\n{combination_values}')
        
        # Write the analysis to a CSV file
        log_message('Writing categorical analysis to file..')
        with open('Output/Analysis.csv', 'w', newline='') as analysis:
            writer = csv.writer(analysis)
            
            # Get the length of the longer '..._values' for padding when writing
            max_len = max(len(unique_values), len(permutation_values), len(combination_values))
            
            for index in range(max_len):
                unique_value = list(unique_values)[index] if index < len(unique_values) else ""
                perm_value = permutation_values[index] if index < len(permutation_values) else ""
                comb_value = combination_values[index] if index < len(combination_values) else ""
                writer.writerow([unique_value, perm_value, comb_value])
            #
        #
    #
#
