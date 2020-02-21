li = [12,33,434,35,343,434,343,43,434,34343,55]
li = [li[i] for i in range(len(li)) if i not in (0,4,5)]
print(li)

