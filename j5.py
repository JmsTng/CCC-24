R, C = int(input()), int(input())
field = [list(input()) for _ in range(R)]
x, y = int(input()), int(input())

searched = set()


def search(r, c, searched):
    total = 0

    if clear(r, c, searched): return total
    if (r, c) in searched: return total
    if 0 > r >= R or 0 > c >= C or field[r][c] == '*': return total

    searched.add((r, c))

    if field[r][c] == 'S': total += 1
    if field[r][c] == 'M': total += 5
    if field[r][c] == 'L': total += 10

    if r + 1 < R: total += search(r + 1, c, searched)
    if c + 1 < C: total += search(r, c + 1, searched)
    if r - 1 >= 0: total += search(r - 1, c, searched)
    if c - 1 >= 0: total += search(r, c - 1, searched)

    return total


def clear(r, c, searched):
    if (r, c) in searched and \
       (r + 1, c) in searched and \
       (r, c + 1) in searched and \
       (r - 1, c) in searched and \
       (r, c - 1) in searched:
        return True
    return False

print(search(x, y, searched))
