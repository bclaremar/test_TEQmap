#!/bin/python3

import scipy.io
import numpy as np

mat = scipy.io.loadmat('EPTfields')
#print(mat)
EPTS=mat['EPTS']
#print(EPTS)
#mat = scipy.io.loadmat('EPTfield')
EPT=mat['EPT']
#print(EPT)
#mat = scipy.io.loadmat('Tfield')
Tt=mat['T']
#print(T)
z=mat['z']
#print(z)

size=np.shape(EPT)
print(size)

LEQ=np.full_like(EPT,0)
LFC=np.full_like(EPT,0)
TEQ=np.full_like(EPT,np.nan)

a=np.where(EPTS-EPT<0)
lOC= list(zip(a[1], a[2], a[0]))
b=np.array(lOC)
lb=len(b)
kx=np.max(b[:,2])
print(kx)

c=np.where(b[:,2]==kx)
c= list(zip(c[0]))
c=np.array(c)
print(len(c))
print(b[c,:3])
kkx=kx
for k in range(len(b)-1,0,-1):

    kx=b[k,2]
    i=b[k,0]
    j=b[k,1]
    if kx-kkx:
    	print(kx)
    if np.isnan(TEQ[i,j]):
        TEQ[i,j]=Tt[kx,i,j]     
        LEQ[i,j]=z[kx,i,j]     
    kkx=kx
    
print(LEQ)
print(TEQ)


'''
for key in mat.keys():
    if key[0]=="_":
        continue
    cmd = '{0:} = mat["{0:}"]'.format(key)
    exec(cmd)
'''
