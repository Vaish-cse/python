def sort_rows(lst):

    return sorted(lst, key=lambda row: sum(row))

def print_list(lst):

    for row in lst:
        print(" ".join(str(x) for x in row))


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

lst = []
for i in range(rows):
    row = input("Enter the values for row {}: ".format(i+1))
    lst.append([int(x) for x in row.split()])

lst_sorted = sort_rows(lst)
print_list(lst_sorted)
