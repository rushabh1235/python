# p = float(input("Enter Original amount : "))
# np = float(input("Enter net price : "))
 
# # Calculating GST amount
# GST_amount = np - p
 
# # Calculating GST percentage
# GST_percent = ((GST_amount * 100) / p)
# print("GST = ",end='') 
   
# print(round(GST_percent),end='') 
# print("%")

# a=['e','r',None,'']
# for i in a:
#     if i==None or '':
#         continue
#     else:
#         print(i)  

# a=['y','y','y','y','n','n','y','n']
# for i,val in enumerate(a):
#     if val=='n':
#         print(i)
# print(a.count('n'))

# def sub(n):
#     l=[]
#     for i in range(n):
#         n=input("enter marks \n") 
#         l.append(n)
#     return l
           
# input("enter student name\n")    
# print(sub(int(input("enter total subjects\n"))))


# import random
# import sys
# class ATM():
#     def __init__(self, name, account_number, balance = 0):
#         self.name = name
#         self.account_number = account_number
#         self.balance = balance
#     def account_detail(self):
#         print("\nACCOUNT DETAIL")
#         print(f"Account Holder: {self.name.upper()}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Available balance: Nu.{self.balance}\n")
#     def deposit(self, amount):
#         self.amount = amount
#         self.balance = self.balance + self.amount
#         print("Current account balance: Nu.", self.balance)
#         print()
#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount > self.balance:
#             print("Insufficient fund!")
#             print(f"Your balance is Nu.{self.balance} only.")
#             print("Try with lesser amount than balance.")
#             print()
#         else:
#             self.balance = self.balance - self.amount
#             print(f"Nu.{amount} withdrawal successful!")
#             print("Current account balance: Nu.", self.balance)
#             print()
#     def check_balance(self):
#         print("Available balance: Nu.", self.balance)
#         print()
#     def transaction(self):
#         print("""
#             TRANSACTION 
#             Menu:
#             1. Account Detail
#             2. Check Balance
#             3. Deposit
#             4. Withdraw
#             5. Exit
#         """)
#         while True:
#             option = int(input("Enter 1, 2, 3, 4, 5:"))
#             if option<=6:
#             # except:
#             #     print("Error: Enter 1, 2, 3, 4, 5 only!\n")
#             #     continue
#             # else:
#                 if option == 1:
#                     atm.account_detail()
#                 elif option == 2:
#                     atm.check_balance()
#                 elif option == 3:
#                     amount = int(input("How much you want to deposit(Nu.):"))
#                     atm.deposit(amount)
#                 elif option == 4:
#                     amount = int(input("How much you want to withdraw(Nu.):"))
#                     atm.withdraw(amount)
#                 elif option == 5:
#                     print(f"""
#                 printing receipt
#               Transaction is now complete.                         
#               Account holder: {self.name.upper()}                  
#               Account number: {self.account_number}                
#               Available balance: Nu.{self.balance}                    
#           """)
#                     sys.exit()
#             else:
#                 print("enter valid no")
# print("ACCOUNT")
# name = input("Enter your name: ")
# account_number = input("Enter your account number: ")
# print("Congratulations! Account created successfully\n")
# atm = ATM(name, account_number)
# while True:
#     trans = input("Do you want to do any transaction?(y/n):")
#     if trans == "y":
#         atm.transaction()
#     elif trans == "n":
#         print("thank you")
#         break
#     else:
#         print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")