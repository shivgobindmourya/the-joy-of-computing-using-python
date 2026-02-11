"""
LISTS PART 1: INTRODUCTION

Topics Covered:
- Creating list
- Printing list
- Iterating using loop
- append()
"""

# Creating a list
shopping = ["bread", "coffee", "sugar"]

# Printing full list
print(shopping)

# Printing one by one (human readable format)
for item in shopping:
    print(item)

# Adding element at end
shopping.append("curd")

print("After append:")
print(shopping)