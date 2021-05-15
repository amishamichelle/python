def reversel(lst):
    return lst[::-1]
# creating an empty list
lst = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
	ele = int(input("Enter the element: "))
	lst.append(ele) # adding the element	
print(lst)

print(reversel(lst))
