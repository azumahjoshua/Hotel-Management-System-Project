from datetime import date

from dishes import dishes
# 
rooms = {
    "one":2000,
    "two":3000,
    "three":4000,
    "four":5000
}


class Hotelms:

    def __init__(self, user_name ='',user_address='',checkindate = '',checkoutdate = '',dayspent = 0, total_bill=0,totalroomrent=0,totalrestaurantbill=[]):
         self.user_name =user_name
         self.user_address = user_address
         self.checkindate = checkindate 
         self.checkoutdate = checkoutdate
         self.dayspent = dayspent
         self.total_bill = total_bill
         self.totalroomrent = totalroomrent
         self.totalrestaurantbill = totalrestaurantbill

    # A function to get user data name, address,checkout dates and checking in dates. The function also calculate the days to be spent by the user
    def customerData(self):
        self.user_name = input('Please enter your name: ')
        self.user_address = input('Please enter your address: ')
        checkinyear = int(input('Enter checkin year: '))
        checkinmonth = int(input('Enter checkin month: '))
        checkinday = int(input('Enter checkin day: '))
        self.checkindate= date(checkinyear, checkinmonth, checkinday)
        checkoutyear = int(input('Enter checkout year: '))
        checkoutmonth = int(input('Enter checkout month: '))
        checkoutday = int(input('Enter checkout day: '))
        self.checkoutdate= date(checkoutyear, checkoutmonth, checkoutday)

        while (self.checkindate >= self.checkoutdate):
            print("Error inputing Date: Checking out should be greater than checking in")
            checkinyear = int(input('Enter checkin year: '))
            checkinmonth = int(input('Enter checkin month: '))
            checkinday = int(input('Enter checkin day: '))
            self.checkindate= date(checkinyear, checkinmonth, checkinday)
            checkoutyear = int(input('Enter checkout year: '))
            checkoutmonth = int(input('Enter checkout month: '))
            checkoutday = int(input('Enter checkin day: '))
            self.checkoutdate= date(checkoutyear, checkoutmonth, checkoutday)
        self.dayspent = self.checkoutdate - self.checkindate
        self.dayspent = self.dayspent.days




    
    # Calculate the rent to be paid 
    def calculateRoomRent(self):
        roomnumber = int(input("Select room number between 1 and 4: "))
        roomprice = 0
        totaldayspent = self.dayspent
        # print(totaldayspent.days)
        try:
            if(roomnumber<=0 or roomnumber >=5):
                print("please choose between the numbers 1 to 4")
                exit()  #to quit the program
            elif(roomnumber == 1):
                roomprice = rooms['one']
            elif(roomnumber == 2):
                roomprice = rooms['two']
            elif(roomnumber == 3):
                roomprice = rooms['three']
            elif(roomnumber == 4):
                roomprice = rooms['four']
            
            print(f"Room Number: {roomnumber}")
            print(f"Room Price: {roomprice*totaldayspent}")
            print("------------------------------------------\n")

            self.totalroomrent = roomprice*totaldayspent
        except ValueError:
            print("Room Number must be an integer")

        
    def restaurantBill(self):
        # print menu
        print(len(dishes))
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
        


    # def laundaryBill():
        # pass
    # def gameBill():
        # pass
    def totalExpenditure(self):
        # room_rent = self.calculateRoomRent()
        # restaurant_bill = self.restaurantBill()
        # Add calls to other bill calculation methods here
        # bills = 0
        self.total_bill = sum(self.totalrestaurantbill) + self.totalroomrent
        # Add up the results of all the bill calculation methods
        # bills += self.total_bill
        return self.total_bill 


print("-------------------------- Hotel-Management-System Menu Options -----------------------------------------")

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
             print("------------------------------------------\n")
             print(f"Total Bill: {user.totalExpenditure()}")
             print("------------------------------------------\n")
        elif option == 5:
            print("------------------------------------------\n")
            print('Thanks message before exiting')
            print("------------------------------------------\n")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')