''' Bank account project with python'''

print("*=*=*"*11)
import datetime
import os


#Bank  Account Holder Names in list
Customer_Names = ['Upender','abhisekh kalyan','john david','pandit','eswar','raju','srinivas','mallika']

# Bank Account holder pins in list 
Customer_pins = ['2529','5491','5587','6369','0834','8099','1899','5189']

# Customer Balance amount
Customer_Balance_amount = [7000,25000,40000,30000,60000,45000,90000,50000]
# Deposit  amount
Deposit_amount = 0
#withdrawal amount
withdrawn_Amount = 0

# Remaing balance Amount
Balance_amount = 0

# counters in Bank
Counter_1 = 1
Counter_2 = 5

now = datetime.datetime.now()

i = 0

# This is a program  displays banking functions as customer choice..

# in this function we are using while function up to true when while is true
while True:
     # os. system("cls") in this

# Below Displays Banking operation for customer
     
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("*-*-*-*-*-*=>=> Welcome to Axis Bank <=<=-*-*-*-*-*-*")
    print("*****************************************************")
    print("**********   Please Select Your choice   ************")
    print("<=<=<=>=>>=> 1. Open a New Bank Account  <=<=<=>=>>=>")
    print("<=<=<=>=>>=> 2. Deposit Cash             <=<=<=>=>>=>")
    print("<=<=<=>=>>=> 3. Withdrawn Cash           <=<=<=>=>>=>")
    print("<=<=<=>=>>=> 4. Balance Enquiry          <=<=<=>=>>=>")
    print("<=<=<=>=>>=> 5. Exit/Quit                <=<=<=>=>>=>")
    print("********** Please Continue Your Banking  ************")

    # This below function works based on  taking of user input...
    user_choice = input("Please select Your choice_number from Main Menu: ")
    # here using if ststement for user choice 

    if user_choice == "1":
        print("Choice Number 1 is selected by User")
        # the line below will take number of customer from the user..
        number_of_customer = eval(input("Number of Customer: "))

        i = i+ number_of_customer
        # the if condition will restrict the number of new account to 5.
        if i > 5:
             print('\n')
             print("Customer Registration exceed reached Or Customer Registration too low")
             i = i - number_of_customer
        else:
            # the while looping will run accoding to the number_of_customer
            while Counter_1 <= i:
                # Thes few lines will take information from the customer and add to the list...
                name = input("Enter the full Name: ")
                Customer_Names.append(name)
                pin = str(input("Please enter the a pin Choices is yours: "))
                Customer_pins.append(pin)
                Deposit_amount = eval(input("Please Enter  the value  of amount to deposit to start an account : "))
                Balance_amount = Balance_amount + Deposit_amount
                Customer_Balance_amount.append(Balance_amount)
                print("\nName=", end=" ")
                print(Customer_Names[Counter_2])
                print("pins=",end=" ")
                print(Customer_pins[Counter_2])
                print("Balance=", end=" ")
                print(Customer_Balance_amount[Counter_2], end=" ")
                print("-/Rs..")
                Counter_1 = Counter_1 + 1
                Counter_2 = Counter_2 + 1
                print("\n Your Name is added to customers system")
                print("Your pin Genrate to customer system ")
                print("your amount is added to Customer system")
                print("----------New Bank Account Opened Successfully----------")
                print("\n")
                print("Your name is avalible on the customers list now: ")
                print(Customer_Names)
                print("\n")
                print("Note! Please Remember The Name and Pin")
                print("=======================================")
                # This is satatement below helps to the user to go back to main menu
        Main_Menu =input("Please press enter a valid key to go back to main menu to perform the another function or exit ...")
    elif user_choice == "3":
        j = 0
        print("choice number 3 is selected by user")
        # this is while loop will prevent the user using the account if the username or pin is wrong..
        while j < 1:
            k = -1
            name = input("Please Enter Your Name: ")
            pin = input("Please Enter the Valid pin: ")
            #  This is while looping will keep the function running when variable k is smaller than the length of the 
            # custeomer_Names list
            while k < len (Customer_Names) - 1:
                k = k+ 1
                # these two if conditions find where both are name and pin matches...
                if name == Customer_Names[k]:
                   if  pin == Customer_pins[k]:
                        j = j + 1
                        # These few statement would show the balance taken from the list
                        print("Your current Balance:", end=" ")
                        print(Customer_Balance_amount[k], end=" ")
                        print("-/Rs\n")
                        Balance_amount = (Customer_Balance_amount[k])
                        # Statement below would tae the amount to withdraw from user...
                        withdrwal = eval(input("Enter the Amount to withdrwan: "))
                        # the if condtion below would look whether the withdraw is grter than the balance not withdrwan
                        if withdrwal > Balance_amount:
                            # this is statement below wold take the adepost from the customer
                            Deposit_amount = eval(input("Please enter the deposit value beacasue your Balance_amount  mention not above engough: "))
                            # this few ststement would like to update the value and show the balance to  user..
                            Balance_amount = Balance_amount + Deposit_amount 
                            print("Your current Balanceis: ", end=" ")
                            print(Balance_amount,end=" ")
                            print("-/Rs\n") #1000-500=500
                            Balance_amount = Balance_amount - withdrwal
                            print("-\n")
                            print("----------Withdrwa Sucessfull!----------")
                            Customer_Balance_amount[k] = Balance_amount
                            print("Your Remaining Balance: ",Balance_amount, end=" ")
                            print("-/Rs\n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            Balance_amount= Balance_amount - withdrwal
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            print("\n")
                            # These few statement would update the values in the list and show it to the customer.
                            print("----Withdraw Successfull!----")
                            Customer_Balance_amount[k] = Balance_amount
                            print("Your Remaing Balance: ", Balance_amount, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                # The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
                # This statement below helps the user to go back to the start of the program (main menu).
        Main_Menu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif user_choice== "2":
        print("Choice number 2 is selected by the customer")
        n = 0
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please Enter Your  name : ")
            pin = input("Please Enter your pin : ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(Customer_Names) - 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name == Customer_Names[k]:
                    if pin == Customer_pins[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(Customer_Balance_amount[k], end=" ")
                        print("-/Rs")
                        Balance_amount= (Customer_Balance_amount[k])
                        # This statement below takes the depositionn from the customer.
                        Deposit_amount = eval(input("Enter the Depost amount  you want to deposit : "))
                        Balance_amount = Balance_amount + Deposit_amount # 1000+500=1500
                        Customer_Balance_amount[k] = Balance_amount
                        print("\n")
                        print("----Cash Deposit Successful!----")
                        print("Your Current Balance: ", Balance_amount, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break   
            # This statement below helps the user to go back to the start of the program (main menu).
        Main_Menu = input("Please press enter key to go back to main menu to perform another function or exit ...")     
    elif user_choice== "4":
        print("Choice number 4 is selected by the user")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(Customer_Names) - 1:
            print("->.Customer =", Customer_Names[k])
            print("->.Balance =", Customer_Balance_amount[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
            # This statement below helps the user to go back to the start of the program (main menu).
        Main_Menu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif user_choice == "5":
        # These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Visit again")
        print("Bye Bye...")
        break

    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        Main_Menu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    
    
    
    
    
   