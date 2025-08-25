a=int(input())
years=int(a)//365
rem_days=a-(years)*365

weeks=int(rem_days)//7
days=rem_days-(weeks)*7

print(years)
print(weeks)
print(days)
