# Dictionary Methods
# 1: clear():this method will clear all the value from the dictionary
Dictionary = {
    "name": "amiri",
    "sname": "abamiri",
    "age": 25
}
print(Dictionary)  # output:{'name': 'amiri', 'sname': 'abamiri', 'age': 25}
# print(Dictionary.clear())#output:None
# 2:copy():this method can copy a full copy of the dictionary
# print(Dictionary.copy())#output:{'name': 'amiri', 'sname': 'abamiri', 'age': 25}

# 3:fromkeys():returns the keys with specified values from the dictionary
# print(dict.fromkeys(Dictionary))#output:{'name': None, 'sname': None, 'age': None}

# 4:get():this method will get the value of the corresponding key
# this also return the value of the key existing in the dictionary
# print(Dictionary.get("age"))#outpu:25
# also this method is  used to print the key and value when they are not defined in the dictionary
# in the above dictionary the contact key and value is not defined so to print and add in the dictionary do as follow
# printdict = Dictionary.get("email", "jabar.amiri34@gmail.com")
# print(printdict)  # output:jabar.amiri34@gmail.com
# method of items():this method will return the key-value pairs of the dictionary
# print(Dictionary.items())#output:dict_items([('name', 'amiri'), ('sname', 'abamiri'), ('age', 25)])
# if any change is come in the dictionary the it will update the list
# Dictionary["phone"]=783688228
# print(Dictionary.items())#output:dict_items([('name', 'amiri'), ('sname', 'abamiri'), ('age', 25), ('phone', 783688228)])

# keys(): return the keys of the dictionary
# print(Dictionary.keys())#output:dict_keys(['name', 'sname', 'age'])

# pop():remove the element with specified keys();
# print(Dictionary.pop("age"))#output:25 in case this will delete the age key with associeted vlaue.
# print(Dictionary)


# popitem():remove the last element form the list
# print(Dictionary.popitem())#it will print the ('age', 25) deleted from the dictionary
# print(Dictionary)

# setdefault():this method will set the default value to the key
# print(Dictionary.setdefault("age",0))#output:25 in case if it doesn't have value it will print the default value.
# print(Dictionary.setdefault("email","jabar.amiri34@gmail.com"))#output:jabar.amiri34@gmail.com

# update():insert an item to the dictionary with key-value pair
# Dictionary.update({"email": "abduljabaramiri34@gmail.com"})
# print(Dictionary)#output:{'name': 'amiri', 'sname': 'abamiri', 'age': 25, 'email': 'abduljabaramiri34@gmail.com'}

#values():return the list of all the vlaues from the dictionary
# print(Dictionary.values())#output:dict_values(['amiri', 'abamiri', 25])
