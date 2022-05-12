def maximum(num1, num2):
    return max(num1, num2)
def maximum2(num1, num2, num3):
    middle = maximum(num1,num2)
    return maximum(middle, num3)
print(maximum2(111,44,57))