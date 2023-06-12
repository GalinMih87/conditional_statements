km = int(input())
den_nosht = input()
price = 0

if den_nosht == "day":
    if km < 20:
      price = 0.7 + (0.79 * km)
    elif km < 100:
        price = 0.09 * km
    else:
        price = 0.06 * km

if den_nosht == "night":
    if km < 20:
        price = 0.7 + (0.9 * km)
    elif km < 100:
        price = 0.09 * km
    else:
        price = 0.06 * km
print(f"{price:.2f}")