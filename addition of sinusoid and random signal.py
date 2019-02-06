import matplotlib.pyplot as plt
import numpy as np
f=float(input("enter the frequency "))
fs=float(input("enter the sampling frequency"))
x=np.arange(0,50,0.5)
y=np.sin(2*np.pi*f*x/fs)
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("sine wave")
z=np.random.rand(x.shape[0])
plt.subplot(2,2,2)
plt.plot(x,z)
plt.title("random signal")
w=y+z
plt.subplot(2,2,3)
plt.plot(x,w)
plt.title("sine+random")
k=w-z
plt.subplot(2,2,4)
plt.plot(x,k)
plt.show()
