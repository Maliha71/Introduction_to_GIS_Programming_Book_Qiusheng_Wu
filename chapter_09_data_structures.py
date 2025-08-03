#Creating a Tuple to Represent the Co-ordinated the Tokyo City
tokyo_point=(
    35.6895,
    139.6917,
)
print(f"The coordinated of Tokyo City:{tokyo_point}")


# Accessing the Tuple Elements
latitude= tokyo_point[0]
latitude
longitude=tokyo_point[1]
longitude

print(f"the latitude is {latitude}")
print(f"the longitude is {longitude}")

#Tuple unpacking
#Function: Extract tuple elements into separate variables

lat,lon= tokyo_point
print(f"Tokyo is located at {lat} and {lon}")

#Multiple cooridate points
#P:Create tuple points for multiple geogrpahic points of multiple places

new_york=(40,7128, -74.0060)
london=(51.5074, -0.1278)
sydney=(-33.8688,151.2093)
print(f"the geo-location of london is {london}, new york is {new_york} and sydney is {sydney}")


#List 
#Ordered, mutable sequences of multiple items.

#P: Create a list of coordinate tuples representing a travel route

route=[
    (35.6895,139.6917),
    (34.0522, -118.2437),
    (51.5074, -0.1278),
]
route

 # P: Create a list of Elevation Measurements

elevations=[
    (120.5, 135.2, 150.8, 168.3, 185.7, 203,1)
 ]
elevations

# P:Create a City Name List

cities = ["Tokyo","Los Angels","London","Paris"]
print(f"cities to visist {cities}")

#Adding Elements to Lists
# . append()

# Will not work for any tuple, Example
new_york=(40,7128, -74.0060)
new_york.append(45)
new_york

#But will work in this way
new_york=new_york+(45,)
new_york

#Will work for list, Example
tokyo=[
    35.6895,
    139.6917,
]

tokyo.append(45,)
tokyo


#Accessing the List Elments

route=[
    (35.6895,139.6917),
    (34.0522, -118.2437),
    (51.5074, -0.1278),
]

first_stop=route[0]
first_stop

second_stop=route[1]
second_stop

third_stop=route[2]
third_stop

#List Slicing
first_two_components=route[0:2]
first_two_components

#or
first_two_components=route[:2]
first_two_components

#P:Find the number of waypoints in the route
len(route)
print(f"The number of waypoints in the route is {len(route)}")

numbers=[1,2,3,4,5,]
print(f"The maximum elevation is {max(numbers)} and the minimym number is {min(numbers)}")

#Sets
#Function: Only unique , Automatically removes duplicates.

#way:1
country_codes= ["USA","CA","MX","UK","USA","USA"]
unique_country_codes=set(country_codes)
unique_country_codes

#way:2
regions_visited={"North America","Europe","Asia","Asia",}
print("Regions visited:",regions_visited)


#Adding Elements to Sets
#YOu can add, but duplicates will automatically be ignored

regions_visited.add("India")
regions_visited

#P:Find out the common things of 2 sets


area_a={"oak","pine","mango"}
area_b={"pine","cedar","mango"}
common_species= area_a.intersection(area_b)
common_species


#P: Find out items unique to A
unique_to_a= area_a-area_b
unique_to_a

#P: All items of A and B together

all_items= area_a.union(area_b)
all_items

#P:Check is any item is in the set

if "mango" in area_a:
    print("the mango is in the set a")
else:
    print("the mango is not in the set a")

#Dictionaries
tokyo_info={
    "name": "SP001",
    "latitude":40.7589,
    "longitude":-73.9851,
    "elevation": 87.3,
    "land_cover":"urban",
    "date_surveyed":"12-76-7889"
}
print("Survey point data:",tokyo_info)


## Safe access to dictionary values

area= tokyo_info.get("land_cover","Not found")
longiture=tokyo_info.get("longtude","not found")  #The second part is if the value is not found. 
longiture
area



#Adding and Updating the values
#Adding Key-Value Pairs

