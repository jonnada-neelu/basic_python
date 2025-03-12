# missing number

n = int(input("Enter the total number of expected elements (n): "))
arr = list(map(int, input(f"Enter {n-1} numbers : ").split()))
def find_missing_number(arr, n):
    
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  
    return expected_sum - actual_sum  

missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")
