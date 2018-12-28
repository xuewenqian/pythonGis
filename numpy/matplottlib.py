import numpy as np 
from matplotlib import pyplot as plt 
 
x = np.arange(-10,10) 
y = x*x+x
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y)
plt.show()