"""
importing date from datetime module
"""
from datetime import date
"""
importing data from index.py
"""
from index import dishes,rooms,games,laundary

class Hotelms:
    """
    A class for managing user data in a hotel
    """

    def __init__(self):
         self.user_name =''
         self.user_address = ''
         self.checkindate = None
         self.checkoutdate = None
         self.days_spent = 0
         self.total_bill = 0
         self.totalroomrent = 0
         self.totalrestaurantbill = []
         self.totallaundarybill = []
         self.totalgamebill = []


    def get_customer_data(self):
        """
        Prompts for user data and calculate days spent
        """
        user_name = input('Please enter your name: ')
        user_address = input('Please enter your address: ')
        if not isinstance(user_name, str):
            raise ValueError('Invalid user name')
        else:
            self.user_name = user_name
            self.user_address = user_address
        try :
            
            while True:    
                checkinyear = int(input('Enter checkin year: '))
                checkinmonth = int(input('Enter checkin month: '))
                checkinday = int(input('Enter checkin day: '))
                self.checkindate= date(checkinyear, checkinmonth, checkinday)
                checkoutyear = int(input('Enter checkout year: '))
                checkoutmonth = int(input('Enter checkout month: '))
                checkoutday = int(input('Enter checkout day: '))
                self.checkoutdate= date(checkoutyear, checkoutmonth, checkoutday)
                if self.checkindate >= self.checkoutdate:
                    print("Error:Check-out date must be later than check-in date.")
                    continue
                elif self.checkindate == self.checkoutdate:
                    self.days_spent = 1
                break
        except ValueError:
            print("Invalid date input")
            return


        
        
        self.days_spent = (self.checkoutdate - self.checkindate).days
        print(f"Total days spent: {self.days_spent}")
        
        

    
    # Calculate the rent to be paid 
    def calculate_room_rent(self):
        """
        users room choice and rent calculation
        """
        roomprice = 0
        totaldayspent = self.days_spent
        while True:
            try:
                roomnumber = int(input("Select room number between 1 and 4: "))

                if (roomnumber <= 0 or roomnumber >= 5):
                    print("please choose between the numbers 1 to 4")
                    continue 
                elif (roomnumber == 1):
                    roomprice = rooms['one']
                elif (roomnumber == 2):
                    roomprice = rooms['two']
                elif (roomnumber == 3):
                    roomprice = rooms['three']
                elif (roomnumber == 4):
                    roomprice = rooms['four']
                else:
                    print("Room Number must be an integer")
                    continue


                print(f"Room Number: {roomnumber}")
                print(f"Room Price: {roomprice * totaldayspent}")
                print("------------------------------------------\n")

                self.totalroomrent =  roomprice * totaldayspent
                break
                
            except:
                print("Room Number must be an integer")
    

        
        # Calculate the restaurant bill
    def calculate_restaurant_bill(self):
        for index in range(len(dishes)):
            for key,val in dishes[index].items():
                print("{} : {}".format(key, val))
            print("-------------------------------------------\n")
        # choose meal id
        menuId = int(input("Select the meal id form the menu list above: "))
        try:
            choosenitem = [i for i in dishes if i['id'] == menuId][0]
            print("{} : {}".format("Food Item", "Price $"))
            print("------------------------------------------")
            print("{} : ${}".format(choosenitem['title'], choosenitem['price']))
            print("-------------------------------------------\n")
            self.totalrestaurantbill.append(choosenitem['price'])
            # print(choosenitem['price'])
            # print(sum(self.totalrestaurantbill))
        except IndexError:
            print("Index not found")
    
    # Calculate laundary bill
    def calculate_laundary_bill(self):
        """
        Prompts the user to select a laundry list, 
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
        print(f"Total Bill: of {self.user_name} is  {self.total_bill}")
        


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
           user.get_customer_data()
        elif option == 2:
            user.calculate_room_rent()
        elif option == 3:
            user.calculate_restaurant_bill()
        elif option == 4:
            user.calculate_game_bill()
        elif option == 5:
            user.calculate_laundary_bill()
        elif option == 6:
             print("------------------------------------------\n")
             user.generate_bill()
             print("------------------------------------------\n")
        elif option == 7:
            print("------------------------------------------\n")
            print('Thank you for visiting our hotel')
            print("------------------------------------------\n")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')