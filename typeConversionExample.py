born_date = input("what is your born date?")
age = 2022 - int(born_date)
print(f"your age is : {age}")


#the following is the password checker
user_name = input("enter your name?")
user_password = input("enter your password?")
print(f"Hi {user_name} your password is {'*' * len(user_password)}")
