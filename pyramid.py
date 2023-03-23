num_rows = int(input("Enter the number of rows: "))

for i in range(1,num_rows+1):
    if i % 2 == 0:
        print(" "*(num_rows-i) + "# "*i)
    else:
        print(" "*(num_rows-i) + "* "*i)
