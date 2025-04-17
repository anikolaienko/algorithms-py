def count_coins_recursive(n: int, coins: list[int]) -> int:
    memory = [-1] * (n + 1)
    return _count_coins_recursive(n, coins, memory)


def _count_coins_recursive(n: int, coins: list[int], memory: list[int]):
    if n < 0:
        return float("inf")
    if n == 0:
        return 0
    if memory[n] != -1:
        return memory[n]
    
    best = float("inf")
    for c in coins:
        best = min(best, _count_coins_recursive(n - c, coins, memory) + 1)

    memory[n] = best
    return best


if __name__ == "__main__":
    print(f"Coins count: {count_coins_recursive(10, [1,3,4])}")
