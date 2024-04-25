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
def user_interface(self):
    while True:
        try:
            print('\n-----------------------------------------------------------')
            print('\n1. Perform a search')
            print('\n2. Visualize data')
            print('\n3. Calculate stats')
            print('\n4. Exit')
            choice = input('Input a number from the list: ')

            log_message(f'User input choice: {choice}')

            if choice == '1':
                # Prompt the user to enter the query condition.
                self.search_condition = input('Enter the query condition (ex. Year > 1950): ')

                # Log the user search condition
                log_message(f'User input search condition: {self.search_condition}')

                # Call the query_data method of the 'DataProcessor' class
                self.filtered_data = self.data_processor.query_data(self.search_condition)
                log_message('"query_data(...)" called successfully')

                print(f'\nFiltered Data: {self.search_condition}')
                print(self.filtered_data)
            elif choice == '2':
                # Call the visualize_data method of the 'DataProcessor' class
                if self.filtered_data.empty:
                    self.data_processor.visualize_data(None, None)
                else:
                    self.data_processor.visualize_data(self.filtered_data, self.search_condition)
                #
                log_message('"visualize_data(...)" called successfully')
            elif choice == '3':
                self.column1 = input('Input the name of the first column: ')
                self.column2 = input('Input the name of the second column: ')
                log_message(f'User input: column1="{self.column1}", column2="{self.column2}"')

                self.data_processor.calculate_stats(self.column1, self.column2)

            elif choice == '4':
                log_message('Exiting the program')
                print('\nExiting the program.')
                break
            else:
                log_message('Invalid input received')
                print('\nInvalid input. Please input a valid option.')
            #
        except Exception as e:
            log_message(f'An error occurred: {str(e)}')
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
class Main:
    # Create an instance of the 'DataProcessor' class
    def __init__(self):
        self.data_processor = DataProcessor()
        self.filtered_data = None
        self.search_condition = None
        self.column1 = None
        self.column2 = None
    #
    
    def run(self):
        log_message('Starting the program')

        # Call the read/store data method of the 'DataProcessor' class
        self.data_processor.read_data()

        # Call the User Interface
        user_interface(self)
    #
#

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    log_message(f'"{module_name}" module begins.')
    
    # Instantiate 'Main' class
    main_instance = Main()

    # Run the 'Main' class
    main_instance.run()
#

#%%
