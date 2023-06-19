holidays = int(input()) # Да го променя на английски език!!!
norm_of_play = 30000 # Да го променя на английски език!!!

pochivni_dni_minuti = holidays * 127 # Да го променя на английски език!!!
rabotni_dni_minuti = (365 - holidays) * 63 # Да го променя на английски език!!!
obshto_minuti = pochivni_dni_minuti + rabotni_dni_minuti # Да го променя на английски език!!!

diff = abs(norm_of_play - obshto_minuti) # Да го променя на английски език!!!

h = diff // 60
m = diff % 60

if norm_of_play >= obshto_minuti: # Да го променя на английски език!!!
    print(f"Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
elif norm_of_play <= obshto_minuti:
    print(f"Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
