
#the print funciton is used to print the out put
print("hello guys this is the first example of python");

#the type() is built-in funciton that return the type of the output as follows
print(type("this is the string type "))

# id() this function uniguely indentify any created object as follows
a = 20
b = a

print(id(a))  
print(id(b))
# the above both function will generate the same object id 


b = 200
# this following line will generate the differ id
print(id(b))

#Multiple assignment
#this can be done into two categories 1:single value to multiple variables
#2: multiple value ot multiple varaibles


#the first one is as follow
x = y = m = 40
print(x)
print(y)
print(m)

#this is the example of multiple assigning  of to multiple variables

a ,b,c = 1,2,3
print("the value of a =",a)
print("the value of b = ",b)
print("the value of c = ",c)
#local variables: are those which are defined inside the function so its scope is within the function
#as follows
 #function definition  
def hello_world():    
    print("hello world")    
# function calling  
hello_world()  
#function definition  
def adding():
    first = 20
    second = 30
    sumOfall = a+b
    print("the sum of a+b = ",sumOfall)
#this is the output of the variables    
adding()

#this is the example of calling parameter from function within python

def returning_parameter():
    valueOf = "this is the returning parameters of the python function"
    return valueOf

print("return value is = ",returning_parameter())

#calling of python function without return statement as well as without parameter will generate 
#none vlaue 
#if the above example if we comment the {return valueOf} statement then it will print the value as none


# how to do arguments in function
#this is done as follows
def HI(id,name,age):
    print("id=",id)
    print("name= ",name)
    print("age = ",age)
HI(1,"bilal",25)

#how to take user input in python
#this is done as follows
# Declare a variable and initialize it  
s_id = input("enter id of the student:")
s_name = input("enter name of the student:")
s_age = input("enter age of the student:")
  
# Global variable in function  
def mainFunction(ID,NAME,AGE): 
    print("student_id:",ID)
    print("student_name:",NAME)
    print("student_age:",AGE)
    
  
mainFunction(s_id,s_name,s_age)  





#data types in python
#1:numeric type:it store integer ,float and complex type of vlaues
#these all are done as follows
def numericType():
    intvalue = 102
    floatvalue = 10.4
    complexvalue = 2.4j
    print(intvalue,type(intvalue))
    print(floatvalue,type(floatvalue))
    print(complexvalue,type(complexvalue))
numericType()   


#sequence type 
#these type can be divided into the following categories
#1:string type 2: list  3:tuple
#1:string: is a sequence of character that are represented within the quotations
#by using single ,double ,and triple quotations
#in python + sign is used for concatenation and * sign is used for repitation
single_quotes = 'this is the single quotes based string'
print(single_quotes)
double_qoutes = "this is double qoutes based string"
print(double_qoutes)
#triple qoutes is used for multi line string as follows
triple_qoutes = '''this is the example of multiline
string in python so super and so needed '''
print(triple_qoutes)
#another example of mulit line string 
another_string = '''first line
second line
third line
fourth line
fifth line
sixth line
'''
print(another_string)
#this is the example of string handling
print(single_quotes[0:4]) #this will print the four first character of the single_qoutes string value
print(single_quotes[3]) #this will print the fourth character of the single_qoutes string value
print(single_quotes + double_qoutes) #this will print the concatenation the single_qoutes and double_qoutes string 
print(single_quotes*3) #this will print the single_qoutes string value triple times




#2:List
#in python list is simillar to array in c but list store differen type of values
#item in the list is separated with comma(,) and enclosed with [] 
#(:) is used for sliceing of the list
list_of_student_record = [1,"amiri","jabar.amiri34@gmail.com",25]
print(list_of_student_record[2:]) #this will print record after the first two value
print(list_of_student_record[3]) #this will print the vlaue in the 3 index
print(list_of_student_record[0:3]) #this will print the vlaue between 0 and 3 index of the list
print(list_of_student_record + list_of_student_record)#this will print the concatenation of both value
print(list_of_student_record*2)#this will print the list twice times


#3:tuple is a sequence type data types
#tuple is similar to the list in many ways
#tuple items is separated with comma and enclosed with () brackets
#tuple is the read-only data structure as we can't modify the value of the size and value of the item

tuple_Of_student_record = (2,"Hamza Amiri","Hamza@gmail.com",25)
print(type(tuple_Of_student_record))#this will print the type of tuple
print(tuple_Of_student_record[2])#this will print vlaue in the 2 index of the tuple
print(tuple_Of_student_record[0:3])#this will print the value of indexes between 0 and 3
print(tuple_Of_student_record[2:])#this will print the values after the 2 index
print(tuple_Of_student_record + tuple_Of_student_record)#this will print the concatenation
print(tuple_Of_student_record * 3)#this will print the tuple triple times

#tuple_Of_student_record[2] = "Hamza33@gmail.com"     this will generate the error




#3:dictionary is an unordered set of key-value pair of items
#it is similar to the associative array or hash table where each key store a specific vlaue
#value is primitive data types whereas value are an arbitrary python object
#items in the dictionary is separated with the comma and enclosed with curley braces{}

_dictionary = {1:"hemat",2:"amiri",3:"ahadi",4:24}
print(_dictionary) #this will print the all items of the dictionary
print(_dictionary[2])#this will print the ahadi
print("the first name is:"+_dictionary[1])
print("the second name is:"+ _dictionary[2])
print(_dictionary.keys())#this will print the key values of the dictionary
print(_dictionary.values())#this will print the values of the dictionary



