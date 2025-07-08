# Create a class `BankAccount` with:

class BankAccount:
  def __init__(self,account_number,balance=0):
    self.account_number = account_number
    self.balance = balance
  def deposit(self,amount):
    self_balance += amount
    print(f"{amount} deposited succesfully")
  def withdraw(self,amount):
    if self.balance < amount:
      print("insufficient balance")
    else:
      self.balance -= amount
      print(f"{amount} withdrawed succesfully")
  def display_balance(self):
    print(f"Balance for account {self.account_number} is {self.balance}")

# - methods: deposit(amount), withdraw(amount), display_balance()

# Simulate deposit and withdrawal for an object.
accounts = {}
while True:
  print("______BANK ACCOUNT_______")
  print("1. Create Account")
  print("2. Access Account")
  print("3. Exit")

  choice = input("choose an option: ")
  if choice == "1":
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
      print("!!Account already created!!")
    else:
      try:
        balance = float(input("Enter your balance: "))
        accounts[acc_num] = BankAccount(acc_num,balance)
        print("Account created succesfully")
      except:
        print("Invalid balance amount,please enter again")
  elif choice == "2":
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
      account = accounts[acc_num]
      while True:
          print(f"Welcome user number {acc_num}")
          print("***Select the service***")
          print("1  Check balance")
          print("2  Withdraw cash")
          print("3 deposit cash")
          print("4 back to main menu")
          action = input("Choose your service: ")
          if action == "1":
            account.display_balance()
          elif action == "2":
            try:
              amt = float(input("Enter the amount: "))
              account.withdraw(amt)
            except:
              print("Invalid input")
          elif action == "3":
            try:
              amt = float(input("Enter the amount: "))
              account.deposit(amt)
            except:
              print("Invalid input")
          elif action == "4":
            break
      else:
        print("Invalid choice")
    elif choice =="3":
      print("Thanks for using Bank!!")
      break

    else:
      print("Account nummber not found")




