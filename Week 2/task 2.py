# Task 2

def sum_and_average_digits(s):
    digits = [int(char) for char in s if char.isdigit()]
    if not digits:
        return 0, 0
    return sum(digits), sum(digits) / len(digits)

s1 = "ab12c3d4"
s, a = sum_and_average_digits(s1)
print(f"String: {s1}")
print(f"Sum: {s}, Average: {a}")
