num1 = int(input("enter first number: "))
num2 = int(input("emnter second number: "))
num3 = int(input("emnter third number: "))

if (num1>=num2) & (num1>=num3):
    largest = num1

elif (num2>=num1) & (num2>=num3):
    largest = num2

else:
    largest = num3

print("the largest number is", largest)



