
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
