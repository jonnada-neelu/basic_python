"""
Write a program that repeatedly adds the digits of a number until the sum is a single digit.

Example
  Input: 9875
  Step 1: 9 + 8 + 7 + 5 = 29
  Step 2: 2 + 9 = 11
  Step 3: 1 + 1 = 2
  Output: 2

"""
# single _ sum

num = int(input("Enter a number: "))
def single_sum(n):
    while n >= 10:  
        n = sum(int(digit) for digit in str(n))
    return n  
result = single_sum(num)
print(f"Output:", result)
