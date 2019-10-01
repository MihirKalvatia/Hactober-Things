limit=int(input("ENTER THE LIST LIMIT: "))
list_unsorted=[]
for i in range(limit):
    element=int(input("ENTER THE LIST ELEMENT: "))
    list_unsorted.append(element)

list_sorted=[]
for i in range(limit):
    minimum=min(list_unsorted)
    list_unsorted.remove(minimum)
    list_sorted.append(minimum)
print(list_sorted)
