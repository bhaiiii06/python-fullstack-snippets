card=8520                  # Set the ATM card number
pin=1234                   # Set the ATM PIN
balance=10000              # Set the initial account balance
print("Welcome to ATM")    # Display welcome message

entered_card = int(input("Please enter your card number: "))  # Ask user to enter card number
p=int(input("Please enter your PIN: "))                       # Ask user to enter PIN

if entered_card == card and p == pin:                         # Check if card number and PIN are correct
  print("1.check balance,2.check pin,3.withdraw,4.deposit,5.exit")  # Show menu options

choose = int(input("Please choose an option (1-5): "))        # Ask user to choose an option

if choose == 1:                                               # If user chooses 1
    print("Your balance is:", balance)                        # Show account balance

elif choose == 2:                                             # If user chooses 2
    new_pin = int(input("Please enter your new PIN: "))       # Ask for new PIN
    pin = new_pin                                             # Update PIN
    print("Your PIN has been changed successfully.")           # Confirm PIN change

elif choose == 3:                                             # If user chooses 3
    withdraw_amount = int(input("Please enter the amount to withdraw: "))  # Ask for withdrawal amount
    if withdraw_amount <= balance:                            # Check if enough balance
        balance -= withdraw_amount                            # Deduct amount from balance
        print("Please collect your cash. Your new balance is:", balance)  # Show new balance
    else:
        print("wrong option")                                 # Show error if not enough balance

else:
        print("you enter wrong card or pin")                  # Show error for invalid card or PIN