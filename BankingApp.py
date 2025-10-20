from datetime import datetime
import random
import os
import json
import hashlib

class BackEnd:

    def create_account(self):
        try:
            with open("StoredData/users.txt","x") as infile:
                None
        except FileExistsError:
            username = input("Enter a username to use\n")
            with open("StoredData/users.txt","r") as users_infile:
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
        pin = str(random.randint(10000,99999))
        salt = os.urandom(100)
        hashed_pin = hashlib.sha256(salt+pin.encode()).hexdigest()
        

        try:
            os.makedirs(f"StoredData/{username}_folder")
        except FileExistsError:
            None
            
        user_record = {"username":username,
        "pin":hashed_pin,
        "balance":initial_deposit,
        "salt":salt.hex()}
        with open (f"StoredData/{username}_folder/UserInfo.json","w") as info:
            json.dump(user_record,info,indent = 4)
        with open("StoredData/users.txt","a") as new_username_infile:
            new_username_infile.write(f"{username}\n")
        print(f"You have succesfully built the account.\n.The user's username is {username} and PIN is {pin}")

class FrontEnd:
    def __init__(self,username):
        self.username = username
        with open(f"StoredData/{self.username}_folder/UserInfo.json","r") as balance_infile:
            user_info = json.load(balance_infile)
        self.user_info = user_info
        self.balance = float(user_info["balance"])
    def pause(self):
        e = str(input("Press 1 to EXIT\n"))
        while e != "1":
            e = str(input("Press 1 to Exit\n"))
            
    def deposit(self,amount):
       while amount < 0:
          return("Invalid amount! re-enter amount\n")
       else:
          self.balance += amount
          self.saving_balance()
          self.save_history("deposit",amount)
      
          return(f"\nYou have successfully deposited E{amount:.2f}\n")
          
        
    def withdraw(self,amount):
        if amount > self.balance:
            return("Insufficient funds!")
        elif amount < 0:
            return(" Invalid amount!")
        else:
           self.balance -= amount
           self.save_history("withdrawal",amount)
           self.saving_balance()
           return(f"You have successfully withdrawn E{amount:.2f}")
           
          
    def check_balance(self):
        return(f"Your balance is E{self.balance:.2f}\n")

     
    def save_history(self,transaction,amount):
        history = (f"{transaction},	{amount},	{self.balance},	{datetime.now().replace(microsecond=0)}\n")
        try:
            with open(f"StoredData/{self.username}_folder/history.txt","x") as history_outfile:
                history_outfile.write(history)
        except FileExistsError:
            with open(f"StoredData/{self.username}_folder/history.txt","a") as history_outfile:
                history_outfile.write(history)

      
    def history(self):
        history_list = []
        try:
            with open(f"StoredData/{self.username}_folder/history.txt","r") as history_infile:
                history = history_infile.readlines()    
        except FileNotFoundError:
            return("History in not available")
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
        hashed_pin = hashlib.sha256(bytes.fromhex(self.user_info["salt"])+new_pin.encode()).hexdigest()
        self.user_info.update({"pin":hashed_pin})
        with open(f"StoredData/{self.username}_folder/UserInfo.json","w") as outfile:
            json.dump(self.user_info,outfile,indent=4)
        print("You have successfully changed your PIN") 
        print("")                      
   
    def saving_balance(self):
        self.user_info.update({"balance":self.balance})
        with open(f"StoredData/{self.username}_folder/UserInfo.json","w") as outfile:
            json.dump(self.user_info,outfile,indent = 4)
            
    def main(self):
        while True:
            self.options()
            option = input("Enter your option\n")
            if option == "1":
                deposit = float(input("Enter amount to deposit\n"))
                print(self.deposit(deposit))
                self.pause()
            elif option == "2":
                withdrawal = float(input("Enter amount to withdraw\n"))
                print(self.withdraw(withdrawal))
                self.pause()
            elif option == "3":
                print(self.check_balance())
                self.pause()
            elif option == "4":
                print(self.history())
                self.pause()
            elif option == "5":
                self.change_pin()
                self.pause()
            elif option == "6":
                print("Have a nice day!")
                break
            else:
                print("Invalid option")
            

           
