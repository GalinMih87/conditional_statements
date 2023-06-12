from math import floor, ceil

vineyard = int(input())
grapes = float(input())
liters_needed = int(input())
robi = int(input())

obshto_grozde = vineyard * grapes
vino = 0.4 * (obshto_grozde / 2.5)

diff = abs(vino - liters_needed)

if vino < liters_needed:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
elif vino >= liters_needed:
    print(f"Good harvest this year! Total wine: {floor(vino)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / robi)} liters per person.")
