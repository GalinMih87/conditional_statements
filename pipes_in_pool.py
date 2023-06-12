v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_l = p1 * h
p2_l = p2 * h
total = p1_l + p2_l
total_procent = (total / v) * 100

prinos_p1 = (p1_l / total) * 100
prinos_p2 = (p2_l / total) * 100

if v >= total:
    print(f"The pool is {total_procent:.2f}% full. Pipe 1: {prinos_p1:.2f}%. Pipe 2: {prinos_p2:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {total - v:.2f} liters.")
