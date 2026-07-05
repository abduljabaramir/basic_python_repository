# string is the collection of characters in python. it is a sequence of characters
#string is immutable in python. it means we can not change the string after creating it
#sliciing string is the process of extracting a part of the string from the original string
#example : get the charactors from position 2 to 5 from the string "python"
string = "Thisispythonstring"
print(string[2:5]) #output is "is " 5 isnt included in the output and the process starts from 2nd position  
#example : By leaving the start index blank, the slice will start from the beginning of the string
string = "Thisispythonstring "
print(string[:5]) #output is "Thisi" 5 isnt included in the output  
#slice to the end of the string by leaving the end index blank
string = "Thisispythonstring"   
print(string[2:]) #output is "sispythonstring" 2 is included in the output and the process starts from 2nd position  
# slicing with negative index -5 and -2 will return the characters from the 5th last to the 2nd last character of the string 
string = "Thisispythonstring"
print(string[-5:-2]) #output is "python" -5 is included and -2 is not included in the output
# the output of the above example is "tri" because the process starts from -5 and ends at -2 but -2 is not included in the output   
#what is the output of the following example
x = "Welcome"
print(x[3:5]) #output is "co" 3 is included and 5 is not included in the output

##Employee ID Exraction using slicing with step

#Scenario: Slicing with step
#you work for a company where every employee ID starts with EMP followed by a number. You have a list of employee IDs and you want to extract the numeric part of each ID using slicing with a step. The employee IDs are stored in a string, and you need to print only the numeric parts.
employee_ids = "EMP20250145"
#Questions are following:
#1. extract only the employee code( EMP )
print (employee_ids[:3]) #output is "EMP" 3 is not included in the output
#2. extract only the employee number( 20250145 )
print (employee_ids[3:11]) #output is "20250145" 3 is included and 11 is not included in the output
#3. extract the employee number in reverse order ( 54102502 )
print (employee_ids[10:2:-1]) #output is "54102502" 10 is included and 2 is not included in the output
#4. extract every second digit of the employee number ( 2505 )
print (employee_ids[3:11:2]) #output is "2505" 3 is included and 11 is not included in the output
#5. extract the employee number from the 3rd digit to the 7th digit
print (employee_ids[2:7]) #output is "02501" 2 is included and 7 is not included in the output
#6.extract the last four digits of the employee number ( 0145 )
print (employee_ids[7:11]) #output is "0145" 7 is included and 11 is not included in the output
#7. extract the employee number in reverse order with a step of 2 ( 5402 )
print (employee_ids[10:2:-2]) #output is "5402" 10 is included and 2 is not included in the output
#8. extract the employee ID in reverse order ( 54102502PME )
print (employee_ids[::-1]) #output is "54102502PME" 10 is included and 2 is not included in the output
#9. what is the out put of the following example
print (employee_ids[-4:]) #output is "0145" -4 is included and the process starts from -4 to the end of the string


##Scenario: Email Processing using slicing with step
# A user enter the following email address "abdul.amiri@gmail.com"

#Questions are following:

#1. extract the username from the email address ( abdul.amiri )
email_address = "abdul.amiri@gmail.com"
print(email_address[:11]) #output is "abdul.amiri" 11 is not included in the output
#2. extract the domain from the email address ( gmail.com )
print(email_address[12:21]) #output is "gmail.com" 12 is included and 21 is not included in the output
#3. extract the username in reverse order ( irima.ludba )
print(email_address[10::-1]) #output is "irima.ludba"
#4. extract the domain in reverse order ( moc.liamg )
print(email_address[20:11:-1]) #output is "moc.liamg"
#5. extract the extension of the email address ( com )
print(email_address[18:21]) #output is "com" 18 is included and 21 is not included in the output
#6. print everything before the @ symbol ( abdul.amiri )
print(email_address[:11]) #output is "abdul.amiri" 11 is not included in the output
#7. print everything after the @ symbol ( gmail.com )
print(email_address[12:21]) #output is "gmail.com" 12 is included and 21 is not included in the output

##Scenario: website URL processing using slicing with step
# A user enters the following website URL "https://www.python.org"

