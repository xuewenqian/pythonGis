import sys
from osgeo import ogr

fn=r'D:\BackUp\projectsBackup\Qgis\pygis\res\ne_50m_populated_places.shp'
ds=ogr.Open(fn,0)
if ds is None:
    sys.exit('could not open {0}.'.format(fn))
lyr=ds.GetLayer(0)

#四至矩形框
extent=lyr.GetExtent()
print(extent)

del ds


