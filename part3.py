'''
______
PART 3
______
There are (at least) 6 errors in this code. Fix them so that it runs properly.

'''

#original code starts here
#number1 = input("Enter a number: ")
#number2 = int(input("Enter another number: ")

#print "The sum of your numbers is", number1 + Number2
#print(Seven times your second number is, 7(number2))

number1 = int(input("Enter a number: "))
#missing parentheses and missing int()
number2 = int(input("Enter another number: "))
#missing second end parentheses

print ("The sum of your numbers is", number1 + number2)
#missing parentheses, capitalized N in number2 variable
print ("Seven times your second number is", 7 * number2)
#missing quatation marks, 7(number2) is not correct format for multiplication 