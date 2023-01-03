# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# user_name_global = input("input username here:")
# def hello_name(user_name):
#     """Greeting users"""
    
    
#     print("\nHello, " + user_name.title() + ".")
# hello_name(user_name_global)



# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# def first_odds():
#                 #GOOD TO GO

#     for odds in range(1,99,2):
#         print(odds)
# first_odds()



#QUESTION 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

# def max_num_in_list():
#     maximum = []
#     for value in range(1,15):
#         maximum.append(value)               #GOOD TO GO
#     print(max(maximum))



# max_num_in_list()




# Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year():
    a_year = input("what year is it?:")
    print(int(a_year))
    a_year = int(a_year)
    if a_year % 400 == 0: 
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True                    #GOOD TO GO
    else:
        return False
print(is_leap_year())


# QUESTION 5 
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

# nums = [2, 3, 4, 5]
# def is_consecutive(num):
   
#     if sorted(num) == num:
#         return True
    
  
#     else:
#         return False
            
# print(is_consecutive(nums))


        






