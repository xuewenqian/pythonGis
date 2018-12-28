import numpy as np

#nupmy.dtype(object,align,copy)

dt=np.dtype(np.int32)
print(dt)

dt2=np.dtype('i8')
print(dt2)

dt3=np.dtype([('age',np.int8)])
print(dt3)


student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)

a=np.array([('abc',21,50),('xyz',18,75)],dtype=student)
print(a)