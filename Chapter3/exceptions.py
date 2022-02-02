# as it stands, this function will result in an error and the program will crash if it is 
# passed the value 0

def divide(num):
    return 42 / num

print(divide(2))
print(divide(12))
# print(divide(0)) this results in an error, cannot divide by 0

# exception handling can be done with try and except statements:

def divide2(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print('Error: Invalid argument.')

# when the code in the try clause causes an error, the program immediately moves to the code
# in the except clause

print(divide2(0)) # this will not result in an error, in fact it will return None

# you can use try blocks outside of a function as well:

try:
    print(divide(2))
    print(divide(10))
    print(divide(0))
    print(divide(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')