from math import floor, ceil

vineyard = int(input())
grapes = float(input())
liters_needed = int(input())
people = int(input())

total_grapes = vineyard * grapes
wine = 0.4 * (total_grapes / 2.5)

diff = abs(wine - liters_needed)

if wine < liters_needed:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
elif wine >= liters_needed:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / people)} liters per person.")
