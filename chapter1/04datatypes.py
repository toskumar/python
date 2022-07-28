a = 10
b = 20
c = a+b
print(c, type(c))

a = 10.1
b = 20.1
c = a+b
print(c, type(c))

a = 10
b = 20.1
c = a+b
print(c, type(c))

a = 'hello'
b = 'world'
c = a+b
print(c, type(c))

a = True
b = False
c = a | b
print(c, type(c))
c = a & b
print(c, type(c))

a = [1,2,3]
b = [3,5,6]
c = a+b
print(c, type(c))

a = {1,2,3}
b = {3,4,5}
c = a.union(b) # a|b
print(c, type(c))
c = a.intersection(b) # a&b
print(c, type(c))
c = a-b
print(c, type(c))
c = b-a
print(c, type(c))
c = a^b #symmetric difference
print(c, type(c))


p_xy = (2,3)
p_rgb = (2,3,4)

print(p_xy, p_xy[0])
print(p_rgb, p_rgb[0])
