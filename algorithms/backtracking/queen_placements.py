def count_queen_placements(n: int) -> int:
    n_2 = n * 2
    columns = [False] * n
    diag1 = [False] * n_2
    diag2 = [False] * n_2
    return _search_queen_placements(0, n, columns, diag1, diag2)


def _search_queen_placements(
        curr_row: int,
        n: int,
        columns: list[bool],
        diag1: list[bool],
        diag2: list[bool]
    ) -> int:
    if curr_row >= n:
        return 1
    
    count = 0
    for x in range(0, n): # column position on curr_row
        if columns[x] or diag1[x + curr_row] or diag2[x - curr_row + n - 1]:
            continue

        columns[x] = diag1[x + curr_row] = diag2[x - curr_row + n - 1] = True
        count += _search_queen_placements(curr_row + 1, n, columns, diag1, diag2)
        columns[x] = diag1[x + curr_row] = diag2[x - curr_row + n - 1] = False

    return count


if __name__ == "__main__":
    n = 8
    print(f"For n={n}, possible placements: {count_queen_placements(n)}")
