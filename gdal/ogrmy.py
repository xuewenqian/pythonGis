from osgeo import ogr

shp=ogr.Open('res/point.shp')
layer=shp.GetLayer()
for feature in layer:
    geometry=feature.GetGeometryRef()
    print(geometry.GetX(),geometry.GetY(),feature.GetField('FIRST_FLD'))
    