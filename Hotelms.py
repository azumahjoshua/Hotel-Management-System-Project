from datetime import date

from index import dishes,rooms,games,laundary

class Hotelms:
    """
    A class for managing a hotel guest's stay, including their name, 
    check-in and check-out dates, and the total cost of their stay.
    """
    # initillise data
    def __init__(self):
         self.user_name =''
         self.user_address = ''
         self.checkindate = None
         self.checkoutdate = None
         self.dayspent = 0
         self.total_bill = 0
         self.totalroomrent = 0
         self.totalrestaurantbill = 0
         self.totallaundarybill = 0
         self.totalgamebill = 0

    # A function to get user data name, address,checkout dates and checking in dates. The function also calculate the days to be spent by the user
    def get_customer_data(self):
        """
        Prompts the user for their name, address, and check-in and check-out dates, 
        and calculates the number of days the guest will be staying at the hotel.
        """

        self.user_name = input('Please enter your name: ')
        self.user_address = input('Please enter your address: ')
        try :
            checkinyear = int(input('Enter checkin year: '))
            checkinmonth = int(input('Enter checkin month: '))
            checkinday = int(input('Enter checkin day: '))
            self.checkindate= date(checkinyear, checkinmonth, checkinday)
            checkoutyear = int(input('Enter checkout year: '))
            checkoutmonth = int(input('Enter checkout month: '))
            checkoutday = int(input('Enter checkout day: '))
            self.checkoutdate= date(checkoutyear, checkoutmonth, checkoutday)
        except ValueError as error:
            print("Invalid date input:", error)
            return


        if self.checkindate >= self.checkoutdate:
            raise ValueError("Error: Check-out date must be later than check-in date.")
        
        self.days_spent = (self.check_out_date - self.check_in_date).days
        print(f"Total days spent: {self.days_spent}")
        
        

    
    # Calculate the rent to be paid 
    def calculate_room_rent(self):
        """
        Prompts the user to select a room number, and calculates the cost of the room rental
        based on the number of days the guest will be staying.
        """
        try:
            roomnumber = int(input("Select room number between 1 and 4: "))
            room_price = rooms['roomnumber']
            if not room_price:
                raise ValueError("Invalid room number. Please choose between 1 and 4.")
            totaldayspent = self.dayspent

            print(f"Room Number: {roomnumber}")
            print(f"Room Price: {room_price*totaldayspent}")
            print("------------------------------------------\n")

            self.totalroomrent. room_price*totaldayspent
        except ValueError:
            print("Room Number must be an integer")
            return

        
        # Calculate the restaurant bill
    def calculate_restaurant_bill(self):
        """
        Prompts the user to select a food id from the hotel restaurant menu, 
        the user can aslo select multiple foods and the price is  stored in a list.
        the function calculates the total bills in te restaurant
        """
        # print menu
        # print(len(dishes))
        for index in range(len(dishes)):
            for key,val in dishes[index].items():
                print("{} : {}".format(key, val))
            print("-------------------------------------------\n")
        # choose meal id
        menuId = int(input("Select the meal id form the menu list above: "))
        # next(filter(lambda obj: obj.get('id') == menuId, dishes), None)
        try:
            choosenitem = [i for i in dishes if i['id'] == menuId][0]
            print("{} : {}".format("Food Item", "Price $"))
            print("------------------------------------------")
            print("{} : {}".format(choosenitem['title'], choosenitem['price']))
            print("-------------------------------------------\n")
            self.totalrestaurantbill.append(choosenitem['price'])
            # print(choosenitem['price'])
            # print(sum(self.totalrestaurantbill))
        except IndexError:
            print("Index not found")
    
    # Calculate laundary bill
    def calculate_laundary_bill(self):
        """
        Prompts the user to select a lundary list, the user can aslo select multiple lundary list and the price is  stored in a list.
        the function calculates the total bills
        """

        for index in range(len(laundary)):
            for key,val in laundary[index].items():
                print("{} : {}".format(key, val))
            print("-------------------------------------------\n")
            # choose laundary id
        laundayId = int(input("Select the laundary id form the laundary list above: "))
        try:
            choosenitem = [i for i in laundary if i['id'] == laundayId][0]
            print("{} : {}".format("Launday Item", "Price $"))
            print("------------------------------------------")
            print("{} : {}".format(choosenitem['name'], choosenitem['price']))
            print("-------------------------------------------\n")
            self.totallaundarybill.append(choosenitem['price'])
        except IndexError:
            print("Index not found")

# calculate game bill
    def calculate_game_bill(self):
        """
        Prompts the user to select a game of choice, and calculate the total game bill

        """
        for index in range(len(games)):
            for key,val in games[index].items():
                print("{} : {}".format(key, val))
        print("-------------------------------------------\n")
        gameId = int(input("Select the game id form the game list above: "))
        try:
            choosenitem = [i for i in games if i['id'] == gameId][0]
            print("{} : {}".format("Game Item", "Price $"))
            print("------------------------------------------")
            print("{} : {}".format(choosenitem['name'], choosenitem['price']))
            print("-------------------------------------------\n")
            self.totalgamebill.append(choosenitem['price'])
        except IndexError:
            print("Index not found")

    # totale expenditure
    def generate_bill(self):
        """
        Calculate the total expenditure of the user in the hotel
        """
        self.total_bill = sum(self.totalrestaurantbill) + self.totalroomrent + sum(self.totalgamebill)
        + sum(self.totallaundarybill)
        # Add up the results of all the bill calculation methods
        # bills += self.total_bill
        print(f"Total Bill: {self.total_bill}")
        


print("-------------------------- Hotel-Management-System Menu Options -----------------------------------------")

menu_options = {
    1: '(User Data: )Option 1',
    2: '(Select Room Number: )Option 2',
    3: '(Select Restaurants: )Option 3',
    4: '(Select Game: )Option 4',
    5: '(Select Laundary: )Option 5',
    6: '(Total Expenditure: )Option 6',
    7: 'Exit',
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
            print("------------------------------------------\n")
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
            user.gameBill()
        elif option == 5:
            user.laundaryBill()
        elif option == 6:
             print("------------------------------------------\n")
             user.generate_bill()
             print("------------------------------------------\n")
        elif option == 7:
            print("------------------------------------------\n")
            print('Thanks message visiting our hotel')
            print("------------------------------------------\n")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')