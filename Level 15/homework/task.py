#This code does not execute properly. Try to figure out why.

def multiply(a, b):
    return(a * b)

#In this simple assignment you are given a number
# and have to make it negative. But maybe the number is already negative?

def make_negative( number ):
    if number > 0:
        return -number
    return number

#Complete the solution so that it reverses the string passed into it.

def sloution(string):
    result = ""
    for i in string:
        result = i + result
    return result

#We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?

def number_to_string(num : int) -> str:
    return str(num)

#Complete the method that takes a boolean value 
# and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

#Your goal is to write a function that removes the first and
# last characters of a string. You're given one parameter, the original string.
#Important: Your function should handle strings of
#any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string

def remove_char(s):
    return s[1:-1]

#Very simple, given a number, find its opposite (additive inverse).

def opposite(number):
    return -number

#Write a function that accepts a non-negative integer 
# n and a string s as parameters, and returns
# a string of s repeated exactly n times.

def repeat_str(repeat, string):
    result = ""
    for i in range(repeat):
        result += string
    return result

#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    count = 0
    for i in sentence:
        if i in "aeiou":
            count += 1
    return count

#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    result =""
    for i in string_:
        if i.lower() not in "aeiou":
            result += i
    return result