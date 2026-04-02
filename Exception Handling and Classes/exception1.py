x = input("Enter a number: ")
y = input("Enter 2nd number: ")
try:
    z = int(x) / int(y)

except ZeroDivisionError as e:
    print("Division by zero is not possible ")
    z = None

except TypeError as e:
    print("Type Error Exception")
    z = None

#this below code is to find out the type of error occurred
"""except Exception as e:
    print('Exception type:', type(e).__name__)
    z = None"""
#once you found out what error has occurred we use this code

print("Division is: ",z)