#Questions are following:

#1. extract the protocol from the URL ( https )
url = "https://www.python.org"
print(url[0:5]) #output is "https" 0 is included and 5 is not included in the output
#2. extract the domain name from the URL ( www.python.org )
print(url[8:22]) #output is "www.python.org" 8 is included
#3. extract the top-level domain from the URL ( org )
print(url[19:22]) #output is "org" 19 is included and
#4. extract the domain name in reverse order ( gro.nohtyp.www )
print(url[21:7:-1]) #output is "gro.nohtyp.www"
#5. extract the protocol in reverse order ( sptth )
print(url[4::-1]) #output is "sptth"
#6. what is the output of the following example
print(url[8:22]) #output is "www.python.org" 8 is included and 22 is not included in the output

##Scenario: Date Processing using slicing with step
# A system stores dates in the format "YYYY-MM-DD". You have a date string and you want to extract the year, month, and day using slicing with a step. The date string is stored in a variable, and you need to print the year, month, and day separately.
date_string = "2024-06-15"
#Questions are following:   

#1. extract the year from the date string ( 2024 )
print(date_string[:4]) #output is "2024" 4 is not included in the output
#2. extract the month from the date string ( 06 )
print(date_string[5:7]) #output is "06" 5 is included and 7 is not included in the output
#3. extract the day from the date string ( 15 )
print(date_string[8:10]) #output is "15" 8 is included and 10 is not included in the output
#4. extract the year in reverse order ( 4202 )
print(date_string[3::-1]) #output is "4202" 3 is included and the process starts from 3 to 0
#5. extract the month in reverse order ( 60 )
print(date_string[6:4:-1]) #output is "60" 6 is included and 4 is not included in the output


##Scenario: Product Code Processing using slicing with step
# An online shopping platform stores codes like this
product_code = "LAPTOP-HP-2025"
#Questions are following:

#1. extract the product type from the code ( LAPTOP )
print(product_code[:6]) #output is "LAPTOP" 6 is not included in the output
#2. extract the brand from the code ( HP )
print(product_code[7:9]) #output is "HP" 7 is included and 9 is not included in the output
#3. extract the year from the code ( 2025 )
print(product_code[10:14]) #output is "2025" 10 is included and 14 is not included in the output
#4. extract the product type in reverse order ( POTPAL )
print(product_code[5::-1]) #output is "POTPAL" 5 is included and the process starts from 5 to 0 

#string Manipulation in python
#upper() method is used to convert the string into upper case
string = "this is python string"
print(string.upper()) #output is "THIS IS PYTHON STRING"
#lower() method is used to convert the string into lower case
string = "THIS IS PYTHON STRING"
print(string.lower()) #output is "this is python string"
#remove() method is used to remove the whitespace from the string
string = "   this is python string   " 
print(string.strip()) #output is "this is python string"
#replace() method is used to replace the character in the string
string = "this is python string"
print(string.replace("python", "java")) #output is "this is java string"    
#find() method is used to find the character in the string
string = "this is python string"
print(string.find("python")) #output is 8
#count() method is used to count the occurrence of a character in the string
string = "this is python string"
print(string.count("python")) #output is 1 
#split() method is used to split the string into a list of substrings
string = "this is python string"
print(string.split()) #output is ['this', 'is', 'python', 'string'] 
#concat method is used to concatenate two strings
string1 = "this is python string"
string2 = " and this is java string"
print(string1 + string2) #output is "this is python string and this is java string" 
#formate string is used to format the string
name = "Amiri"
age = 25
print("My name is {} and I am {} years old.".format(name, age)) #output is "My name is Amiri and I am 25 years old."    
#format() method is used to format the string with positional arguments
name = "Amiri"
age = 25
print("My name is {0} and I am {1} years old.".format(name, age)) #output is "My name is Amiri and I am 25 years old."      
#f-string is used to format the string with variables
name = "Amiri"
age = 25
print(f"My name is {name} and I am {age} years old.") #output is "My name is Amiri and I am 25 years old."  
#placeholder is used to format the string with variables
name = "Amiri"
age = 25
print("My name is %s and I am %d years old." % (name, age)) #output is "My name is Amiri and I am 25 years old."    
#modifier is used to format the string with variables
name = "Amiri"
age = 25
result = f"My name is {name} and I am {age} years old."
print(result) #output is "My name is Amiri and I am 25 years old"

