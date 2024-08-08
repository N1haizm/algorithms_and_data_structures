def factorial(num):
    # Edge case - Exit Condition
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(6))