counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for key, value in counties_dict.items():
    print(f"{key} county has {value:,} registered voters.")

print("\n\n\n")

#Dictionary of dictionaries example
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registerd voters.")