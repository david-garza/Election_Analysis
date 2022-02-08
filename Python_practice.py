# Python If statement
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# Membership statements
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# Logical AND
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# logical OR
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# For loop
for county in counties:
    print(county)

# Dictionary Loops
print("\nFor Loop over a dictionary, returns keys")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

print("\nFor Loop over a dictionary, using key method")

for temp in counties_dict.keys():
    print(temp)

print("\nFor Loop over a dictionary, using value method")
for temp in counties_dict.values():
    print(temp)

print("\nFor Loop over a dictionary, using county key to get values")
for county in counties_dict:
    print(county)
    print(counties_dict[county])

print("\nFor Loop over a dictionary, using get method to get values")
for county in counties_dict:
    print(counties_dict.get(county))

print("\nFor Loop over a dictionary, to print key and values using items method")
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

# Dictionary of dictionary loop examples
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

print("\nDictionary of dictionaries loop as list")
for county_dict in voting_data:
    print(county_dict)

print("\nDictionary of dictionaries loop as list only printing county names")
for i in range(len(voting_data)):
    print(voting_data[i]['county']) #Returns a dictionary, county is the key to pull county value

# Printing values form a dictionary of dictionaries
print("\nDictionary of dictionaries returning values using nested loops")
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)