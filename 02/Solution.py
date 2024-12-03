def PartOne():
  Content = open("Input.txt").read().splitlines()

  SafeLevels = 0
  for Line in Content:
    Levels = [int(i) for i in Line.split()]
    LevelsZip = list(zip(Levels, Levels[1:]))
    LevelsDelta = [abs(x-y) for x, y in LevelsZip]
    LevelsSign = [1 if x-y >= 0 else -1 for x, y in LevelsZip]

    if min(LevelsDelta) < 1 or max(LevelsDelta) > 3:
      continue
    if abs(sum(LevelsSign)) != len(Levels)-1:
      continue
    
    SafeLevels += 1

  return SafeLevels

def IsSafe2(LevelsDelta, LevelsSign, Length):
  Tolerated = False
  for Delta in LevelsDelta:
    if Delta < 1 or Delta > 3:
      if Tolerated:
        return 0
      else:
        Tolerated = True

  DeltaSign = abs(abs(sum(LevelsSign))-Length)//2
  if DeltaSign > 1 or (Tolerated and DeltaSign > 0):
    return 0
  
  return 1

def PartTwo():
  Content = open("Input.txt").read().splitlines()

  SafeLevels = 0
  for Line in Content:
    Levels = [int(i) for i in Line.split()]
    LevelsZip = list(zip(Levels, Levels[1:]))
    LevelsDelta = [abs(x-y) for x, y in LevelsZip]
    LevelsSign = [1 if x-y >= 0 else -1 for x, y in LevelsZip]
    
    SafeLevels += IsSafe2(LevelsDelta, LevelsSign, len(Levels)-1)

  return SafeLevels

print(PartOne())
print(PartTwo())