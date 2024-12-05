import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    
  def part1(self):
    index_emptyline = self.lines.index("")
    rules = self.lines[:index_emptyline]
    uglyUpdates = self.lines[index_emptyline +1:]
    updates = [[int(num) for num in block.split(',')] for block in uglyUpdates]

    incorrect = self.getIncorrect(rules, updates)

    correct = updates.copy()
    for line in incorrect:
      if line in correct:
        correct.remove(line)

    result = []
    for line in correct:
      result.append(line[len(line)//2])
    
    return(sum(result))

  def getIncorrect(self, rules, updates):
    incorrect = []
    for rule in rules:
      first, second = map(int,rule.split("|"))
  
      for update in updates:
        if first not in update:
          continue
        if second not in update:
          continue
        foundFirst = update.index(first)
        foundSecond = update.index(second)
        if foundFirst > foundSecond:
          if update not in incorrect:
            incorrect.append(update)
    return incorrect
  
  def orderUpdates(self, rules, incorrect):
    for rule in rules:
      first, second = map(int,rule.split("|"))

      for update in incorrect:
        if first not in update:
          continue
        if second not in update:
          continue
        foundFirst = update.index(first)
        foundSecond = update.index(second)
        if foundFirst > foundSecond:
          thingie = update.pop(foundFirst)
          update.insert(foundSecond, thingie)
    return incorrect

  def part2(self):
    index_emptyline = self.lines.index("")
    rules = self.lines[:index_emptyline]
    uglyUpdates = self.lines[index_emptyline +1:]
    updates = [[int(num) for num in block.split(',')] for block in uglyUpdates]
    checkIncorrect = []

    incorrect = self.getIncorrect(rules, updates)
    incorrect = self.orderUpdates(rules, incorrect)

    if checkIncorrect != incorrect:
      checkIncorrect = self.getIncorrect(rules, updates)
      checkIncorrect = self.orderUpdates(rules, incorrect)
    
    result = []
    for line in checkIncorrect:
      result.append(line[len(line)//2])
    
    return(sum(result))
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
