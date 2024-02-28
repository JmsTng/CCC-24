R, C = int(input()), int(input())
field = [list(input()) for _ in range(R)]
r, c = int(input()), int(input())

frontier = {(r, c)}
searched = set()
total = 0

while len(frontier):
    print(frontier)
    print(searched)
    r, c = frontier.pop()
    searched.add((r, c))

    if field[r][c] == "*":
        continue

    if r + 1 < R and (r + 1, c) not in searched:
        frontier.add((r + 1, c))
    if r - 1 >= 0 and (r - 1, c) not in searched:
        frontier.add((r - 1, c))
    if c + 1 < C and (r, c + 1) not in searched:
        frontier.add((r, c + 1))
    if c - 1 >= 0 and (r, c - 1) not in searched:
        frontier.add((r, c - 1))

    if field[r][c] == 'S':
        total += 1
    elif field[r][c] == 'M':
        total += 5
    elif field[r][c] == 'L':
        total += 10

print(total)
