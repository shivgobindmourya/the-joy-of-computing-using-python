"""
LISTS PART 2: MANIPULATION

Topics:
- Indexing
- insert()
- count()
- len()
"""

shopping = ["bread", "coffee", "sugar", "curd"]

# Indexing
print("First item:", shopping[0])
print("Second item:", shopping[1])

# Insert at specific position
shopping.insert(1, "oil")
print("After insert:", shopping)

# Count occurrences
ages = [12, 23, 12, 25, 23, 25, 12]

print("Count of 12:", ages.count(12))

# Length of list
print("Length of ages list:", len(ages))
