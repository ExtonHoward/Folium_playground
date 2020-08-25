import pandas
from geopy.geocoders import ArcGIS

df = pandas.read_csv('files\supermarkets.csv')
df ["Address"] = df["Address"] + ", " + df["City"] + ', ' + df["State"] + ', ' + df["Country"]

nom = ArcGIS()
n = nom.geocode("3995 23rd St, San Francisco, CA 94114, USA")
lat = n.latitude
long = n.longitude

df ["Coordinates"] = df["Address"].apply(nom.geocode)
df ["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df ["Longitude"] = df["Coordinates"].apply(lambda x : x.longitude if x != None else None)

print (df)
