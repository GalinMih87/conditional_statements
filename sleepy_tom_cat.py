holidays = int(input()) # Да го променя на английски език!!!
norm_of_play = 30000 # Да го променя на английски език!!!

holidays_in_minutes = holidays * 127 # Да го променя на английски език!!!
working_days_in_minutes = (365 - holidays) * 63 # Да го променя на английски език!!!
obshto_minuti = holidays_in_minutes + working_days_in_minutes  # Да го променя на английски език!!!

diff = abs(norm_of_play - obshto_minuti) # Да го променя на английски език!!!

h = diff // 60
m = diff % 60

if norm_of_play >= obshto_minuti: # Да го променя на английски език!!!
    print(f"Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
elif norm_of_play <= obshto_minuti:
    print(f"Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
