#String Creation

location_name="Mount Everest" # Double quote
country= 'Nepal' #Single quote
description=""" Mount Everest is the Highest Peak """

print(f" Location \t {location_name}")

#Concatenation
location_full= location_name+ ", "+country
location_full

#Building a path

data_folder="geographic data"
filename="mountainpeaks.csv"
filepath=data_folder+"/"+filename
filepath

#String Repetation

separator= "-" * 30
print (separator)

tab_space=" "*4
tab_space

#String Length

location="Japan"

print(f"{len(location)}")

#  
City="Tokyo"
Latitude= 27.9881
Longitude= 86.9250 
Elevation= 8848

location_information=(
    City
    + " is located at coordiante "
    +str (Latitude)
    +str (Longitude)
)
print(location_information)

Loci= ( City + " is located at " + str(Latitude) + "and" + str(Longitude) + "and" + str(Elevation) )
Loci 

#A more complex example-building a geographic summary
country ="Nepal"
cities=["Kathmandu", "Pokhra", "Lalipur"]
summary= "Major cities in "+ country + " include " + ", ".join(cities)
print(summary)


#join() function
country ="Nepal"
cities=["Kathmandu", "Pokhra", "Lalipur"]
summary= "Major cities in" + country + " include " + ().join(cities)
summary

#Case Conversion
mountain_name="Mount Everest"

print(f"origianals: {mountain_name}")
print(f"Uppercase: {mountain_name.upper()}")
print (f"Capital: {mountain_name.capitalize()}")
print(f"Lowercase: {mountain_name.lower()}")
print(f"Titlecase: {mountain_name.title()}")

# Whitespace Removal Method

messy_location= "  San Francisco   "
print(f"Original: '{messy_location.strip()}'")
print(f"lstrip(): '{messy_location.lstrip()}'")
print(f"rstrip(): {messy_location.rstrip()}'")

#String Replacement =.replace()
location="Mount Everest, Nepal"
updated_location=location.replace("Everest","Kilimanjaro")

print(f"{location}")
print(f"{updated_location}")

#String Splitting

location_full= "mount everest, nepal, asia "
location_parts= location_full.split(", ")

print(f"split into the parts: {location_parts}")

#splitting coordinates into stirngs

coordinate_string= "40.8383,-90.83983"
lat_str, lon_str= coordinate_string

print(f"coordiate are: Lat={lat_str} and long= {lon_str} ")



 # Splitting file paths
 file_path = "data/geographic/cities/world_cities.csv"
 path_components = file_path.split("/")
 print(f"Path components: {path_components}")
 print(f"Filename: {path_components[-1]}")  # Last component is the filename



#String Joining

city_names= ["san francisco", "NY", "Tokyo"]
city_name= ",".join(city_names)
print(f"Join city name: {city_name}")

#creating path files

path_components = ["data", "geographic", "elevation", "dem.tif"]
city_names = "/".join(path_components)
print(f"joined city names: {city_names}")
 
#String Formatiing
#F-string formatiing

location= "Mount Everst"
latitude= 27.9881
longitude= 86.92
elevation= 8848

#  Simple variable insertion
location_info= f"location :{location}"
location_info

coordinates=f"coordinates: {latitude}, {longitude}"
coordinates

#Formatting Numbers in Strings

precise_lat = 40.712
precise_lon = -4.0059
coordinates = f"coordinates:{precise_lat:.2f},{precise_lon:.2f}"
print(coordinates)

#Adding thousands separators for large numbers

population= 8336817
area= 783.6

formatted_stats=f"NYC Popultaion:{population:,}, Area: {area: .2f}"
formatted_stats


#Legacy Formatting Methods

#using .format() method

location= "San Francisco"
lat= 37.983
lon= -122.743

#Basic Format Method
formatted_1= "Location:{} at coordiatnes ({},{})".format(location, lat, lon)
formatted_1

formatted_2= "Location:{0} at coordiatnes ({1},{2})".format(location, lat, lon)
formatted_2

