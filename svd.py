import numpy as np
from numpy import linalg as LA

a=[[1,1,0,2],[1,1,2,0],[2,0,1,1]]
b=[[1,1],[2,2]]
U,s, V = np.linalg.svd(a, full_matrices=True,compute_uv =True)
V=np.array(V)
V=V.transpose()
print "U"  
for i in range(3):
    print U[i]
print "A"
for i in range(3):
    print s[i]
print "v Transpose"
for i in range(4):
    print V[i]
