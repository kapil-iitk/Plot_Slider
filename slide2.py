import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

class ChangingPlot(object):
    def __init__(self):

	data = np.genfromtxt('AR.csv', dtype=None, delimiter=',', skip_header=1) 
	[aa,bb]=data.shape
	self.bb=int(bb)
	self.freq=data[:,0]
	self.AR_sim=data[:,1]

        # change this for the stepsize
        self.inc = 1.0 

        self.fig, self.ax = plt.subplots()
        self.sliderax = self.fig.add_axes([0.2, 0.02, 0.6, 0.03], axisbg='yellow')

        self.slider = Slider(self.sliderax, 'Value', 0, self.bb, valinit=self.inc)
	
        self.slider.on_changed(self.update)
        self.slider.drawon = False
	
    	self.dot, = self.ax.plot(self.freq, self.AR_sim)
	self.ax.axhline(y=3,linestyle='-.',color='b',linewidth=0.5)
    def update(self, value):
        value = int(value / self.inc) * self.inc
	data = np.genfromtxt('AR.csv', dtype=None, delimiter=',', skip_header=1) 
	[aa,bb]=data.shape
	self.freq=data[:,0]
	self.AR_sim=data[:,[value]]
	self.dot.set_data([self.freq,self.AR_sim])
        self.slider.valtext.set_text('{}'.format(value))
        self.fig.canvas.draw()

    def show(self):
        plt.show()

p = ChangingPlot()
p.show()