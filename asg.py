# ASSIGNMENT 3

# Q1: write a python program to print the following string in a specific format 
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are''');

# Q2:Write a Python program to get the Python version you are using


# import sys
# print("python version")
# print(sys.version)
# print("version info")
# print(sys.version_info)


# Q3:Write a Python program to display the current date and time.
# import datetime 

# now = datetime.datetime.now();
# print("current date and time:")
# print(now.strftime("%y-%m-%d %H:%M:%S"))


# Q4:Write a Python program which accepts the radius of a circle from the user and compute
# the area
# radius = input("enter radius")
# area = 3.14*radius**2
# print(area)

# Q5:Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

# firstName = input("enter your frist name ");
# lastName = input("enter your lastname");
# print(lastName + firstName)

# Q6:Write a python program which takes two inputs from user and print them addition
# a =input("enter your age ")
# b =input("enter you birthdate")
# print(a+b)


# Q7:Write a program which takes 5 inputs from user for different subject’s marks, total it
#and generate mark sheet using grades ?
# chem = int(input("enter marks chemistry"))
# maths = int(input("enter marks maths"))
# eng = int(input("enter marks english"))
# urdu = int(input("enter marks urdu"))
# phy = int(input("enter marks physics"))
# total = chem + maths + eng + urdu + phy;
# # print(total)
# per =total/ 5;
# print(per)
# if( 90>=80 ){
#     print(per) 
  
#  }elif(per>= 70)  {
#   print("B")
#  }elif(per>=   60)  {
#   print("C")
#  }elif(per >=40)  {
#   print("D")
#  }else{
#   print("fail")
#  }-------------------------------not complete


# Q8:Write a program which take input from user and identify that the given number is even
# or odd?

# number = int(input("Enter a number"))

# if(number % 2)== 0:
#     print("{0} is even number".format(number))
# else:
#     print("{0} is odd number".format(number))


# Q9:Write a program which print the length of the list?
# animals =[ "lion","tiger","cow","goat"]


# for i in range(len(animals)):
#     print(i,animals[i])


# Q10:Write a Python program to sum all the numeric items in a list?
# list = [1,3,25,80,136]
# sum = 0
# for i in list:
#     sum = sum+i
# print("sum of the list  ",sum)

# Q11:Write a Python program to get the largest number from a numeric list.

# l =[]

# n=int(input("Enter the length of the list"))
# for i in range (1,n+1):
#     e= int(input("Enter element"))
#     l.append(e)
# print(l)
# l.sort()
# print("the largest element of a list is",l[n-1])



#Q12: Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i<5:
#      print(i) 


# assignment 4

# Q1:Make a calculator using Python with addition , subtraction ,
# multiplication ,division and power. 

# print("select on operation from perform")
# print("1. ADD")
# print("2. SUBTRACT")
# print("3. MULTIPLY")
# print("4. DIVIDE")

# operation =input()
# if operation == "1":
#     num1 = input("enter first number")
#     num2 = input("enter second number")
#     print("the sum is"+ str(int(num1) +int(num2)))
# elif operation == "2":
#     num1 = input("enter first number")
#     num2 = input("enter second number")
#     print("the sum is" + str(int(num1) -int(num2)))
# elif operation == "3":
#     num1 = input("enter first number")
#     num2 = input("enter second number")
#     print("the sum is"+ str(int(num1) *int(num2)))

# elif operation == "4":
#    num1 = input("enter first number")
#    num2 = input("enter second number")
#    print("the sum is"+ str(int(num1) /int(num2)))

# else:
#  print("invaild")


# Q2:Write a program to check if there is any numeric value in list using for
# loop.

# for i in range(1,10):
#  print(i)

# Q3:Write a Python script to add a key to a dictionary.

# my_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# my_dict["occupation"] = "Engineer"

# print(my_dict)

# Q4:Write a Python program to sum all the numeric items in a dictionary.
# my_dict = {
#     "a": 10,
#     "b": 20,
#     "c": "not a number",
#     "d": 15.5,
#     "e": "another string",
#     "f": 7
# }

# def sum_numeric_values(dictionary):
#     total = 0
#     for value in dictionary.values():
#         if isinstance(value, (int, float)):
#             total += value
#     return total

# total_sum = sum_numeric_values(my_dict)
# print("Sum of numeric values in the dictionary:", total_sum)


# Q5:Write a program to identify duplicate values from list.

# def find_duplicates(lst):
#     duplicates = []
#     seen = set()
    
#     for item in lst:
#         if item in seen:
#             duplicates.append(item)
#         else:
#             seen.add(item)
    
#     return duplicates

# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# duplicate_values = find_duplicates(my_list)

# if len(duplicate_values) > 0:
#     print("Duplicate values in the list:", duplicate_values)
# else:
#     print("No duplicate values found in the list.")

# Q6:Write a Python script to check if a given key already exists in a
# dictionary

def count_numeric_values(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, (int, float)):
#             count += 1
#     return count

# user_list = []

# while True:
#     user_input = input("Enter a value (or 'exit' to finish): ")
    
#     if user_input.lower() == 'exit':
#         break
    
#     try:
#         num_value = int(user_input)
#     except ValueError:
#         try:
#             num_value = float(user_input)
#         except ValueError:
#             num_value = user_input
        
#     user_list.append(num_value)

# numeric_count = count_numeric_values(user_list)

# if numeric_count > 0:
#     print(f"The list contains {numeric_count} numeric value(s).")
# else:
#     print("The list does not contain any numeric values.")

# print("User list:", user_list)