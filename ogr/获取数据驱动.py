from osgeo import ogr
import ospybook as pb

driver=ogr.GetDriverByName('GeoJSON')
print(driver)

driver2=ogr.GetDriverByName('ESRI shapefile')
print(driver2)

#输出驱动列表

pb.print_drivers()