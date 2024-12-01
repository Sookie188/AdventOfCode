import argparse
from collections import Counter


class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    self.leftList = []
    self.rightList = []
    for line in self.lines:
      stupidParts = line.split(' ')
      self.leftList.append(int(stupidParts[0]))
      self.rightList.append(int(stupidParts[-1]))
    
  def part1(self):
    distances = []
    leftList = sorted(self.leftList)
    rightList = sorted(self.rightList)
    for a, b in zip(rightList, leftList):
        distances.append(abs(a-b))
    return sum(distances)
  
  def part2(self):
    counter = Counter(self.rightList)
    score = []
    for line in self.leftList:
      score.append(line*counter[line])
    return sum(score)

if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
