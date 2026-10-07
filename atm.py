acc_amount = 500000
pin = "2828"

while  True:
  print("---------------------------------------------")
  print("                 CHECK MENU                  ")
  print("=============================================")
  print("1.Check amount")
  print("2.Withdraw amount")
  print("3.Deposite amount")
  print("4.Exit")
  print("==============================================")

  choice = int(input("Enter what you wanna do?"))
  ypin = input("Enter your pin: ")
  if ypin == pin:


 # check amount
   if choice == 1:
     print(f"This is your account amount {acc_amount}")



  # withdraw amount
   elif choice ==2 :


     w_amount = int(input("Enter how much amount you want to withdraw"))
     if w_amount > acc_amount  :
       print("sorry you dont have that much money")

     elif w_amount<0:
       print("sorry you can't enter any value in minus")

     else :
       acc_amount -= w_amount
       print(f"ok collect your cash: {w_amount}")
       print(f"and this is your amount {acc_amount}")




 # deposite amount
   elif choice == 3:
     add_amount = int(input("Enter how much money you wanna deposite"))
     acc_amount += add_amount
     print(f"ok your amount have been deposite and now this is your total amount {acc_amount}")


  # exit
   elif  choice == 4:
     print("Existing from the sytem")
     break


  else:
   print("sorry your pin is not correct try again") 