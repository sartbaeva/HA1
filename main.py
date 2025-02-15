#Question1 - Write a program myfamily.py and try out the following piece of code.
#myfamily = ("mother", "father", "sister", "brother", "sister")
#print(myfamily)
#1. Use type()to check the type of the object myfamily
#2. Access tuple items sister by using index numbers
#3. Check whether we can add an item me by using the append() method.
#4. Check whether we can remove the item brother by using the pop()
method.myfamily = ("mother", "father", "sister", "brother", "sister")
print(myfamily)

type_of_myfamily = type(myfamily)
print("Type of myfamily:", type_of_myfamily)

print("First sister:", myfamily[2])
print("Second sister:", myfamily[4])

try:
    myfamily.append("me")
except AttributeError as e:
    print("Error:", e)

try:
    myfamily.pop(3)
except AttributeError as e:
    print("Error:", e)

#Q2: Write a program laptop.py and try out the following piece of code.
#laptop = { "brand": "dell", "model": "alienware", "year": 2010 }
#1. Print the brand value of the dictionary
#2. Add new information (key: value)by using a boolean data type as value and home as key: This laptop is at home now, so "home": True
#3. Modify the value of the key year to 2019
laptop = {"brand": "dell", "model": "alienware", "year": 2010}

print("Brand:", laptop["brand"])

laptop["home"] = True

laptop["year"] = 2019

print("Updated laptop dictionary:", laptop)

Q3- Write a program user.py that stores information about a user into a dictionary,user_info = {}
user_info["name"] = input("Enter your name: ")
user_info["age"] = int(input("Enter your age: "))
user_info["email"] = input("Enter your email: ")
user_info["city"] = input("Enter your city: ")

# Displaying user information
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")
