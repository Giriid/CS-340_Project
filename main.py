#%% MODULE BEGINS
module_name = '<main>'

'''
Version: <0.3>

Description:
    <***>

Authors:
    <Adam, Josh, Josh>

Date Created     :  <04-08-2024>
Date Last Updated:  <04-24-2024>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from logger import log_message
from DataProcessor import DataProcessor

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def user_interface(data_processor, filtered_data, search_condition, column1, column2, count, column_name):
    while True:
        try:
            print('\n-----------------------------------------------------------')
            print('\n1. Perform a search')
            print('\n2. Visualize data')
            print('\n3. Calculate stats')
            print('\n4. Categorical analysis')
            print('\n5. Exit')
            choice = input('Input a number from the list: ')

            log_message(f'User input choice: {choice}')

            if choice == '1':
                # Prompt the user to enter the query condition.
                search_condition = input('Enter the query condition (ex. Year > 1950): ')

                # Log the user search condition
                log_message(f'User input search condition: {search_condition}')

                # Call the query_data method of the 'DataProcessor' class
                filtered_data = data_processor.query_data(search_condition)
                log_message('"query_data(...)" called successfully')

                print(f'\nFiltered Data: {search_condition}')
                print(filtered_data)
            elif choice == '2':
                # Call the visualize_data method of the 'DataProcessor' class
                if filtered_data.empty:
                    data_processor.visualize_data(None, None)
                else:
                    data_processor.visualize_data(filtered_data, search_condition)
                #
                log_message('"visualize_data(...)" called successfully')
            elif choice == '3':
                column1 = input('Input the name of the first column: ')
                column2 = input('Input the name of the second column: ')
                
                log_message(f'User input: column1="{column1}", column2="{column2}"')

                data_processor.calculate_stats(column1, column2)
            elif choice == '4':
                # Asks user for column name to analyze
                column_name = input(
                    'Input a column name to obtain unique values, generate permutations, and generate combinations'
                )
                log_message(f'User column name: {column_name}')

                count = input('Input the amount of permutations and combinations to generate - leave blank for none: ')
                log_message(f'User count selection: {count}')

                #------------------------------------------------------------------------------------
                # Passing 'count' as type str but should be of type int
                # Call the categorical_analysis method of the 'DataProcessor' class
                unique_values = data_processor.categorical_analysis(column_name, count)
                #------------------------------------------------------------------------------------

                print(unique_values)
            elif choice == '5':
                log_message('Exiting the program')
                print('\nExiting the program.')
                break
            else:
                log_message('Invalid input received')
                print('\nInvalid input. Please input a valid option.')
            #
        except Exception as e:
            log_message(f'\n---------------------------\nAn error occurred: {str(e)}\n---------------------------')
            print(f'\nAn error occurred: {str(e)}')
        #
    #
#

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code start here
def run():
    log_message('Starting the program')
    data_processor = DataProcessor() # Create an instance of the 'DataProcessor' class
    filtered_data = None
    search_condition = None
    column1 = None
    column2 = None
    count = None
    column_name = None

    # Call the read/store data method of the 'DataProcessor' class
    data_processor.read_data()

    # Call the User Interface
    user_interface(data_processor, filtered_data, search_condition, column1, column2, count, column_name)
#

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    log_message(f'"{module_name}" module begins')
    # Start the program
    run()
#

#%%
