from math import floor

h = int(input())
d = int(input())
peoples = int(input())

obuchenie = (d - (d * 0.1)) * 8
izvanreden_trud = peoples * (2 * d)
obshto_chasove = floor(obuchenie + izvanreden_trud)

diff = abs(obshto_chasove - h)
if obshto_chasove >= h:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")