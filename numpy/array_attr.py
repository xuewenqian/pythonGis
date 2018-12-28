import numpy as np

a=np.arange(24)

print(a)
print(a.ndim)

b=a.reshape(2,3,4)
print(b)
print(b.ndim)

c=np.array([[1,2,3],[4,5,6]])
print(c.shape)

c.shape=(3,2)
print(c)

d=c.reshape(3,2)
print(d)


print('-----itemsize属性-----')
x=np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)

y=np.array([1,2,3,4,5],dtype=np.float64)
print(y.itemsize)

print('-----flag属性-----')
x=np.array([1,2,3,4,5])
print(x.flags)