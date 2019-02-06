import scipy.io.wavfile as wav
import numpy as a
import matplotlib.pyplot as plt
fs,data=wav.read('p.wav')
print(fs,len(data),data)
plt.subplot(2,1,1)
plt.plot(data)
t=a.arange(0,len(data)/fs,1.0/fs)
plt.subplot(2,1,2)
plt.plot(t,data)
plt.show()
wav.write('p-slow',0.5*fs,data)
wav.write('k-fast',3*fs,data)

