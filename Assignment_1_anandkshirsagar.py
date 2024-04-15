# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:07:57 2024

@author: Lenovo
"""

# PPHA 30537
# Spring 2024
# Homework 1

# YOUR CANVAS NAME HERE - ANAND KSHIRSAGR
# YOUR CNET ID NAME HERE - anandkshirsagar
# YOUR GITHUB USER NAME HERE- anandksagar

# Due date: Sunday April 14th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

#answer-
#lets select the range of colors as desired objects in the list- 
color_list= ["red","pink","green","blue"]
 
    
# Now,lets use enumerate() function to simultaneously connect the index and the value of each element mentioned in the list
for index, item in enumerate(color_list):
        print(f"The value at position {index} is {item}")

# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

#answer-

# As a first step, lets select the strings to test whether they are palindrome or not 
word_strings = [
    "radar",
    "A man, a plan, a canal, Panama!",
    "Microsoft",
    "This isn't a palindrome"
]

# Iterate through the strings
# we can only understand possible palindromatic nature of the word string when we iterate string within in string
for word_string in word_strings:
# to check whether the given set of strings is palindrome or not- 
# lets create the cleaned string by removing non-alphanumeric characters and convert it to lowercase
# To do that, lets use the string method of isalnum()  
    cleaned_string = ''.join(char.lower() for char in word_string if char.isalnum())
    
    
# now lets Check whether the cleaned string is equal when run in its reverse
# reverse of the character string can be represented by the cleaned_string[::-1]:
    if cleaned_string == cleaned_string[::-1]:
        
        print(f'"{word_string}" is a palindrome.')
    else:
        print(f'"{word_string}" is not a palindrome.')


# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.

available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')

# The given set of vegetables are given as follows:
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']

while True:
    choice = input('Please pick a vegetable I have available: ')
    if choice in available_vegetables:
        print(f"Bon Appetite! Enjoy your favorite vegetable {choice}.")
        break
    else:
        print("Sorry. Please pickup the correct vegetable from the list.")
    
    
# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

#Answer-

# lets concider the various names as list of strings and call that list as list_1 
list_1 = ["Andy", "Brian", "Claire", "anthony", "Joseph", "Brad", "greta", "sam"]

# now , to transform the string objects in to lowercase we will use this code formation
new_list = [word.lower() for word in list_1 if not (word.lower()
                                                    
                                                    
#to filter out those strings that starting with "a" or "b" 
                                                    
.startswith('a') or word.lower().startswith('b'))]

# now, join both code fragments together to transform the string objects in to lowercase will use this code formation and filter out those strings that starting with "a" or "b"
new_list = [word.lower() for word in list_1 if not (word.lower().startswith('a') or word.lower().startswith('b'))]

print(new_list)



# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

#answer-
# given set of short names and long names are as follows-
Short_name = ['IL', 'IN', 'MI', 'WI']
Long_name = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

# lets create the single dictionary comprehension to combine given set of short_names and long_names
#for dictionary comprehension, we use  Short_name as index and Long_for the value
new_dictionary = {Short_name[i]: Long_name[i] for i in range(len(Short_name))}

print(new_dictionary)

###################################################################################################


# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

#answer-
#our given list for the numbers are - start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

# lets concider number_01 is the first number in very tuple and
# lets number_02 be the second numeber in every tuple
#now lets create the function for the summition of the two numebers (tuple)
def sum_classification(number_01, number_02):
   
#now the results of summition of tuples can be concidered as string like- big, just right, small      
    Total = number_01 + number_02

    if Total > 10:
        return "big"
    elif Total == 10:
        return "just right"
    else:
        return "small"

# Apply the function to each tuple and store the results in a new list
result_list = [sum_classification(number_01, number_02) for number_01, number_02 in start_list]

print(result_list)

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()



#answer-
# in given set of code, global variable is 'a' and local variable is 'b' 
#as a part of the rewriting the code, we transfer 'a' to the my_func function as apart of the argument,
# This makes 'a' independant of the global variable. this reduces the complexity of the code and 
#makes it more easy to operate and understand.   
def my_func(a):
    b = 40
    return a + b

x = my_func(10)

# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random

#answer-
  
import random
import string

# Our random password contains upper-case and lower-case letters, numbers, and special characters

# lest Create desirable function-
def generate_password(length, special_characters=True, numbers=True):
    
    # Let's set the length of the password between 8 and 16
    if not 8 <= length <= 16:
        print("Please double check your password length and keep it between 8 and 16 characters.")
        return None
    
    # Let's convert strings by maintaining special characters 
    characters = string.ascii_letters
    if numbers:
        characters += string.digits
    if special_characters:
        characters += "!@#$%^&*"
    
    # The random password we get is:
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

# Demo:
password = generate_password(12, special_characters=True, numbers=True)
print("Random Password:", password)


# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

#answer-
import random
# lets create the class for the movie database-
class Movie_database:
    def __init__(self, anand):
        self.anand= anand
        self.movies = []

    def add_movie(self, Movie_name, Movie_genre, Movie_rating):
        self.movies.append({"name": Movie_name, "genre": Movie_genre, "rating": Movie_rating})

    def what_to_watch(self):
        if not self.movies:
            print("Database contains no movies.So,Add movies!")
            return
        
        chosen_movie = random.choice(self.movies)
        print(f"Tonight's movie watch list', courtesy of {self.anand}:")
        print(f"Movie_name: {chosen_movie['name']}")
        print(f"Movie_genre: {chosen_movie['genre']}")
        print(f"Movie_rating: {chosen_movie['rating']}")

# Creating an instance of the class of movie data base
Movie_database = Movie_database("anand")

# Add following four movies in to our movie database
Movie_database.add_movie("Toy Story", "Animation", 5)
Movie_database.add_movie("Narnia", "fantasy", 4.5)
Movie_database.add_movie("300", "action", 4)
Movie_database.add_movie("40 year old virgin", "comedy", 4.5)

# Call the what_to_watch method to randomly pick a movie to watch
Movie_database.what_to_watch()

