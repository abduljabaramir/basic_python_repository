#boolean is one of the most imporatnt data type in python programming language
#used to represent the truth value of the expression
#used in conditional statements and loops
#used in decision making and control flow of the program
#used in data validation and error handling
#used in logical operations and comparisons
#used in data filtering and searching
#used in data analysis and machine learning
#used in data visualization and reporting
#used in data storage and retrieval
#used in data encryption and security
#used in data compression and optimization
#used in data transmission and networking

#scenario: User Login System
# A user enters the following credentials to log in to a system:
username = "admin"
password = "password123"

#questions are the following:

#1. check whether the username is admin or not
is_admin = (username == "admin")
print(is_admin)

#2. check whether the password is correct or not
is_correct_password = (password == "password123")
print(is_correct_password)

#3. check whether the user is logged in successfully
is_logged_in = is_admin and is_correct_password
print(is_logged_in) 

#4. check whether the user is not logged in
is_not_logged_in = not is_logged_in
print(is_not_logged_in)

#5. what boolean value should be returned if only one credential is correct
is_one_credential_correct = is_admin or is_correct_password
print(is_one_credential_correct)

#6. what is the output of the following epxression
print((username == "admin") and (password == "password123")) # True
print((username == "admin") or (password == "password123")) # True

#7. what is the output of the following expression
print(username == "admin")


#scenario: Age Verification System

#Quesionts are the following:

#1. check whether the user is eligible to vote or not
age = 20
is_eligible_to_vote = (age >= 18)
print(is_eligible_to_vote)

#2. check whether the user is a minor or not
is_minor = (age < 18)
print(is_minor)

#3. check whether the user is an adult or not
is_adult = (age >= 18)
print(is_adult)

#4. what happens if the age is 17 ?
age = 17
is_not_elgibile = (age < 18)
print("The person is not eligible for assistance:", is_not_elgibile)


#scenario: ATM withdrawal

#questions are the followings:
balance = 15000
withdraw = 8000
#1.check whether the widrawal is allowed?
eneter_amount = int(input("Enter the amount you want to withdraw"))
def withdraw_amount(amount):
    if amount <= balance:
        print("withdrawal Allowed")
        return True
    else:
        print("Insufficient Balance")
        return False
    
withdraw_amount(eneter_amount)

# the following is based on Boolean based

is_withdrawal_allowed = eneter_amount <= balance
print(" withdrawal is allowed: ", is_withdrawal_allowed)

if is_withdrawal_allowed:
    print("Transaction successfully")
    balance -= eneter_amount
    print("your remaining balance is: ", balance)
else:
    print("Insufficient amount entered")