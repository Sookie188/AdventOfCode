import argparse


class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()

  def part1(self):
    result = 0
    for line in self.lines:
      levels = [int(n) for n in line.split()]
      if self.checkLevels(levels):
        result +=1
    return result
  
  def part2(self):
    result = 0
    for line in self.lines:
      levels = [int(n) for n in line.split()]
      if self.checkLevels(levels):
        result +=1
      else:
        if self.checkLevelsAgain(levels):
          result +=1
    return result


  def checkLevels(self, levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    if all(diff > 0 for diff in differences):
        # This list is increasing.
        if all(diff <= 3 for diff in differences):
          # print(levels)
          return True
    elif all(diff < 0 for diff in differences):
        # This list is decreasing.
        if all(diff >= -3 for diff in differences):
          return True
    else:
        # This list is mixed.
        return False
    
  def checkLevelsAgain(self, levels):
    for i in range(len(levels)):
      toCheck = levels[:i] + levels[i+1:]
      if self.checkLevels(toCheck):
        return True

  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
