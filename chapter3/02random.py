import random

#random number between 0 to 1
a = random.random()
print(a)
print(int(a*100))

# random rumber between 1000 to 9999
print(random.randint(1000,9999))

# random number between 0 to 10
print(random.randrange(10))

# random number between 5 to 10, same as randomint
print(random.randrange(5,10))

# random number between 1 to 11 eg., 1,3,5,7,9,11
print(random.randrange(1,11,2))

