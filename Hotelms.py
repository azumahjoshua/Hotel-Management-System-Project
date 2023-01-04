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
    def __init__(self):
         self.user_name =''
         self.user_address=''
         self.checkindate = ''
         self.checkoutdate = ''
         self.dayspent = 0
         self.totalRent = 0
         self.totalMeal = 0
    
    # A function to get user data name, address,checkout dates and checking in dates. The function also calculate the the days to be spent by the user

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
        # checking out date should be greater than checking in date
        if(self.checkindate > self.checkoutdate):
            print("Error inputing Date: Checking out  should be greater than checking in")
            checkinyear = int(input('Enter checkin year: '))
            checkinmonth = int(input('Enter checkin month: '))
            checkinday = int(input('Enter checkin day: '))
            self.checkindate= date(checkinyear, checkinmonth, checkinday)
            checkoutyear = int(input('Enter checkout year: '))
            checkoutmonth = int(input('Enter checkout month: '))
            checkoutday = int(input('Enter checkin day: '))
            self.checkoutdate= date(checkoutyear, checkoutmonth, checkoutday)
        else:
            self.dayspent = self.checkoutdate - self.checkindate

    
    # Calculate the rent to be paid 
    def calculateRoomRent(self):
        roomnumber = int(input("Select room number:"))
        roomprice = 0
        totaldayspent = self.dayspent
        print(totaldayspent.days)
        try:
            if(roomnumber<=0 or roomnumber >=5):
                print("Room number should be be greater than 0 or less than 5")
                exit
            elif(roomnumber == 1):
                roomprice = rooms['one']
            elif(roomnumber == 2):
                roomprice = rooms['two']
            elif(roomnumber == 3):
                roomprice = rooms['three']
            elif(roomnumber == 4):
                roomprice = rooms['four']
            
            print(f"Room Number: {roomnumber}")
            print(f"Room Price: {roomprice*totaldayspent.days}")
            print("------------------------------------------\n")

            self.totalRent = roomprice*totaldayspent.days
            return self.totalRent
        except:
            print("Room Number must be a integer")

        
    def restarantBill(self):
        # print menu
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
            print("------------------------------------------\n")
            print("{} : $ {}".format(choosenitem['title'], choosenitem['price']))
            print("------------------------------------------\n")

            self.totalMeal = choosenitem['price']
            return self.totalMeal
            # print(choosenitem['price'])
        except IndexError:
            print("Index  not found")
        


    # def laundaryBill():
        # pass
    # def gameBill():
        # pass
    # def totalExpenditure(self):
        # print(f"Total Bill: {self.calculateRoomRent() + self.restarantBill()}")
        # return self.calculateRoomRent() + self.restarantBill()

       




# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))


# user1 = Hotelms()
# user1.customerData()
# user1.calculateRoomRent()
# 
# user1.restarantBill()
# 
# 
# 
# menu_options = {
    # 1: 'Option 1',
    # 2: 'Option 2',
    # 3: 'Option 3',
    # 4: 'Exit',
# 
    # 
# }