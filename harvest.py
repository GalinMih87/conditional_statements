from math import floor, ceil

vineyard = int(input())
grozde_kwm = float(input())
nujni_litri = int(input())
robi = int(input())

obshto_grozde = vineyard * grozde_kwm
vino = 0.4 * (obshto_grozde / 2.5)

diff = abs(vino - nujni_litri)

if vino < nujni_litri:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
elif vino >= nujni_litri:
    print(f"Good harvest this year! Total wine: {floor(vino)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / robi)} liters per person.")
