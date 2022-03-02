# in python conditional statements tells the compiler to execute some statements which true condition
# there are some type of coditions as follows:

# if statements:these statements are used when the condition become true
a = 10
b = 20
if a > b:
    print("a is greater than b")
if b > a:
    print("b is greater than a")
# in the above statements anyone that true the conditions is executed


# if-else: if the first condition is true the first block is executed if not the second block is executed
if a > b:
    print("first block has run")
else:
    print("the second block has run")

# elif:this type of expression is used for nested if-else like in other programming language
if a > b:
    print("first block")
elif b == a:
    print("second block")
else:
    print("third block")

# short hand if:
if a < b: print("a is lower than b")  # output:a is lower than b

# short-hand if-else
print("a is greater") if a > b else print("b is greater") if b > a else print("both are equal")  # output:b is greater

# combining conditional statements:for this purpose we use some operators like and ,or
# and:this keyword is used to combine the statements if both conditions are true
c = 5
if a < b and c < a:
    print("b is greater than a and b")  # output:b is greater than a and b

# or:this keyword is used if at least one of the condition is true
if a < b or a < c:
    print("a is lower than b")  # output:a is lower than b

# pass:this keyword is used when the if statement does not have content to avoid getting of error
if a > b:
    pass

# an example of conditional statements
is_old = False
is_licenced = True
if is_old:
    print("your are old enough to drive")
elif is_licenced:
    print("now you can drive ")
else:
    print("you are not of age")
print("checked")
