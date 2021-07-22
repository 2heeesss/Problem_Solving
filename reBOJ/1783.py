import sys
input = sys.stdin.readline

n, cal = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(cal):
    cards.sort()
    cards[0], cards[1] = cards[0]+cards[1], cards[0]+cards[1]

print(sum(cards))
