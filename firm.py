from math import floor

h = int(input())
d = int(input())
peoples = int(input())

training = (d - (d * 0.1)) * 8
overtime = peoples * (2 * d)
obshto_chasove = floor(training + overtime)

diff = abs(obshto_chasove - h)
if obshto_chasove >= h:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")
