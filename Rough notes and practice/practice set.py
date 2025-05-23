# string basic quetions practice

# Assign a string "hello world" to a variable and print the 6th character.

# s = "hello world"
# print(s[5])
''' #Index:   0 1 2 3 4 5 6 7 8 9 10
              String:  h e l l o   w o r l d
                  so if we have to print the 6 value we have to put 7'''

# Given the string "Python", print the last 3 characters using slicing.


# a = "python"
# print(a[-3:]) #a[-3:] means "from the 3rd-last character to the end".


# Concatenate two strings "Hello" and "World" with a space in between and print it.

# a = "hello"
# b = "world"
# print(a+" "+b)

# Given the string " Hello ", print the string after removing spaces from both ends

# a = " Hello "
# a = a[1:6]
# print(a)

# Given "data", change it to "dAta" using slicing and indexing

# a = "data"
# a = a[0] + "A"+a[2:]
# print(a)

# Create a list with elements [10, 20, 30, 40] and replace the second element with 25.

# a = [10, 20, 30, 40]
# a[2] = 25
# print(a)

# # ccess the last item in the list [1, 2, 3, 4, 5] using negative indexing.

# a = [1, 2, 3, 4, 5]
# print(a[-1])

# Concatenate two lists [1, 2] and [3, 4] into a new list and print it.

# a = [1,2]
# b = [3,4]
# print(a+b)


# Given a tuple (5, 10, 15, 20), print the second and third elements using slicing.

# a = (5,10,15,20)
# print(a[1:3])

#greatest of 4 number

# a =int(input("enter the number"))
# b =int(input("enter the number"))
# c =int(input("enter the number"))
# d =int(input("enter the number"))

# if a>b and  a>c and a>d:
#     print("a is greater",a)
# elif b>c and b>d and b>a :
#     print("b is greater",b)
# elif c>a and c>b and c>d:
#     print("c is greater ",c)
# else:
#     print("d is greater",d)


english =int(input("enter the number"))
maths =int(input("enter the number"))
hindi =int(input("enter the number"))

total_percentage=(100*(english+maths+hindi))/300
if total_percentage>=40 and english>33 and maths>33 and hindi>33:
    print("you are pass, congrotulation",total_percentage)
else:
    print("u are fail")

