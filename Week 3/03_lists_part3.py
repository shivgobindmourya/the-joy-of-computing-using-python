"""
LISTS PART 3: OPERATIONS

Topics:
- sort()
- reverse()
- Working with string lists
"""

ages = [12, 23, 34, 15, 87, 7, 3, 1]

# Sorting
ages.sort()
print("Ascending:", ages)

# Reverse (Descending)
ages.reverse()
print("Descending:", ages)

# Sorting string list
students = ["arun", "rajesh", "harish", "akanksha"]

students.sort()
print("Sorted students:", students)

# Insert dummy value
students.insert(0, "JOC")
print("After inserting course name:", students)
