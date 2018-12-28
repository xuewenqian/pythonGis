import urllib.request
import urllib.parse
import urllib.error
url="https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"
url2="https://github.com/GeospatialPython/Learn/raw/master/point.zip"
url2="https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip"

filename="res/hancock.zip"
filename2="res/point.zip"
filename3="res/SatImage.zip"

urllib.request.urlretrieve(url2,filename3)