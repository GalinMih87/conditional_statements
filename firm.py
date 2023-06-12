from math import floor

h = int(input())
d = int(input())
peoples = int(input())

training = (d - (d * 0.1)) * 8
overtime = peoples * (2 * d)

total_hours = floor(training + overtime)

diff = abs(total_hours - h)
if total_hours >= h:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")
