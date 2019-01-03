import ospybook as pb

fn=r'D:\BackUp\projectsBackup\Qgis\pygis\res\ne_50m_populated_places.shp'
pb.print_attributes(fn,3,['NAME','POP_MAX'])