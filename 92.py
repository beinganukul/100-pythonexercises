s = "H1e2l3o5w6o7r8l9d"
s = [s[i] for i in range(len(s)) if i%2 == 0]
print(''.join(s))

