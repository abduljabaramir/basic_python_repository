#A set is a collection which is unordered, unchangeable*, and unindexed.
#this is used to store multiple data in a single variable
#it is created with curely brackets
#it doesn't allow duplicate vlaue
#example
firstSet = {1,2,3,4,5,6,7,8,9,9,9}
# print(firstSet)#output:{1, 2, 3, 4, 5, 6, 7, 8, 9}


#accessing set item
#it doesn't allow index base
# print(firstSet[0])#output:TypeError: 'set' object is not subscriptable
#you can access the item of the set by using loop
# for check in firstSet:
#     print(check)
#
# print(3 in firstSet)#True

#add items to set
#to add items to set we use the add() method
# firstSet.add("amiri")
# print(firstSet)

#join two sets
#to join two sets we use the update()
# secondset = ("amiri","karim","ahadi")
# firstSet.update(secondset)
# print(firstSet)#output:{1, 2, 3, 4, 5, 6, 7, 8, 9, 'karim', 'ahadi', 'amiri'}


#remove items from the set
#some methods are exist to remove the items from the list
# print(firstSet.remove(2))
# print(firstSet)

# print(firstSet.discard(2))
# print(firstSet)

# print(firstSet.pop())
# print(firstSet)

# print(firstSet.clear())
# print(firstSet)

#join two sets
#there are some methods to do join for two sets
#union():this method return a new set combined from two different sets\
secondset = {1,2,3,4,5,6,7,8,"amiri","hello"}
# setThird = firstSet.union(secondset)
# print(setThird)

#update():this method will insert the values of one set into another set
# firstSet.update(secondset)
# print(firstSet)

#intersection_update():this method returns the values which belongs to both sets but keep in mind that will update the first set
# firstSet.intersection_update(secondset)
# print(firstSet)#output:{1, 2, 3, 4, 5, 6, 7, 8}

#instersection():returns the values exist in the both sets not in one
# print(firstSet.intersection(secondset))
# print(firstSet)#output:{1, 2, 3, 4, 5, 6, 7, 8, 9}

# difference():this method returns the values that exist in the first set and not in the second set
# print(firstSet.difference(secondset))#output:{9}
# print(firstSet)

# difference_update():this method will update the first set with difference values
# print(firstSet.difference_update(secondset))
# print(firstSet)#output:{9}

#isdisjoint():this method will return True if the two sets are not intersected
#like as follows
# print(firstSet.isdisjoint(secondset))#output:False

#for the concept of union() method : | this operator is also used
# print(firstSet|secondset)#output:{1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'amiri'}

#for intersection() method the & operator is used
# print(firstSet & secondset)#output:{1, 2, 3, 4, 5, 6, 7, 8}


#issubset():this method will return true if elements of one set completly exist in another set as follows
# print(firstSet.issubset(secondset))#output:False because all elements in the firstset not exist  in the secondset

thirdset = {1,2,3,4,5}
fourthset = {1,2,3,4,5,6,7,8,9}
#
# #issuperset():this method will reutrn true if the values of one set exist in the another set
# print(fourthset.issuperset(thirdset))#output:True

#symmetric_difference():this method keep only elements that are not exist in both set
# print(thirdset.symmetric_difference(fourthset))#output:{6, 7, 8, 9}

# #symmetric_difference_update():this method will return the values as symmetric_difference but it will update the first set
# print(thirdset.symmetric_difference_update(fourthset))
# print(thirdset)#output:{6, 7, 8, 9}
