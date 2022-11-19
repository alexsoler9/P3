import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

senyal, fm = sf.read('fonema_sonoro_a_30ms.wav')
t = np.arange(0, len(senyal)) / fm

fig, (g1, g2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=0.5)

autocorrelation = t

for i in range(len(senyal)):
    for k in range(len(senyal)-i):
        autocorrelation[i] = autocorrelation[i] + senyal[k] * senyal[k+i-1]
    autocorrelation[i] = autocorrelation[i]  / len(senyal)

g1.plot(senyal)
g1.grid(True)
g1.set_title('Señal temporal')
g1.set_xlabel('Muestras')
g1.set_ylabel('Amplitud')

g2.plot(autocorrelation)
g2.grid(True)
g2.set_title('Autocorrelación')
g2.set_xlabel('Muestras')
g2.set_ylabel('r(k)')

plt.show()