tokyo_info["area_km2"]=2191
tokyo_info["timezone"]="JST"
tokyo_info["population"]=14000

print("updated tokyo:",tokyo_info)

world_capitals= {
    "Japan":{
        "capital":"Tokyo",
        "coordinates":(89843,93843),
        "population": 483084,

    },
    "France":{
        "capital":"Paris",
        "coordinates":(738743,78743),
        "population":798739849,
    },   
}

world_capitals

#Access informtion

france_info=world_capitals["France"]
france_info

print(f"the info of france is {world_capitals["France"]}")

# #Create a list of tuples, where each tuple contains the name of a city and its corresponding latitude and
#  longitude:
#  • New York City: (40.7128, −74.0060)
#  • Los Angeles: (34.0522, −118.2437)
#  • Chicago: (41.8781, −87.6298)
#  Perform the following tasks:
#  1. Add a new city (e.g., Miami: (25.7617, −80.1918)) to the list.
#  2. Print the entire list of cities.
#  3. Slice the list to print only the first two cities

city_tuple=[
    ( "New York City: (40.7128, −74.0060)"),
    ("Los Angeles: (34.0522, −118.2437)"),
    ("Chicago: (41.8781, −87.6298)"),
]
city_tuple

#1
city_tuple.append("Miami: (25.7617, −80.1918)")
city_tuple

#2
city_dic= {
    "New York City":(40.7128, -74.0060),
     "Los Angeles":(34.0522, -118.2437),
     "Chicago":(41.8781, -87.6298),
}
   
list(city_dic.keys())

#3
city_tuple[0,2]
city_tuple



# # Create a tuple to store the coordinates (latitude, longitude) of the Eiffel Tower: (48.8584, 2.2945). Perform
#  the following tasks:
#  1. Access and print the latitude and longitude values from the tuple.
#  2. Try to change the latitude value to 48.8585. What happens? Explain why


eiffel_tuple= (48.8584, 2.294)

#1
latitude,longitude= (48.8584, 2.294)
latitude
longitude

#2
eiffel_tuple[0]=48.8585



#  Create a set of countries you have visited, such as {“USA”, “France”, “Germany”}. Perform the following
#  tasks:
#  1. Add a new country to the set.
#  2. Try to add the same country again. What happens?
#  3. Print the updated set.

#1
countries={"USA","fRNACE","Germany"}
countries.add("Inida")
countries

#2
countries.add("USA")
countries

#3
print(f"The updated set is {countries}")


# #9.9.4. Exercise 4: Working with Dictionaries
#  Create a dictionary to store information about a specific geospatial feature, such as a river:
#  • Name: “Amazon River”
#  • Length: 6400 km
#  • Countries: [“Brazil”, “Peru”, “Colombia”]
#  Perform the following tasks:
#  1. Add a new key-value pair to the dictionary to store the river’s average discharge (e.g., 209,000 m³/s).
#  2. Update the length of the river to 6992 km.
#  3. Print the dictionary

#1
river = {
    "Name": "Amazon River",
    "Length": "6400 km",
    "Countries": ["Brazil", "Peru", "Colombia"]
}

river["Distance"]="209,000 m³/s"
river

#2
river["Distance"]="6992 km"
river

#3
print("print", river)

#  9.9.5. Exercise 5: Nested Data Structures
#  Create a dictionary to represent a city that contains the city’s name, population, and coordinates (latitude,
#  longitude):
#  • Name: “Tokyo”
#  • Population: 13,515,271
#  • Coordinates: (35.6895, 139.6917)
#  Perform the following tasks:
#  1. Access and print the population of the city.
#  2. Access and print the city’s latitude.
#  3. Update the population to 14,000,000 and print the updated dictionary.

city_info = {
    "Name": "Tokyo",
    "Population": 13515271,
    "Coordinates": (35.6895, 139.6917),
}

#1
accessed_info= city_info["Name"]
print(accessed_info)

#2
accessed_lat= city_info["Coordinates"]
print(accessed_lat)

#3
city_info["Population"]=14000000
city_info

