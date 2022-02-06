"""
You are given an array of integer size n, where n is in range [1, 10^5].
Every consequent subarray has min and max variable.
Find a total sum of difference (max - min) elements in all consequent subarrays.

For instance:
Array: [2, 5, 7]

Possible subarrays sizes: 1, 2 and 3
For size 1 subarrays and (max - min) differences are:
[2] -> 2 - 2 = 0
[5] -> 5 - 5 = 0
[7] -> 7 - 7 = 0

For size 2 subarrays and (max - min) differences are:
[2, 5] -> 5 - 2 = 3
[5, 7] -> 7 - 5 = 2

For size 3 subarrays and (max - min) differences are:
[2, 5, 7] -> 7 - 2 = 5

Result:
0 + 0 + 0 + 3 + 2 + 5 = 10
"""

def calc_min_max_window_diff(input):
    n = len(input)
    if n <= 1:
        return 0

    diff_sum = 0
    min_values = input.copy()
    max_values = input.copy()
    
    for i in range(1, n):
        j = i - 1
        while j >= 0 and min_values[j] > input[i]:
            min_values[j] = input[i]
            j -= 1
        
        j = i - 1
        while j >= 0 and max_values[j] < input[i]:
            max_values[j] = input[i]
            j -= 1
        
        diff_sum += sum([max_values[j] - min_values[j] for j in range(i)])
    
    return diff_sum
