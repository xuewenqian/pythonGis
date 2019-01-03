import os
from ospybook.vectorplotter import VectorPlotter

os.chdir(r'D:\GIS_Design_Department\git\pythonGis\osgeopy-data\global')
vp=VectorPlotter(False)
vp.plot('ne_50m_admin_0_countries.shp',fill=False)
vp.plot('ne_50m_populated_places.shp','bo')
vp.draw()