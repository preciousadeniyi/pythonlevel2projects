class USSDMenu:
    '''Class to represent a USSD menu system.'''

    def __init__(self):
        
        self.options = {
            '1': 'My Offer',
            '2': 'My Area',
            '3': 'Data Plans',
            '4': 'N5000/18GB',
            '5': 'N3000/10GB',
            '6': 'N1500/2GB',
            '7': 'N500/2GB',
            '8': 'SMART DATA PLANS',
            '9': 'BORROW AIRTIME/DATA',
            '10': 'FAMILY PLAN'
        }

    def display_menu(self):
        
        print("Welcome to USSD Menu:")
        for key, value in self.options.items():
            print(f"{key}. {value}")

    def handle_selection(self, choice):
        
        if choice == '1':
            self.display_offer_menu()
        elif choice == '2':
            print("Large Area Options:")
            print("1. 10k/20GB for 30 days")
            print("2. 100k/1TB for 365 days")
        elif choice == '3':
            self.display_data_plans()
        elif choice == '8':
            self.display_smart_data_plans()
        elif choice == '9':
            print("You've selected BORROW AIRTIME/DATA. You can now borrow airtime or data.")
        elif choice == '10':
            print("Family Plan Options:")
            print("1. Option 1")
            print("2. Option 2")
            print("3. Option 3")
        elif choice.isdigit() and choice in self.options:
            print(f"You've selected {self.options[choice]}")
        else:
            print("Invalid selection. Please try again.")

    def display_offer_menu(self):
        '''Display offer menu.'''
        offer_menu = {
            '1': 'N100 for 500MB',
            '2': 'N200 for 1GB'
        }
        print("Offer Menu:")
        for key, value in offer_menu.items():
            print(f"{key}. {value}")
        choice = input("Enter your choice: ")
        if choice in offer_menu:
            print(f"You've selected {offer_menu[choice]}. You've been credited.")
        else:
            print("Invalid selection. Please try again.")

    def display_data_plans(self):
        '''Display data plans menu.'''
        print("Data Plans:")
        print("1. N50 for 50MB (1 day)")
        print("2. N100 for 100MB (1 day)")
        
        print("7. N3000 for 10GB (30 days)")

    def display_smart_data_plans(self):
        '''Display smart data plans menu.'''
        print("Smart Data Plans:")
        print("1. Smart Plan 1")
        print("2. Smart Plan 2")
        

def main():
    
    ussd_menu = USSDMenu()
    while True:
        ussd_menu.display_menu()
        choice = input("Enter your choice (or '#' to exit): ")
        if choice == '#':
            print("Exiting USSD menu.")
            break
        try:
            ussd_menu.handle_selection(choice)
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()

