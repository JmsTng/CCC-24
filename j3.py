from collections import Counter

scores = [int(input()) for _ in range(int(input()))]

counter = Counter(scores)

scores = list(set(scores))
scores.sort(reverse=True)

print(scores[2], counter.get(scores[2]))