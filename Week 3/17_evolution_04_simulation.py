"""
Evolution Simulation using Binary DNA

Steps:
1. Read DNA from file
2. Convert to list
3. Apply mutation randomly
4. Print final DNA
"""

import random

# Read DNA file
with open("DNA_data.txt", "r") as file:
    dna = list(file.read().strip())


def evolve(dna):
    index = random.randint(0, len(dna) - 1)
    probability = random.randint(1, 100)

    # 1% mutation chance
    if probability == 1:
        if dna[index] == '0':
            dna[index] = '1'
        else:
            dna[index] = '0'


# Apply evolution 10,000 times
for _ in range(10000):
    evolve(dna)

print("Final DNA after evolution:")
print("".join(dna))
