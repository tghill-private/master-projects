from numpy import empty,zeros,amax
from pylab import imshow,gray,show,contourf,title
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n=100    #How many grid points to use
v1=-1.0
v2=1.1

target = 1e-2
phi=zeros([n+1,n+1],float)
phi[45,16:84]=v1
phi[55,16:84]=v2
phinew=empty([n+1,n+1],float)
A=zeros([n+1,n+1],float)
A[45:46,16:84]=v1
A[55:56,16:84]=v2

delta=1.0
while delta>target:
    for i in range (n+1):
        for j in range (n+1):
            if i==0 or i==n or j==0 or j==n:
                phinew[i,j]=phi[i,j]
            else:
                phinew[i,j]=(phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])/4. +A[i,j]
    delta=amax(abs(phi-phinew))
    phi,phinew=phinew,phi

imshow(phi)
#contourf(phi,interpolation='nearest')
#contour(phi,color='k',interpolation="nearest")
#title("Contour Plot of Phi")

show()

##A=array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],float)
##print A
##print A[1:2]
##print A[1:3,2:3]    #Gives column [8,13]
