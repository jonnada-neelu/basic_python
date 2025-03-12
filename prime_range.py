"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""

# Prime numbers in range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

def is_prime(num): 
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_primenum(start, end):
    if start > end:  
        print("Error: The starting number should be less than or equal to the ending number.")
        return  
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()  
print_primenum(start, end)
