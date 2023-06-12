pochivni_dni = int(input())
norma_za_igra = 30000

pochivni_dni_minuti = pochivni_dni * 127
rabotni_dni_minuti = (365 - pochivni_dni) * 63
obshto_minuti = pochivni_dni_minuti + rabotni_dni_minuti

diff = abs(norma_za_igra - obshto_minuti)

h = diff // 60
m = diff % 60

if norma_za_igra >= obshto_minuti:
    print(f"Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
elif norma_za_igra <= obshto_minuti:
    print(f"Tom will run away")
    print(f"{h} hours and {m} minutes more for play")