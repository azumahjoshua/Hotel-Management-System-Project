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
    user_name =''
    user_address=''
    checkindate = ''
    checkoutdate = ''
    dayspent = 0
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
        # checking out date should be greater than checking in date
        if(self.checkindate > self.checkoutdate):
            print("Error inputing Date: Checking out should be greater than checking in")
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

            return roomprice*totaldayspent
        except:
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
            
            return choosenitem['price']
            # print(choosenitem['price'])
        except IndexError:
            print("Index not found")
        


    # def laundaryBill():
        # pass
    # def gameBill():
        # pass
    def totalExpenditure(self):
        return self.calculateRoomRent() + self.restaurantBill()

       




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