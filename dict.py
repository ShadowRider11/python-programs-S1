
dict1 = {"apple": "green", "banana": "yellow"}
dict2 = {"cherry": "red"}

dict1.update(dict2)
print("Updated Dictionary:", dict1)



n = 10
d = dict()
for x in range(1, n + 1):
    d[x] = x * x
print("Dictionary with Squares:", d)



fruits = {"mango": 5, "orange": 8, "grapes": 12}
sum = 0
for i in fruits.values():
    sum = sum + i
print("The sum of values: ", sum)



items = {"pen": 2, "notebook": 3, "eraser": 4}
mul = 1
for i in items.values():
    mul = mul * i
print("Product of values: ", mul)

