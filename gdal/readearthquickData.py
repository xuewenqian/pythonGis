import urllib.request
import urllib.parse
import urllib.error

url="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"

earthquakes=urllib.request.urlopen(url)
#print(earthquakes.readline())
#print('\n')
#print(earthquakes.readline())
#print(earthquakes.readline())
#print(earthquakes.readline())
#print(earthquakes.readline())

for record in earthquakes:
    print(record)