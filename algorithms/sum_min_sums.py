# Complete the 'findTotalPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#
MODULO_COEF = 10 ** 9 + 7

def findTotalPower(power):
    min_value = power[0]
    sum_values = [power[0]]
    total_sum = min_value * sum_values[-1]

    for i in range(1, len(power)):
        min_value = min(min_value, power[i])
        curr_sum = power[i] * power[i] + sum(sum_values) * min_value
        sum_values.append(sum(sum_values) + power[i])
        
        total_sum = (total_sum + curr_sum) % MODULO_COEF
    
    return total_sum

def findTotalPowerSlow(power):
    total_sum = 0
    for i in range(len(power)):
        min_power = power[i]
        sum_power = power[i]
        total_sum = (total_sum + min_power * sum_power) % MODULO_COEF
        for j in range(i + 1, len(power)):
            min_power = min(min_power, power[j])
            sum_power += power[j]
            total_sum = (total_sum + min_power * sum_power) % MODULO_COEF
    
    return total_sum
