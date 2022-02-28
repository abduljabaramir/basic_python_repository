# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



#tuple: are used to store multiple values in a single variable
#in python it is used to store the collection of data
#it is a collection which is ordered and unchangeable
#tuple are written with round brackets
#tuple is like list but unlike list can be modified,they are immutable means not changeable
#following is the simple example of tupel
firstTuple = ("amiri","tamim","maryem","jan")
print(firstTuple)#outpu:('amiri', 'tamim', 'maryem', 'jan')
#tupe item is indexed, first index is [0] and the last index is [n-1]

# #notchangeable concept as follows:
# print(firstTuple[1])#output:tamim
# #if we want to change the vlaue of the 1 index in the tuple it doen't work
# firstTuple[1]="kairm"
# print(firstTuple[1])#output:TypeError: 'tuple' object does not support item assignment

#some example of tuple that was applied to the list
# a,b,c,*rest = (1,2,3,4,5,6,7,8)
# print(a,b,c)#output:1 2 3
# print(rest)#output:[4, 5, 6, 7, 8]

#one item in the tuple is valid if we put a comma after the value as follows
# oneItemTuple  = ("amiri")#this is just string type
# oneItemTuple2 = ("amiri",)#this is tuple type

#methods of Tuple:
#there are two methods of tuple 1:count() and 2:index()
#count():returns the number of times a value has occured
# print(firstTuple.count("maryem"))#it will return the 1
# #index():return the index  of the vlaue
# print(firstTuple.index("maryem"))#it will return 2 means maryem is on index 2

#accessing tuple:
#You can access tuple items by referring to the index number, inside square brackets:
# print(firstTuple[1])#output:tamim
# #negative index means start from the last
# print(firstTuple[-1])#output:jan
# print(firstTuple[-2])#output:maryem
# print(firstTuple[-4])#output:amiri

#range of indexes
# Note: The search will start at index 1 (included) and end at index 5 (not included).
secondTuple = (1,2,3,4,5,6,7,8,9)
# print(secondTuple[1:5])#it will print the 2,3,4,5
# print(secondTuple[::2])#output:(1, 3, 5, 7, 9)
# print(secondTuple[start:end:step])

#range of negative index:
#it will start from the reverse side
#the first index in included and the second index in exluded
# print(secondTuple[-4:-1])#output:(6, 7, 8)

#check if an item exist or not
# if 1 in secondTuple:
#     print("yes the value is exist in the list")


#update tuple
#you better know that the tuple is immutable means not changeable once defined
#if you want to update the vlaus in the tuple first it is converted to the list and then the list converted ot the tuple
# firstList = list(secondTuple)
# print("the following is the original tuple:\n",secondTuple)
# firstList[2]="amiri"
# updated =tuple(firstList)
# print(" the updated tuple :\n",updated)


#add items
#to add items to tuple it is not directly possible so change the tuple to the list and then back change
# updatedList = list(secondTuple)
# updatedList.append("ahadi seb")
# updatedTuple = tuple(updatedList)
# print(updatedTuple)#output:(1, 2, 3, 4, 5, 6, 7, 8, 9, 'ahadi seb')

#add tuple to tuple
# thirdTuple = ("ahadi seb","janjanme")
# secondTuple += thirdTuple
# print(secondTuple)#output:(1, 2, 3, 4, 5, 6, 7, 8, 9, 'ahadi seb', 'janjanme')

#remove item form the tuple
#this is also done as the previouse
# updatelist = list(secondTuple)
# print(secondTuple)
# updatelist.remove(5)
# updatetuple = tuple(updatelist)
# print(updatetuple)

#upacking Tuple
#when we create a tuple we normally assign some values to it this process is called packing
#when we assign the values fo the tuple to the variables this process is called upacking
#example of upacking of tuple as follows
# a,b,c,*rest = ("first","second","third","four","five","six")
# print(a,b,c)#output:first,second,third
# print((rest))#output:four,five,six
# #this is another example
# a,*rest,d = ("first","second","third","four","five","six")
# print(a)
# print(rest)#output:['second', 'third', 'four', 'five']
# print(d)


#Loop tuples
#using for loops
#example
# for x in secondTuple:
#     print(x)

#loops through index

# for i in range(len(secondTuple)):
#     print(secondTuple[i])

#using while loops
# i = 0
# while(i<len(secondTuple)):
#      print(secondTuple[i])
#      i = i+1

#join two tuples
#there for to join two tuple we use + operator
#as follows
# thirTuple = ("amiri","karim","ahadi")
# jointuple = secondTuple + thirTuple
# print(jointuple)#output:(1, 2, 3, 4, 5, 6, 7, 8, 9, 'amiri', 'karim', 'ahadi')

#multiplying two tuples
#to multiply two tuples we must use * keyword
#print(secondTuple*3)#output:(1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9)

