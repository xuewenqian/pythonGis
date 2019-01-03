import sys 
from osgeo import ogr
import time

fn=r'D:\BackUp\projectsBackup\Qgis\pygis\res\ne_50m_populated_places.shp'
ds=ogr.Open(fn,0)
if ds is None:
    sys.exit('could not open {0}.'.format(fn))
lyr=ds.GetLayer(0)


for feat in lyr:
    name=feat.NAME
    print(name)

#将当前要素指针重新指向起始位置
lyr.ResetReading()
time.sleep(5)
    
for feat in lyr:
    name=feat.NAME
    print(name)

del ds