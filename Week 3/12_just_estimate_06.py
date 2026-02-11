"""
Crowd Computing – Plotting Estimates

This program:
1. Takes crowd estimates
2. Applies 10% trimmed mean
3. Calculates mean & median
4. Plots:
   - Trimmed estimates
   - Actual value
   - Mean
   - Median
"""

import matplotlib.pyplot as plt
import statistics

# Sample crowd estimates
estimates = [
    120, 150, 200, 250, 300, 350, 400, 450, 500,
    720, 1000, 1500, 2000, 375, 260, 275, 320, 467,
    180, 220, 300, 280, 330, 360, 390, 410, 430
]

# Step 1: Sort estimates
estimates.sort()

# Step 2: Trim 10% smallest & largest values
trim_value = int(0.1 * len(estimates))
trimmed_estimates = estimates[trim_value: len(estimates) - trim_value]

# Step 3: Calculate statistics
mean_value = statistics.mean(trimmed_estimates)
median_value = statistics.median(trimmed_estimates)
actual_value = 375  # Real number of gems

print("Trimmed Mean:", mean_value)
print("Median:", median_value)

# Step 4: Plotting
y_values = [5] * len(trimmed_estimates)

plt.plot(trimmed_estimates, y_values, "r--", label="Trimmed Estimates")
plt.plot(actual_value, 5, "g^", label="Actual Value")
plt.plot(mean_value, 5, "ro", label="Mean")
plt.plot(median_value, 5, "bs", label="Median")

plt.xlabel("Estimates")
plt.ylabel("Constant Axis")
plt.title("Crowd Estimate Analysis")
plt.legend()
plt.show()
