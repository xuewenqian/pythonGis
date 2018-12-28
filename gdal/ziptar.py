import zipfile
import tarfile

#待解压文件
zipName='res/SatImage.zip'

zip=open(zipName,'rb')
zipShape=zipfile.ZipFile(zip)

#解压zip文件
for fileName in zipShape.namelist():
    out=open('res/'+fileName,"wb")
    out.write(zipShape.read(fileName))
    out.close()


#生成tar文件   
#tar=tarfile.open('res/hancock.tar.gz','w:gz')
#tar.add('res/hancock.shp')
#tar.add('res/hancock.shx')
#tar.add('res/hancock.dbf')
#tar.close()