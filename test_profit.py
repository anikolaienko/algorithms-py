import typing
from collections import deque


def solution(prices: typing.List[float], trades: typing.List[typing.List[int]]) -> float:
    shares_held = deque()
    profit = 0

    for trade in trades:
        is_purchase = trade[1] > 0
        shares_traded = abs(trade[1])
        price = prices[trade[0]]

        for i in range(shares_traded):
            if is_purchase:
                shares_held.append(price)
            else:
                profit += price - shares_held.popleft()

    return profit


if __name__ == "__main__":
    print(solution([10.25, 11, 10.75, 11.5], [[0, 10], [1, -5], [2, 10], [3, -15]]))
