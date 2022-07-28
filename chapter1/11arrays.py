# declare array
fruits = ["orange", "apple", "banana", "cherry"]

print(fruits, type(fruits))
# access elements in the array
print(fruits[0], type(fruits[0]))
print(fruits[0:2], type(fruits[0:2]))

fruits.append("mango")

for fruit in fruits:
    print(fruit)