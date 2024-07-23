from ipywidgets import interact
import numpy as np
import matplotlib.pyplot as plt
def plot_sine_wave(frequency=1.0):
   x = np.linspace(0, 2*np.pi, 1000)
   y = np.sin(frequency * x)
   plt.plot(x, y)
   plt.show()
interact(plot_sine_wave, frequency=(0.5, 10.0))