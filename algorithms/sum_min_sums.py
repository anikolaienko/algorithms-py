# Complete the 'findTotalPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#
MODULO_COEF = 10 ** 9 + 7

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
