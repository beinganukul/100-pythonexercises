li = [12,24,33,23,44,56,77,43,55,77,89,64,55]
li = [li[i] for i in range(len(li)) if i<3 or 4<i]
print(li)

