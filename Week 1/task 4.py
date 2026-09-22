import math

if __name__ == '__main__':
    try:
        num = int(input("Enter a non-negative integer to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            fact = math.factorial(num)
            print(f"The factorial of {num} is {fact}")
    except ValueError:
        print("Please enter a valid integer.")
