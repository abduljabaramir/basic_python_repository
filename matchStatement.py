
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(2))            
#this is the list
var = 3

match var:
    case 1:
        print("this is small")
    case 2:
        print("this is meduim")
    case 3:
        print("this is large")

 #the following example will show x and y axis location
var = (8,0)
match var:
    case (0,x):
        print("the value is on the y axis")
    case (x,0):
        print("the value is on the x axis")
    case (x,y):
        print("the value is not exist on any axis")


#using if statement with match statement as follows

def print_grade(score):
    match score:
        case score if score >=90:
            print("A")
        case score if score >= 80:
            print("B")
        case score if score >= 70:
            print("C")
        case score if score >= 60:
            print("D")
        case score if score >= 50:
            print("just pass")
        case _:
            print("failed")
    
    
print_grade(91)
print_grade(49)


print(5%3*2)
#operator precedence
#()
#**
#*/%
#+-


#write  a python program to print the binary number of any number
print(bin(5))
#write a python program to print the number of related binary 
print(int("101",2))

Amiri = "this is variable"
print(Amiri)


#the following the is example of type conversion in python
print("the type of the value is:" , type(str(100))) #this will print <type str>
print("the type of the value is:",type(int(str(100))))#this will print the vlaue as <type int>


