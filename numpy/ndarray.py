import numpy as np

#np.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)

print('-----一维数组-----')
a=np.array([1,2,3])
print(a)

print('-----二维数组-----')
b=np.array([[1,2],[3,4]])
print(b)

print('-----最小维度-----')
c=np.array([1,2,3,4,5],ndmin=2)
print(c)

print('-----数据格式-----')
d=np.array([1,2,3],dtype=complex)
print(d)