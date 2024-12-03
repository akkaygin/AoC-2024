def PartOne():
  Content = open("Input.txt").read().splitlines()

  LeftList = list()
  RightList = list()
  for Line in Content:
    Left, Right = Line.split()
    LeftList.append(int(Left))
    RightList.append(int(Right))
  
  LeftList.sort()
  RightList.sort()

  DeltaTotal = 0
  for i in range(len(LeftList)):
    DeltaTotal += abs(LeftList[i] - RightList[i])
  
  return DeltaTotal

from collections import defaultdict
def PartTwo():
  Content = open("Input.txt").read().splitlines()

  LeftList = set()
  RightList = defaultdict(int)

  for Line in Content:
    Left, Right = Line.split()
    LeftList.add(int(Left))
    RightList[int(Right)] += 1
  
  SimilarityScore = 0
  for i in LeftList:
    SimilarityScore += i * RightList[i]
  
  return SimilarityScore

print(PartOne())
print(PartTwo())
