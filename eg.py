import numpy as np
from scipy import stats

# Step 1: Create a NumPy array
data = np.array([12, 45, 67, 23, 45, 89, 45, 67, 23, 89])
print("Original Data:", data)

# Step 2: Calculate basic statistics using NumPy
mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)

# Step 3: Use SciPy to calculate the mode
mode_result = stats.mode(data, keepdims=True)
print("Mode:", mode_result.mode[0])

# Step 4: Control Statements
print("\nValues greater than the mean:")

# Using a for loop with conditionals
for value in data:
    if value > mean_val:
        print(f"{value} is above average")
    elif value == mean_val:
        print(f"{value} is equal to the average")
    else:
        print(f"{value} is below average")

# Step 5: Using while loop to find and print even numbers
print("\nEven numbers in data using while loop:")
i = 0
while i < len(data):
    if data[i] % 2 == 0:
        print(f"{data[i]} is even")
    i += 1
