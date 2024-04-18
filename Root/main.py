#%% MODULE BEGINS
module_name = '<main>'

'''
Version: <0.2>

Description:
    <***>

Authors:
    <Adam, Josh, Josh>

Date Created     :  <04-08-2024>
Date Last Updated:  <04-17-2024>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from DataProcessor import DataProcessor
from DataAnalyzer import DataAnalyzer

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_query_condition():
    '''
    Prompt the user to enter the query condition.

    Returns:
    - condition (str): The query condition entered by the user.
    '''
    return input('Enter the query condition (ex. Year > 1950): ')

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def init(self):
    self.data_processor = DataProcessor()
    self.data_analyzer = DataAnalyzer({})

#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Global declarations Start Here



# Class definitions Start Here


# Function definitions Start Here


#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code start here
class Main:
    # Create an instance of the 'DataProcessor' class
    def __init__(self):
        init(self)
    #
    
    def run(self):
        # Call the read/store data method of the 'DataProcessor' class
        self.data_processor.read_data()

        # Get the query condition from the user
        condition = get_query_condition()

        # Call the query_data method of the 'DataProcessor' class with the user provided condition
        filtered_data = self.data_processor.query_data(condition)

        # Display the filtered data
        print('Filtered Data:')
        print(filtered_data)

        # Call the visualize_data method of the 'DataProcessor' class with the filtered data
        self.data_processor.visualize_data(filtered_data, condition)
    #
#

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    # Instantiate 'Main' class
    main_instance = Main()

    # Run the 'Main' class
    main_instance.run()

# %%
