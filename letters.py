input_str = input("Enter a string with a number and a name: ")
n,name = input_str.split(maxsplit=1)
n = int(n)

result = ""
for i, char in enumerate(name):
    if (i+1) % n == 0:
        result += "z"
    else:
        result += char

print(result)
