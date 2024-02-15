def print_square(square):
    print('')
    for row in square:
        print(row)
    print('')

def find_unassigned(square):
    for i in range(N):
        for j in range(N):
            if square[i][j] == 0:
                return i, j
    return -1, -1

def is_valid(square, r, c, value):
    # row constraint
    if value in square[r]:
        return False

    # column constraint
    if value in [square[i][c] for i in range(N)]:
        return False

    # inequality constraints
    for i in range(N):
        if square[r][i] == value or square[i][c] == value:
            return False

    # row inequalities
    if r > 0 and square[r - 1][c] != 0:
        if square[r - 1][c] > 0 and value <= square[r - 1][c]:
            return False
        elif square[r - 1][c] < 0 and value >= -square[r - 1][c]:
            return False
    if r < N - 1 and square[r + 1][c] != 0:
        if square[r + 1][c] > 0 and value <= square[r + 1][c]:
            return False
        elif square[r + 1][c] < 0 and value >= -square[r + 1][c]:
            return False

    # column inequalities
    if c > 0 and square[r][c - 1] != 0:
        if square[r][c - 1] > 0 and value <= square[r][c - 1]:
            return False
        elif square[r][c - 1] < 0 and value >= -square[r][c - 1]:
            return False
    if c < N - 1 and square[r][c + 1] != 0:
        if square[r][c + 1] > 0 and value <= square[r][c + 1]:
            return False
        elif square[r][c + 1] < 0 and value >= -square[r][c + 1]:
            return False

    return True

def solve(square):
    r, c = find_unassigned(square)
    if r == -1 and c == -1:
        print_square(square)
        exit(0)

    for value in range(1, N + 1):
        if is_valid(square, r, c, value):
            square[r][c] = value
            solve(square)
            square[r][c] = 0

N = 4 

puzzle = [
    [2, 4, 1, 3],
    [3, 1, 4, 2],
    [4, 3, 2, 1],
    [1, 2, 3, 4]
]

print_square(puzzle)
solve(puzzle)
