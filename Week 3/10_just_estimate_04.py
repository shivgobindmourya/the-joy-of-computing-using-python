"""
JUST ESTIMATE – PART 04
Programming the 10% Trimmed Mean in Python

Steps:
1. Store estimates in list
2. Sort data
3. Remove 10% smallest and largest values
4. Calculate trimmed mean
"""

from statistics import mean
from scipy import stats

# Sample dataset (replace with full dataset if needed)
estimates = [
    100, 120, 150, 150, 150, 170, 175,
    180, 200, 220, 250, 275, 300,
    320, 350, 400, 450, 500, 600,
    720, 1000, 1010, 1500, 1786, 2000
]

# Step 1: Sort the data
estimates.sort()

# Step 2: Calculate 10% trim value
trim_value = int(0.1 * len(estimates))

# Step 3: Remove smallest and largest 10%
trimmed_data = estimates[trim_value : len(estimates) - trim_value]

# Step 4: Calculate trimmed mean manually
manual_trimmed_mean = mean(trimmed_data)

print("Manual 10% Trimmed Mean:", manual_trimmed_mean)

# Using scipy built-in function
scipy_trimmed_mean = stats.trim_mean(estimates, 0.1)

print("Scipy 10% Trimmed Mean:", scipy_trimmed_mean)
