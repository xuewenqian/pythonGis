import geojson

p=geojson.Point([-92,37])

geojs=geojson.dumps(p)
print(geojs)