# Find a path from the upper-left corner to the lower-right corner of an n × n grid,
# such that we only move down and right.
# Each square contains a positive integer, and the path should be constructed
# so that the sum of the values along the path is as large as possible.

from collections import deque


def find_max_sum_path(grid: list[list[int]]) -> int:
    n = len(grid)
    max_values = [[-1] * n for _ in range(n)]
    max_values[0][0] = grid[0][0]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        x1 = x + 1
        if x1 < n:
            if max_values[y][x1] < 0:
                queue.append((x1, y))
            max_values[y][x1] = max(max_values[y][x1], max_values[y][x] + grid[y][x1])

        y1 = y + 1
        if y1 < n:
            if max_values[y1][x] < 0:
                queue.append((x, y1))
            max_values[y1][x] = max(max_values[y1][x], max_values[y][x] + grid[y1][x])
        
    return max_values[-1][-1]


def find_max_sum_path2(grid: list[list[int]]) -> int:
    n = len(grid)
    max_values = [[0] * n for _ in range(n)]
    max_values[0][0] = grid[0][0]
    
    for x in range(1, n):
        max_values[0][x] = max_values[0][x - 1] + grid[0][x]
    
    for y in range(1, n):
        max_values[y][0] = max_values[y - 1][0] + grid[y][0]

    for y in range(1, n):
        for x in range(1, n):
            max_values[y][x] = max(max_values[y][x - 1], max_values[y - 1][x]) + grid[y][x]
    
    return max_values[-1][-1]


if __name__ == "__main__":
    grid = [
        [3, 7, 9, 2, 7],
        [9, 8, 3, 5, 5],
        [1, 7, 9, 8, 5],
        [3, 8, 6, 4, 10],
        [6, 3, 9, 7, 8]
    ]
    print(f"Max path: {find_max_sum_path(grid)}")
    print(f"Max path: {find_max_sum_path2(grid)}")
