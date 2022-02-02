#loops are use to avoid coding again and again
#loops are used for code re-usability
#we can traverse the elements in the list ,dictionary,array or etc
#there are three types of the loops
#1:for loop: when iteration is finit,it is called per-tested loop
#2:while loop: when the iteration of the pre-tested loop
#3:do while loop: executes at least one when the execution of the program is not finit

#string base loop 
string_traverse = "abduljabaramiri"
for find in string_traverse:
    print(find)

sequence_numbers = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in sequence_numbers:
    c = n*i 
   # print(c)
#the following program will print the sum of the above list 

listofvalue = [20,30,40,50,60]
sum  = 0
for sumoflist in listofvalue:
    sum = sum + sumoflist

print(sum)    
   
#function of range()
#this function is used to generate the sequence of the numbers
#in this fucntion the iteration will go utill the n-1 
#example
_Number = int(input("enter the number:"))
for multiplication in range(1,11,2):
    print(_Number,"*",multiplication,"=",_Number*multiplication)

#raange() is also used with sequence type of numbers
#the following example will print the _dictionary list
_dictionary_example = ["amiri","ahadi","karimullah","himmat"]
print("the following are the names of the dictionary have placed ")
for i in range(len(_dictionary_example)):
    
    print(i+1,"=",_dictionary_example[i],end =" ")

#the following is the example of python inner for loop
print("the following is the example of inner for loop in python")
for i in range(6):
    for j in range(i):
        print("*",end ="")
    print()     


#this is the example of pyramid
rows = int(input("enter the rows"))
for i in range(rows+1):
    for j in range(i):
        print(i,end="")
    print()        


#following is the example of while loop
#to print the letter of the following string without the a and t

stringjava = "javatpoint"
i = 0
while i < len(stringjava):
    if stringjava[i] == 'a' or stringjava == 't':
        i+=1
        continue
    print(stringjava[i],end="")
    i+=1
#this is the example of while loop that print the 
#table of the ten numbers with any user inpute
i = 1
entervalue = int(input("enter any number:"))

while i < (entervalue+1):
    print("%dX%d = %d"%(entervalue,i,entervalue*i))
    i += 1



#this is the matching program
list = [1,2,3,4,5,6,7,8]
for i in list:
    if i == 4:
        print("item found in :%d"%i,"position")


#continue keyword using
stringsearch = "python"

for i in stringsearch:
    if i == "o":
        continue
    print(i)


#this is the example of the nested while loop
n = 2
while 1:
    
    i = 1
    while i <= 10:
         print("%dX%d = %d"%(n,i,n*i))
         i += 1;
    choice = int(input("do you want to go zero for stoping"))
    if choice == 0:
        break
    n = n+1


    #pass statement 
#this is the statement which is used that required syntictically 
#but prograg does not execute any command or action
#as follows
for item in "jabar.amiri34@gmail.com":
    if item == '@':
        pass
        print("this is pass block")
    print("current letter is:",item)
print("ok this is the end of the program")    


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
http_error(404)            
            