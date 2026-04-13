# Creating a tuple
ice_cream_flavours = ("vanilla", "chocolate", "butterscotch", "strawberry")
# print("Tuple:", ice_cream_flavours)


# Accessing elements
print("First element:", ice_cream_flavours[0])
print("Second element:", ice_cream_flavours[1])


# Looping through tuple
print("All flavours:")
for flavour in ice_cream_flavours:
    print(flavour)


# Length of tuple
print("Length:", len(ice_cream_flavours))


# Count function
numbers = (1, 2, 2, 3, 4, 2)
print("Count of 2:", numbers.count(2))


# Index function
numbers2 = (10, 20, 30, 20)
print("Index of 20:", numbers2.index(20))


# Mixed data types
mixed = (1, "hello", 3.5, True)
print("Mixed tuple:", mixed)


# Reassigning tuple
numbers3 = (1, 2, 3)
numbers3 = (4, 5, 6)
print("Reassigned tuple:", numbers3)


# Rainbow example
rainbow = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
print("Rainbow:", rainbow)


# RGB Pixel example
pixel = (0.7, 0.1, 0.2)
print("Pixel RGB:", pixel)


# ❌ The following operations are NOT allowed in tuples (will give error)
# ice_cream_flavours[1] = "blackcurrant"
# ice_cream_flavours.append("mango")
# del ice_cream_flavours[1]