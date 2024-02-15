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
  # Check row constraint
  if value in square[r]:
      return False

  # Check column constraint
  if value in [square[i][c] for i in range(N)]:
      return False

  return True


def solve(square):
  # Find the next unassigned variable
  r, c = find_unassigned(square)

  # If there is no unassigned variable, solution has been found
  if r == -1 and c == -1:
      print_square(square)
      exit(0)

  # Consider its possible assignments
  for value in range(1, N + 1):
      # If the possible solution is valid, 
      # explore from that point forward
      if is_valid(square, r, c, value):
          square[r][c] = value
          solve(square)

  # If we reach here, we never found a solution
  #clear the assignment and backtrack
  square[r][c] = 0


### Main
N = 5

square = [[0 for _ in range(N)] for _ in range(N)]

# Set fixed numbers
square[0][0] = 4
square[1][4] = 2
square[2][2] = 4
square[3][4] = 4

print("Initial Latin Square:")
print_square(square)

solve(square)
