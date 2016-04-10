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

    def update(self, value):

        line_width=2
        font_size=16
        
        ## Range in X axis, Frequency in GHz
        xmin=1
        xmax=4
        ## Range in Y axis, Left, S11 in db
        ymin1=-25
        ymax1=0
        ## Range in Y axis, Right, Axial Ratio
        ymin2=0
        ymax2=5

        data1 = np.genfromtxt('AR.csv', dtype=None, delimiter=',', skip_header=1)
        data2 = np.genfromtxt('S11.csv', dtype=None, delimiter=',', skip_header=1)
        self.freq1=data1[:,0]
        self.s11=data1[:,1]
        self.freq2=data2[:,0]
        self.AR=data2[:,1]
           
        ## Subplot, first plot S11 
        self.fig, self.ax1 = plt.subplots()
        self.p1=self.ax1.plot(self.freq1,self.s11,linestyle='--',color='r', linewidth=line_width, label='|S11|')
    
        ## ax1.set_title('S11 and Axial Ratio')
        self.ax1.set_xlabel('Frequency (in GHz)',fontsize=font_size)
        self.ax1.set_ylabel('|S11| (dB)',fontsize=font_size)
        self.ax1.set_xlim(xmin, xmax)
        self.ax1.set_ylim(ymin1,ymax1)
    
        ## Draw horizontal line along y=-10 db
        self.plt.axhline(y=-10,linestyle='-.',color='r',linewidth=0.5)
        ## Draw vertical shaded region 
        x_min_sd=1.62
        x_max_sd=3.06
        self.plt.axvspan(x_min_sd,x_max_sd, facecolor='g', alpha=0.1)
    
        ## Now plot Axial Ratio, right side
        self.ax2 = self.ax1.twinx()
        self.p2=ax2.plot(self.freq2,self.AR,linestyle='-',color='b', linewidth=line_width, label='Axial Ratio')
    
        self.ax2.set_ylabel('Axial Ratio (dB)',fontsize=font_size)
        self.ax2.set_xlim(xmin, xmax)
        self.ax2.set_ylim(ymin2, ymax2)
           
        ## Draw horizontal line along y=3 (for CP)
        self.plt.axhline(y=3,linestyle='-.',color='b',linewidth=0.5)
        
        
        value = int(value / self.inc) * self.inc
        data = np.genfromtxt('AR_stub_pos.csv', dtype=None, delimiter=',', skip_header=1) 
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