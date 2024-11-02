a,b,c =[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

c=list(c)
popped_value = c.pop()
c.append(40)
c=tuple(c)
d = a, b, c

print(list(d))
