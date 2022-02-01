"""
Hurricane Analysis

Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe 
the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter 
a problem that you cannot easily solve.

Project Goals
You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a 
number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.
"""

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
# Takes a list of damages in M/B format and returns in float format
def update_recorded_damages(damages_list):
  damages_converted = []
  for damage in damages_list:
    if damage == 'Damages not recorded':
      damages_converted.append(damage)
    elif "M" in damage:
      damages_converted.append(conversion["M"] * float(damage.strip("M")))
    elif "B" in damage:
      damages_converted.append(conversion["B"] * float(damage.strip("B")))
  return damages_converted

damages = update_recorded_damages(damages)   


# 2 
# Create a Table
def hurricanes_dictionary(names, months, years, max_wind, areas_affected, damage, deaths):
  hurricane_dictionary = {}
  for i in range(len(names)):
    hurricane_dictionary.update({names[i]: {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_wind[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Deaths": deaths[i]}})
  return hurricane_dictionary

# Create and view the hurricanes dictionary
hurricane_dictionary = hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricane_dictionary)

# 3
# Organizing by Year
def dictionary_by_year(hurricane_dictionary):
  dictionary_by_year = {}
  year_tracker = []
  for year in years:
    if year not in year_tracker:
      year_list = []
      for hurricane in hurricane_dictionary.values():
        if hurricane["Year"] == year:
          year_list.append(hurricane)
      dictionary_by_year[year] = year_list
    year_tracker.append(year)
  return dictionary_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = dictionary_by_year(hurricane_dictionary)
# print(hurricanes_by_year)

# 4
# Counting Damaged Areas
def count_by_affected_area(hurricane_dictionary):
  all_areas_affected = []
  for hurricane in hurricane_dictionary.values():
    for i in range(len(hurricane["Areas Affected"])):
      all_areas_affected.append(hurricane["Areas Affected"][i])
  hurricanes_counted_by_area = {}
  for area in all_areas_affected:
    if area not in hurricanes_counted_by_area.keys():
      hurricanes_counted_by_area[area] = all_areas_affected.count(area)
  return hurricanes_counted_by_area

# create dictionary of areas to store the number of hurricanes involved in
hurricane_count_by_area = count_by_affected_area(hurricane_dictionary)
# print(hurricane_count_by_area)

# 5 
# Calculating Maximum Hurricane Count
def most_hurricanes(hurricane_count_dict):
  most_hurricanes_count = 0
  most_hurricanes = {}
  for area, count in hurricane_count_by_area.items():
    if count > most_hurricanes_count:
      most_hurricanes = {area: count}
      most_hurricanes_count = count
    elif count == most_hurricanes_count:
      most_hurricanes.update({area: count})
  return most_hurricanes


# find most frequently affected area and the number of hurricanes involved
most_frequent_hurricanes = most_hurricanes(hurricane_count_by_area)
# print(most_frequent_hurricanes)

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricane_dictionary):
  deadliest = {}
  max_mortality = 0
  for name, hurricane in hurricane_dictionary.items():
    if hurricane["Deaths"] > max_mortality:
      deadliest = {name: hurricane["Deaths"]}
      max_mortality = hurricane["Deaths"]
    elif hurricane["Deaths"] == max_mortality:
      deadliest.update({name: hurricane["Deaths"]})
  return deadliest
# find highest mortality hurricane and the number of deaths

most_deadly_hurricane = deadliest_hurricane(hurricane_dictionary)
# print(most_deadly_hurricane)


# 7
# Rating Hurricanes by Mortality
def hurricanes_by_mortal_rating(hurricane_dictionary):
  mortal_rating_hurricanes = {}
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for name, hurricane in hurricane_dictionary.items():
    if hurricane["Deaths"] == mortality_scale[0]:
      if mortality_scale[0] in mortal_rating_hurricanes.keys():
        mortal_rating_hurricanes[0].append(hurricane)
      else:
        mortal_rating_hurricanes[0] = [hurricane]
    elif hurricane["Deaths"] <= mortality_scale[1]:
      if mortality_scale[1] in mortal_rating_hurricanes.keys():
        mortal_rating_hurricanes[1].append(hurricane)
      else:
        mortal_rating_hurricanes[1] = [hurricane]
    elif hurricane["Deaths"] <= mortality_scale[2]:
      if mortality_scale[2] in mortal_rating_hurricanes.keys():
        mortal_rating_hurricanes[2].append(hurricane)
      else:
        mortal_rating_hurricanes[2] = [hurricane]
    elif hurricane["Deaths"] <= mortality_scale[3]:
      if mortality_scale[3] in mortal_rating_hurricanes.keys():
        mortal_rating_hurricanes[3].append(hurricane)
      else:
        mortal_rating_hurricanes[3] = [hurricane]
    elif hurricane["Deaths"] <= mortality_scale[4]:
      if mortality_scale[4] in mortal_rating_hurricanes.keys():
        mortal_rating_hurricanes[4].append(hurricane)
      else:
        mortal_rating_hurricanes[4] = [hurricane]
    else:
      if 5 in mortal_rating_hurricanes.keys():
        mortal_rating_hurricanes[5].append(hurricane)
      else:
        mortal_rating_hurricanes[5] = [hurricane]
  return mortal_rating_hurricanes

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_mortality_ranked = hurricanes_by_mortal_rating(hurricane_dictionary)
# print(hurricanes_mortality_ranked)

# 8 Calculating Hurricane Maximum Damage
def greatest_damage_hurricane(hurricane_dictionary):
  max_damage = 0
  max_damage_hurricane = {}
  for name, hurricane in hurricane_dictionary.items():
    if hurricane["Damage"] == "Damages not recorded":
      continue
    elif hurricane["Damage"] > max_damage:
      max_damage_hurricane = {name: hurricane["Damage"]}
      max_damage = hurricane["Damage"]
    elif hurricane["Damage"] == max_damage:
      max_damage_hurricane.update({name: hurricane["Damage"]})
  return max_damage_hurricane

# find highest damage inducing hurricane and its total cost
most_destructive_hurricane = greatest_damage_hurricane(hurricane_dictionary)
# print(most_destructive_hurricane)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
def hurricanes_by_damage_rating(hurricane_dictionary):
  hurricane_rating_by_damage = {}
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for name, hurricane in hurricane_dictionary.items():
    if hurricane["Damage"] == "Damages not recorded":
      continue
    elif hurricane["Damage"] == damage_scale[0]:
      if damage_scale[0] in mortal_rating_hurricanes.keys():
        hurricane_rating_by_damage[0].append(hurricane)
      else:
        hurricane_rating_by_damage[0] = [hurricane]
    elif hurricane["Damage"] <= damage_scale[1]:
      if damage_scale[1] in hurricane_rating_by_damage.keys():
        hurricane_rating_by_damage[1].append(hurricane)
      else:
        hurricane_rating_by_damage[1] = [hurricane] 
    elif hurricane["Damage"] <= damage_scale[2]:
      if damage_scale[2] in hurricane_rating_by_damage.keys():
        hurricane_rating_by_damage[2].append(hurricane)
      else:
        hurricane_rating_by_damage[2] = [hurricane] 
    elif hurricane["Damage"] <= damage_scale[3]:
      if damage_scale[3] in hurricane_rating_by_damage.keys():
        hurricane_rating_by_damage[3].append(hurricane)
      else:
        hurricane_rating_by_damage[3] = [hurricane] 
    elif hurricane["Damage"] <= damage_scale[4]:
      if damage_scale[4] in hurricane_rating_by_damage.keys():
        hurricane_rating_by_damage[4].append(hurricane)
      else:
        hurricane_rating_by_damage[4] = [hurricane] 
    else:
      if 5 in hurricane_rating_by_damage.keys():
        hurricane_rating_by_damage[5].append(hurricane)
      else:
        hurricane_rating_by_damage[5] = [hurricane]
  return hurricane_rating_by_damage

# categorize hurricanes in new dictionary with damage severity as key
destructive_hurricanes_rated = hurricanes_by_damage_rating(hurricane_dictionary)
# print(destructive_hurricanes_rated)
# print(destructive_hurricanes_rated[5])
