def count_neighbours(grid, row, col):
    counter = 0
    if row > 0:
        r = grid[row-1]
        if col > 0:
            counter += r[col-1]
        counter += r[col]
        if col + 1 < len(r):
            counter += r[col+1]
    r = grid[row]
    if col > 0:
        counter += r[col-1]
    if col + 1 < len(r):
        counter += r[col+1]
    if len(grid) > row + 1:
        r = grid[row + 1]
        if col > 0:
            counter += r[col-1]
        counter += r[col]
        if col + 1 < len(r):
            counter += r[col+1]
  
    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 2, 3) == 3, "1st example"

