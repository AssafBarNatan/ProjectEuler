f = open("inputs/Problem18.txt")

lines = []
line = f.readline()

while line:
  lines.append(line[:-1].split(" "))
  line = f.readline()

lines = [[int(x) for x in line] for line in lines]

#lines = lines[::-1]

while len(lines) > 1:
  second_last = lines[-2]
  last = lines[-1]

  for i in range(len(lines[-2])):
    lines[-2][i] += max(lines[-1][i], lines[-1][i+1])

  lines = lines[:-1]
  for i in lines:
    print(i)

print(lines)
