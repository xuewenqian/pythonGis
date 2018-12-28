from osgeo import gdal

raster=gdal.Open('res/SatImage.tif')
print(raster.RasterCount)
print(raster.RasterXSize)
print(raster.RasterYSize)