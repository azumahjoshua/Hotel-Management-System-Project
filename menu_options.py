from Hotelms import Hotelms

menu_options = {
    1: '(User Data: )Option 1',
    2: '(Select Room: )Option 2',
    3: '(Select Restaurants: )Option 3',
    4: '(Total Expenditure: )Option 4',
    5: 'Exit',
}

# create an object of  a user
user = Hotelms()

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           user.customerData()
        elif option == 2:
            user.calculateRoomRent()
        elif option == 3:
            user.restaurantBill()
        elif option == 4:
             print(f"Total Bill: {user.totalExpenditure()}")
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')