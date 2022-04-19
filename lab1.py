day_1=['home','library', 'school', 'job', 'home']
day_2=['home', 'school', 'pc','home']
day_3=['home', 'library', 'school', 'job', 'home']

days = day_1 + day_2 + day_3
print(days)

unique_locations= set (days)
for location in unique_locations:
    print (location, days.count(location))