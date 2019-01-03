import sys
from osgeo import ogr

fn=r'D:\BackUp\projectsBackup\Qgis\pygis\res\ne_50m_populated_places.shp'
ds=ogr.Open(fn,0)
if ds is None:
    sys.exit('could not open {0}.'.format(fn))
lyr=ds.GetLayer(0)

#此图层要素总量
num_features=lyr.GetFeatureCount()
print(num_features)
#根据要素编号Fid获取对应图层
third_feature=lyr.GetFeature(num_features-1)
print(third_feature.NAME)

del ds
