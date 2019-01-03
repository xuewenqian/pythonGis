import sys
from osgeo import ogr

fn=r'D:\BackUp\projectsBackup\Qgis\pygis\res\ne_50m_populated_places.shp'
ds=ogr.Open(fn,0)
if ds is None:
    sys.exit('could not open {0}.'.format(fn))
lyr=ds.GetLayer(0)

i=0
for feat in lyr:
    pt=feat.geometry()
    x=pt.GetX()
    y=pt.GetY()
    name=feat.NAME #GetField('Name')
    pop=feat.GetField('POP_MAX')
    print(name,pop,x,y)
    i+=1
    if i==10:
        break
del ds