txt = f"The price is {20 * 59} dollars"
print(txt)

#escape character is used to escape the special characters in the string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#string Methods in python
#1:capitalize() method is used to capitalize the first character of the string
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x) #output is "Hello, and welcome to my world."
#2:casefold() method is used to convert the string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x) #output is "hello, and welcome to my world."   
#3:center() method is used to center the string
txt = "banana"
x = txt.center(20)
print(x) #output is "       banana       "
#4:count() method is used to count the occurrence of a character in the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) #output is 2
#5:encode() method is used to encode the string into bytes
txt = "My name is Amiri"
x = txt.encode()
print(x) #output is b'My name is Amiri'
#6:endswith() method is used to check if the string ends with a specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) #output is True
#7:expandtabs() method is used to set the tab size of the string
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x) #output is "H  e  l  l  o"
#8:find() method is used to find the first occurrence of a specified value
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) #output is 7   
#9:format() method is used to format the string
txt = "For only {price:.2f} dollars!"
x = txt.format(price = 49)
print(x) #output is "For only 49.00 dollars!"
#10:format_map() method is used to format the string using a dictionary
txt = "My name is {name}, I am {age} years old."
my_dict = {"name": "Amiri", "age": 25}
x = txt.format_map(my_dict)
print(x) #output is "My name is Amiri, I am 25 years old."
#11: index() method is used to find the first occurrence of a specified value
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) #output is 7   
#12:isalnum() method is used to check if all the characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x) #output is True
#13: isalpha() method is used to check if all the characters in the string are alphabetic
txt = "CompanyX"
x = txt.isalpha()
print(x) #output is True
#14: isdecimal() method is used to check if all the characters in the string are decimal
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x) #output is True
#15: isdigit() method is used to check if all the characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x) #output is True
#16: isidentifier() method is used to check if the string is a valid identifier
txt = "Demo"
x = txt.isidentifier()
print(x) #output is True
#17: islower() method is used to check if all the characters in the string are lowercase
txt = "hello world!"
x = txt.islower()
print(x) #output is True
#18: isnumeric() method is used to check if all the characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x) #output is True
#19: isprintable() method is used to check if all the characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) #output is True
#20: isspace() method is used to check if all the characters in the string are whitespace
txt = "   "
x = txt.isspace()
print(x) #output is True
#21: istitle() method is used to check if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) #output is True
#22: isupper() method is used to check if all the characters in the string are uppercase
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) #output is True
#23: join() method is used to join the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) #output is "John#Peter#Vicky"
#24: ljust() method is used to left justify the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") #output is "banana               is my favorite fruit
#25: lower() method is used to convert the string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x) #output is "hello my friends"
#26: lstrip() method is used to remove the whitespace from the left side of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite") #output is "of all fruits banana      is my favorite
#27: partition() method is used to split the string into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) #output is ("I could eat ", "bananas", " all day")



#Testing with the follwing questions:
passport = "AFG-P-2026-987654"


print(passport[:3]) #output is "AFG" 3 is not included in the output
print(passport[4:5]) #output is "P" 4 is included and 5 is not included in the output
print(passport[6:10]) #output is "2026" 6 is included and 10 is not included in the output
print(passport[11:]) #output is "987654" 11 is included and
print(passport[-4:]) #output is "7654" -4 is included and the process starts from -4 to the end of the string
print(passport[-6::-1]) #output is "456789" -6 is included and the process starts from -6 to the end of the string
print(passport[::-1]) #output is "456789-6202-P-GFA" -1 is included and the process starts from -1 to the end of the string
print(passport[:-6]) #output is "AFG-P-2026" -6 is not included and the process starts from 0 to -6
#extract every second character from the passport number
print(passport[::2]) #output is "AG-P0-9754"
#what s the output of the following example
print(passport[-6:-2]) #output is "9876" -6 is included and -2 is not included in the output
