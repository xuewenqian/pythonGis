import numpy as np

print('-----empty构建方法-----')
x=np.empty([3,2],dtype=int)
print(x)

print('-----zeros构建方法-----')
x=np.zeros(5)
print(x)
y=np.zeros((5,),dtype=np.int)
print(y)
z=np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
print(z)

print('-----ones构建方法-----')
x=np.ones(5)
print(x)
y=np.ones((2,2),dtype=int)
print(y)