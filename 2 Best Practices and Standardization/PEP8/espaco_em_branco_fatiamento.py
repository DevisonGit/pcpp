"""
Bad:
bread[0 : 3], roll[1: 3 :5], bun[3: 5:], donut[ 1: :5 ]

Good:
bread[0:3], roll[1:3:5], bun[3:5:], donut[1::5]
"""

bread = "bread"
roll = "roll"
bun = "bun"
donut = "donut"

print(bread[0:3], roll[1:3:5], bun[3:5:], donut[1::5])
