import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

for i in a:
    for x in i:
        print(x)
    
    
b=np.array([10,20,30,40])
print(a.shape)
print(b.shape)
print(a+b)

c=np.array([[1,2,3],[5,6,7],[9,10,11]])
d=np.array([[1,2,3],[5,6,7]])
print(c.shape,d.shape)
#print(c+d)

e=np.array([[[1,2,3 ]],[[4,5,6 ]]])
print(e.shape)
f=np.array([10,20,30])
print(e+f)

g=np.array([ [[1],[2],[3]],[[4],[5],[6]], [[7],[8],[9]], [[10],[11],[12]],
             [[13],[14],[15]] ])
print(g.shape)
h=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(h.shape)
print(g+h)
