num = int(input("Enter a Number: "))
num1 = 0
num2 = 1

for i in range(num):
    print(num1, end=" ")
    num3 = num1 + num2
    num1 = num2
    num2 = num3
