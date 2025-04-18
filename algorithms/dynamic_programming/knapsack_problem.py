# Knapsack problem: Given a list of weights [w1,w2,...,wn],
# determine all sums that can be constructed using the weights.

def find_all_sums(weights: list[int]) -> int:
    all_sum = sum(weights) + 1
    possible = [[False] * all_sum for _ in range(len(weights) + 1)]
    possible[0][0] = True

    for k, weight in enumerate(weights):
        for pos in range(0, all_sum):
            if pos - weight >= 0:
                possible[k + 1][pos] |= possible[k][pos - weight]
            possible[k + 1][pos] |= possible[k][pos]

    return sum(possible[-1])


def find_all_sums2(weights: list[int]) -> int:
    """Optimized to use 1 dimensional array."""
    n = sum(weights) + 1
    possible = [False] * n
    possible[0] = True

    for weight in weights:
        for x in range(n - 1, -1, -1): # going from right to left
            if possible[x]:
                possible[x + weight] = True

    return sum(possible)


if __name__ == "__main__":
    print(f"Sum: {find_all_sums([1, 3, 3, 5])}")
    print(f"Sum2: {find_all_sums2([1, 3, 3, 5])}")
