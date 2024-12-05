import argparse
from termcolor import colored

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()

  def part1(self):
    matrix = [list(row) for row in self.lines]
    
    results = self.findXmas(matrix, "XMAS")
    print(results)

  def findXmas(self, matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def search_from(x, y, dx, dy):
        """Search for the word starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or matrix[nx][ny] != word[i]:
                return False
        return True
    
    foundXmas = 0
    # Check each position in the grid
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == word[0]:  # Possible start of the word
                for dx, dy in directions:
                    if search_from(x, y, dx, dy):
                        foundXmas += 1

    return foundXmas


  def part2(self):
    matrix = [list(row) for row in self.lines]
    results = self.findMas(matrix, "MAS")
    print(len(results)/2)
    return len(results)/2

  def findMas(self, matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    word_len = len(word)
    directions = [
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def search_from(x, y, dx, dy):
        """Search for the word starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or matrix[nx][ny] != word[i]:
                return False
        return True

    def isX(x, y, dx, dy):
        if(dx == 1 and dy == 1): # down-right
            # if down-left or up-right
            if search_from(x, y+2, 1, -1):
                print("found DR: ", x, y+2)
                return True
            if search_from(x+2, y, -1, 1):
                print("found DR: ", x+2, y)
                return True
        if(dx == -1 and dy == -1): # up-left
            if search_from(x, y-2, -1, 1):
                print("found UL: ", x, y-2)
                return True
            if search_from(x-2, y, 1, -1):
                print("found UL: ", x+2, y-2)
                return True
        if(dx == 1 and dy == -1): # down-left
            if search_from(x, y-2, 1, 1):
                print("found DL: ", x, y-2)
                return True
            if search_from(x+2, y, -1, -1):
                print("found DL: ", x+2, y+2)
                return True
        if(dx == -1 and dy == 1) : # up-right
            if search_from(x, y+2, -1, -1):
                print("found UR: ", x, y+2)
                return True
            if search_from(x-2, y, 1, 1):
                print("found UR: ", x-2, y-2)
                return True
    
    foundMasx = []
    # Check each position in the grid
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == word[0]:  # Possible start of the word
                for dx, dy in directions:
                    if search_from(x, y, dx, dy):
                        print("check: ", x, y, dx, dy)
                        if isX(x, y, dx, dy):
                            print("found X! ")
                            foundMasx.append((x, y, dx, dy))  # Speichere die Position des Treffers

    return foundMasx

def highlight_words_in_grid(grid, matches, word):
    # Erstelle eine Kopie des Grids, um die Markierungen zu machen
    highlighted_grid = [row[:] for row in grid]  # Tiefenkopie des Grids

    # Markiere die Buchstaben des gefundenen Wortes
    for match in matches:
        x, y, dx, dy = match
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            # Färbe den Buchstaben rot
            highlighted_grid[nx][ny] = colored(grid[nx][ny], 'red')

    # Ausgabe des hervorgehobenen Grids
    for row in highlighted_grid:
        print(" ".join(row))


if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
