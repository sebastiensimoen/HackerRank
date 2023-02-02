# ------------ Day 0: Mean, Median, and Mode ------------

# Read the number of elements in the array
array_length = int(input().strip())

# Read the elements of the array separated by spaces
array_elements = list(map(int, input().strip().split()))

# Calculate the mean of the array elements
array_mean = sum(array_elements) / array_length
print(array_mean)

# Calculate the median of the array elements
sorted_elements = sorted(array_elements)
if array_length % 2 == 0:
    median = (sorted_elements[array_length // 2 - 1] + sorted_elements[array_length // 2]) / 2
else:
    median = sorted_elements[array_length // 2]
print(median)

# Calculate the mode of the array elements
counts = {}
for element in array_elements:
    if element in counts:
        counts[element] += 1
    else:
        counts[element] = 1

max_frequency = max(counts.values())
mode = min([key for key in counts if counts[key] == max_frequency])
print(mode)

### WITH STATISTIC ###
import statistics

# Read the number of elements in the array
array_length = int(input().strip())

# Read the elements of the array separated by spaces
array_elements = list(map(int, input().strip().split()))

# Calculate the mean of the array elements
array_mean = statistics.mean(array_elements)
print(array_mean)

# Calculate the median of the array elements
array_median = statistics.median(array_elements)
print(array_median)

# Calculate the mode of the array elements
array_mode = statistics.mode(sorted(array_elements))
print(array_mode)
