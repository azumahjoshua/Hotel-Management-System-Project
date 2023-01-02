from datetime import date, datetime


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
        # print(totaldayspent.days)
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
            return roomprice*totaldayspent.days
        except:
            print("Room Number must be a integer")


    
        
    # def restarantBill():
        # pass
    # def laundaryBill():
        # pass
    # def gameBill():
        # pass
    # def totalExpenditure():
        # pass

       




# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))


user1 = Hotelms()
user1.customerData()

user1.calculateRoomRent()