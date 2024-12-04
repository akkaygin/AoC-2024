def PartOne():
  def Search(x0, y0, Expected, Direction):
    x, y = x0+Direction[0], y0+Direction[1]
    if 0 <= x < len(Lines[0]) and 0 <= y < len(Lines):
      if Lines[y][x] == Expected:
        if Expected == 'A':
          return Search(x, y, 'S', Direction)
        else:
          return 1
    return 0

  Content = open("Input.txt").read().splitlines()

  Directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  Lines = [list(Line) for Line in Content]
  Result = 0
  for y in range(len(Lines)):
    xi = ''.join(Lines[y]).find('X')
    while xi >= 0:
      for dx, dy in Directions:
        xx, xy = xi+dx, y+dy
        if 0 <= xx < len(Lines[0]) and 0 <= xy < len(Lines):
          if Lines[xy][xx] == 'M':
            Result += Search(xx, xy, 'A', (dx, dy))
      Lines[y][xi] = 'x'
      xi = ''.join(Lines[y]).find('X')
  return Result

def PartTwo():
  Content = open("Input.txt").read().splitlines()

  Lines = [list(Line) for Line in Content]
  Result = 0
  for y in range(1, len(Lines)-1):
    ai = ''.join(Lines[y]).find('A')
    while ai >= 0:
      if ai != 0 and ai != len(Lines[0])-1:
        Set = set()
        Set |= {Lines[y-1][ai-1], Lines[y+1][ai-1], Lines[y-1][ai+1], Lines[y+1][ai+1]}
        if {'M', 'S'} == Set and Lines[y-1][ai-1] != Lines[y+1][ai+1] and Lines[y-1][ai+1] != Lines[y+1][ai-1]:
          Result += 1

      Lines[y][ai] = 'a'
      ai = ''.join(Lines[y]).find('A')
  return Result
  
print(PartOne())
print(PartTwo())