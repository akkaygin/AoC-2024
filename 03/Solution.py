import re

def PartOne():
  Content = open("Input.txt").read().strip()

  Matches = re.findall(r"mul\((\d+),(\d+)\)", Content)
  Sum = 0
  for x, y in Matches:
    Sum += int(x)*int(y)
  
  return Sum

def PartTwo():
  Content = open("Input.txt").read()

  Matches = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", Content)
  Sum = 0
  Active = True
  for Match in Matches:
    if Match[2] == "do":
      Active = True
    elif Match[3] == "don't":
      Active = False
    else:
      if Active:
        Sum += int(Match[0]) * int(Match[1])
  
  return Sum

print(PartOne())
print(PartTwo())