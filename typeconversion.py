#there are some function to convert data types to one another
#int():this function is used to convert any data type ot string
#int(vlaue,base):it takes two parameters one is the value and another is the base
#base like two ro octal or ten
value = "10001"
print(int(value,2))#this will convert value on base 2
print(int(value,8))#this will convert value on base 8
print(int(value,10))#this will convert value on base 10

#how to convert string value to float
#float():this function is used to convert the value to float
print("the value in float is :",float(value))

#how to convert integer to string
#the str():function can be used
print("jabar.amiri"+str(34)+"@gmail.com")#printing:jabar.amiri34@gmail.com

#how to convert string to tuple:
#tuple():this function is used:
print(tuple(value))


#how to convert string to set()
#set():this function is used:
print(set(value))

#how to convert string to list:
#list():function is used:
print(list(value))

#how to convert integer to coplex
#complex(): function is used
a = 1
b = 3
print(complex(a,b))


#how to convert complext to integer and float
complex_value = 1+3j
print(abs(complex_value))



#escape sequence
#firt example 
weather = "it's sunny"
print(weather)

#second example
weatheR = "it's\" kind of\"sunny to be now"
print(weatheR)



#formatted string
name = "amiri"
age = 25
#this will print the as follows 
print("hi "+ name +" your "+ str(age) + " years old.")

# there for to print the above statement as string formatted we do as follows
print(f"hi {name} your {age} years old. ")

#the above is also done as follows
print("hi {} your {} years old.".format(name,age))

#the above code is also done as follows
print("hi {new_name} your {new_age} years old.".format(new_name = "amiri",new_age = 25))

string_value = "jabar.amiri34@gmail.com"
print(string_value[0])#printing:j
print(string_value[0:4])#printing:jaba
print(string_value[2:9])#printing:bar.ami
print(string_value[0:11:2])#printing:jbraii
print(string_value[1:])#printing:abar.amiri34@gmail.com
print(string_value[0::2])#printing:jbraii4galcm
print(string_value[:])#printing:jabar.amiri34@gmail.com
print(string_value[::2])#printing:jbraii4galcm
print(string_value[:9])#printing:jabar.ami
#python start with back side by entering the negative index value as follows
print(len(string_value))#printing:23
print(string_value[-1])#printing:m
print(string_value[-2])#printing:o
print(string_value[-23:-1])#printing:jabar.amiri34@gmail.co
print(string_value[-23:])#printing:jabar.amiri34@gmail.com
print(string_value[::-1])#printing:moc.liam@43irima.rabaj


