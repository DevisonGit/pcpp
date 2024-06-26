"""Simple is better than complex.
import heapq

numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
heapq.heapify(numbers)

sorted_numbers = []

while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print(sorted_numbers)
"""
numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
numbers.sort()

print(numbers)
