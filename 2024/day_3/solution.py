import argparse
import re


class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    
  def part1(self):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    text = str(self.lines)
    matches = re.findall(pattern, text)
    numbers = []
    for match in matches:
      justNumbers = match.strip("mul()").split(",")  
      numbers.append(int(justNumbers[0]) * int(justNumbers[1]))
    return sum(numbers)
      
    
  def part2(self):
    text = str(self.lines)
    pattern_section = r"don't\(\)(.*?)do\(\)"
    section_match = re.findall(pattern_section, text)
    for match in section_match:
      text = text.replace(match, "")

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    numbers = []
    for match in matches:
      justNumbers = match.strip("mul()").split(",")  
      numbers.append(int(justNumbers[0]) * int(justNumbers[1]))
    return sum(numbers)    
   
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
