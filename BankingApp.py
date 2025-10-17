pin = 12345
p =int(input("Enter your 5 digit PIN \n"))
infile = open("banking_app_balance.txt","r")
firstline = infile.readline()
balance = infile.readline()
bool(p ==pin)
while (p==pin) is False:
      p = int(input("Wrong pin! Enter your 5 digit pin\n"))
else:
   print("_______________")
   print("Choose option")
   print("")
   print("1.Deposit")
   print("2.Withdraw")
   print("3.Check balance")
   print("4.Exit")
   
   print("_______________")
   option = str(input("Enter your option\n"))
while option :
 while option == "1":
   D = float(input("Enter amount to deposit\n"))
   balance = balance + D
   if D < 0:
      print ("Invalid amount")
   else:
      print ("Your balance is E%.2f"%balance)
   E = str(input("Press 1 to EXIT\n"))
   bool (E == "1")
   while (E == "1") is False:
      E = str(input("Invalid input! Press 1 to Exit\n")) 
   else:
      print("_______________")
      print("Choose option")
      print("")
      print("1.Deposit")
      print("2.Withdraw")
      print("3.Check balance")
      print("4.Exit")
      print("_______________")
      option = str(input("Enter your option\n"))
   
 while option == "2":
   W = float(input("Enter amount to withdraw\n"))
   if W > balance:
      print ("Insufficient funds")
   elif W < 0:
      print ("invalid amount")
   else:
      balance = balance - W
      print ("Your balance is E%.2f"%balance)
   E = str(input("Press 1 to EXIT\n"))
   bool (E == "1")
   while (E == "1") is False:
      E = str(input("Invalid input! Press 1 to Exit\n")) 
   else:
      print("_______________")
      print("Choose option")
      print("")
      print("1.Deposit")
      print("2.Withdraw")
      print("3.Check balance")
      print("4.Exit")
      print("_______________")
      option = str(input("Enter your option\n"))
 while option == "3":
   print ("Your balance is E%.2f"%balance)
   E = str(input("Press 1 to EXIT\n"))
   bool (E == "1")
   while (E == "1") is False:
      E = str(input("Invalid input! Press 1 to Exit\n")) 
   else:
      print("_______________")
      print("Choose option")
      print("")
      print("1.Deposit")
      print("2.Withdraw")
      print("3.Check balance")
      print("4.Exit")
      print("_______________")
      option = str(input("Enter your option\n"))
 if option == "4":
   print ("Thank you. Have a nice day")
 else:
   option = input("Invalid input!Enter your option!\n") 
