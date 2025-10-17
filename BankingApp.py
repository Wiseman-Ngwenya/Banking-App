from datetime import datetime
import random
import os

class inside_bank:

    def create_account(self):
        try:
            with open("users.txt","x") as infile:
                None
        except FileExistsError:
            username = input("Enter a username to use\n")
            with open("users.txt","r") as users_infile:
                usernames  = users_infile.readlines()
        clean_usernames = []
        for user in usernames:
            clean_username = user.strip()
            clean_usernames.append(clean_username)
        while username in clean_usernames:
            print("Username already exists")
            username = input("Enter a username to use\n")
        else:
            initial_deposit = input("Enter initial deposit\n")
        pin_list = []
        for i in range(5):
            number = random.randint(0,9)
            pin_list.append(number)
        pin = (f"{pin_list[0]}{pin_list[1]}{pin_list[2]}{pin_list[3]}{pin_list[4]}")
        with open("users.txt","a") as new_username_infile:
            new_username_infile.write(f"{username}\n")
        try:
            os.makedirs(f"{username}_folder")
        except FileExistsError:
            None
        with open (f"{username}_folder/credentials.txt","w") as credentials_infile,open(f"{username}_folder/balance.txt","x") as balance_infile:
            credentials_infile.write(f"{username}\t{pin}")
            balance_infile.write(f"{initial_deposit}")
        print(f"You have succesfully built the account.\n.The user's username is {username} and PIN is {pin}")

class customer:
    def __init__(self,username):
        self.username = username
        with open(f"{self.username}_folder/balance.txt","r") as balance_infile:
            self.balance = float(balance_infile.read())

    def deposit(self):
       amount = float(input("Enter amount to deposit\n"))   
       while amount < 0:
          amount = float(input("Invalid amount! re-enter amount\n"))
       else:
          self.balance += amount
          print("")
          print("You have successfully deposited E%.2f"%amount)
          print("")
          self.save_history("deposit",amount)
        
    def withdraw(self):
        amount = float(input("Enter amount to withdraw\n"))
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount < 0:
            print(" Invalid amount!")
        else:
           self.balance -= amount 
           print("")
           print("You have successfully withdrawn E%.2f"%amount)
           print("")
           self.save_history("withdrawal",amount)
          
    def check_balance(self):
        print(f"Your balance is E{self.balance:02}")
        print("")
        e = str(input("Press 1 to EXIT\n"))
        while e != "1":
            e = str(input("Press 1 to Exit\n"))
     
    def save_history(self,transaction,amount):
        history = (f"{transaction},	{amount},	{self.balance},	{datetime.now().replace(microsecond=0)}\n")
        try:
            with open(f"{self.username}_folder/history.txt","x") as history_outfile:
                history_outfile.write(history)
        except FileExistsError:
            with open(f"{self.username}_folder/history.txt","a") as history_outfile:
                history_outfile.write(history)
        e = input("Press 1 to EXIT\n")
        while e != "1":
            e = str(input("Press 1 to EXIT\n"))
      
    def history(self):
        history_list = []
        with open(f"{self.username}_folder/history.txt","r") as history_infile:
            history = history_infile.readlines()    
            
        for line in history:
            clean_line = line.replace("\t"," ")
            history_list.append(clean_line)
        print("Transaction,	Amount,	Balance,	Date,		Time")
        try:
            for i in range(len(history_list)-10,len(history_list)):
                print((history_list[i]).replace(" ","\t"))
        except IndexError:
            for j in range(len(history_list)):
                print((history_list[j]).replace(" ","\t"))
        e = str(input("Press 1 to EXIT\n"))
        while e != "1":
            e = str(input("Press 1 to EXIT\n"))   
    
    def options(self):
        print("")
        print("select option (1 to 4)")
        print("________________")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Show balance")
        print("4.Recent history")
        print("5.Change PIN")
        print("6.Exit")
        print("________________")

    def change_pin(self):
        
        new_pin = input("Enter your new PIN\n")
        new_pin_2 = input("Confirm your new PIN\n")
        while new_pin != new_pin_2:
            print("PIN does not match the first one")
            new_pin = input("RE-Enter your new PIN\n")
            new_pin_2 = input("Confirm your new PIN\n")     
      
        with open(f"{self.username}_folder/credentials.txt","w") as outfile:
            outfile.write(f"{self.username}\t{new_pin}")
        print("You have successfully changed your PIN") 
        print("")           
        e = str(input("Press 1 to EXIT\n"))
        while e != "1":
            e = str(input("Press 1 to EXIT\n"))              
   
    def saving_balance(self):
        with open(f"{self.username}_folder/balance.txt","w") as outfile:
            outfile.write(str(self.balance))
            
    def main(self):
        while True:
            self.options()
            option = input("Enter your option\n")
            if option == "1":
                self.deposit()
            elif option == "2":
                self.withdraw()
            elif option == "3":
                self.check_balance()
            elif option == "4":
                self.history()
            elif option == "5":
                self.change_pin()
            elif option == "6":
                print("Have a nice day!")
                break
            else:
                print("Invalid option")
            self.saving_balance()

            
"""1.Debug the whole program"""
            
            
            
            

            
account = customer("immanuel")
account.main()

