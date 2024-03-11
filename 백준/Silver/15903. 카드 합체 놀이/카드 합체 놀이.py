import sys
import heapq
input=sys.stdin.readline
n,m=map(int, input().split())
card_list=list(map(int, input().split()))
cards = []
for card in card_list:
    heapq.heappush(cards, card)

for i in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))