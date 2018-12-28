from osgeo import gdal_array

srcArray=gdal_array.LoadFile("res/SatImage.tif")
band1=srcArray[0]
gdal_array.SaveArray(band1,'res/band1.jpg',format="JPEG")