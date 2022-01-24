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
