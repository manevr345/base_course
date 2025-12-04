def is_device(a, b):
    return(a*3)
a = 2
print(is_device(4, 8))
nums = [24, 34, 67,67, 9]
result = list(map(is_device, nums))
print(result)
num1 = [6, 7,9, 5]
num2 = [5, 6,7,566]
result = list(map(is_device, num1, num2))
print(result)