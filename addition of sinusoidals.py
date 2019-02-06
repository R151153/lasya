import matplotlib.pyplot as plt
import numpy as np
f=float(input("enter the frequency"))
fs=float(input("enter the sampled frequency"))
x=np.arange(0,100,0.5)
y=np.sin(2*np.pi*f*x/fs)
plt.subplot(1,5,1)
plt.plot(x,y)
b=np.cos(2*np.pi*f*x/fs)
plt.subplot(1,5,2)
plt.plot(x,b)
c=y+b
plt.subplot(1,5,3)
plt.plot(x,c)
d=y-b
plt.subplot(1,5,4)
plt.plot(x,d)
plt.show()
plt.stem(x,y)
plt.show()

