
"""import numpy as np
digits=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(digits)


print(digits.shape)
print(digits[:,np.newaxis])
print(digits[np.newaxis:])
#print()
#print([[1,2,3],[4,5,6],[7,8,9]])
"""
import numpy as np
curve_center=80
grades=np.array([72,35,64,88,51,90,74,12])

def curve(grades):
    average=grades.mean()
    change=curve_center-average
    new_grades=grades+change
    return np.clip(new_grades,grades,100)
print(curve(grades))

a=np.linspace(5,50,24,dtype=int).reshape(3,8)
print(a)
print(a[a%8==0])
print(np.sort(a,axis=1))
a=np.zeros(shape=(3,3))
print(a)