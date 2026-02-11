"""
File Handling Demo for Evolution Simulation
"""

# Read file
with open("sample_dna.txt", "r") as file:
    content = file.read()
    print("Original Content:")
    print(content)

# Write file (append mode)
with open("sample_dna.txt", "a") as file:
    file.write("\nMutation Occurred")

print("Data appended successfully.")
