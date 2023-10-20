# FizzBuzz Coding Challenge 🌟

# Objective:
# Your task is to implement a Python function called fizzbuzz that takes a positive integer as an argument and returns a string based on specific conditions. This is a well-known coding problem that assesses basic control flow and logical reasoning skills.

# Requirements:
# Function Name: fizzbuzz
# Input: A single positive integer.
# Output: A string that adheres to the following conditions:
# If the input integer is divisible by both 3 and 5, return "FizzBuzz".
# If the input integer is divisible by 3 but not 5, return "Fizz".
# If the input integer is divisible by 5 but not 3, return "Buzz".
# If the input integer is neither divisible by 3 nor 5, return the integer as a string.


def FizzBuzz(x):
    if x % 3 == 0 and x % 5 ==  0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

if __name__ == '__main__':

    print(FizzBuzz(14))