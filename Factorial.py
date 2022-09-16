num = int(input("Enter a Number: "))
factorial = 1

if num < 0:
        print("Factorial does't exist for negative numbers!")
        exit()
elif num == 0:
        print("The Factorial of 0 is 1!")
        exit()
else: 
        for i in range(1, num+1):
                factorial = factorial*i

print(f"Factorial of {num} is {factorial}")
