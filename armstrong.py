def is_armstrong(num):
    n = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    return num == sum


lst = input("Enter a list of numbers separated by spaces: ").split()
lst = [int(x) for x in lst]

for i in range(len(lst)):
    if is_armstrong(lst[i]):
        lst[i] = 1
    else:
        lst[i] = 0

print(lst)
