holidays = int(input()) 
norm_of_play = 30000 

holidays_in_minutes = holidays * 127 
working_days_in_minutes = (365 - holidays) * 63 
total_minutes = holidays_in_minutes + working_days_in_minutes  

diff = abs(norm_of_play - total_minutes) 

h = diff // 60
m = diff % 60

if norm_of_play >= total_minutes: 
    print(f"Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
elif norm_of_play <= total_minutes:
    print(f"Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
