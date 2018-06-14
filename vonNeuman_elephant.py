"""
vonNeuman_elephant.py
    "With four parameters I can fit an elephant,
       and with five I can make him wiggle his trunk."

Original Version
    Author: Piotr A. Zolnierczuk (zolnierczukp at ornl dot gov)
    Retrieved on 14 September 2011 from
    http://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant/
Modified to wiggle trunk:
    2 October 2011 by David Bailey (http://www.physics.utoronto.ca/~dbailey)

Based on the paper:
    "Drawing an elephant with four complex parameters", by
    Jurgen Mayer, Khaled Khairy, and Jonathon Howard,
    Am. J. Phys. 78, 648 (2010), DOI:10.1119/1.3254017

    The paper does not specify how the wiggle parameter controls the
    trunk, so a guess was made.

Inspired by John von Neumann's famous quote (above) about overfitting data.
    Attributed to von Neumann by Enrico Fermi, as quoted by
      Freeman Dyson in "A meeting with Enrico Fermi" in
      Nature 427 (22 January 2004) p. 297 
"""

import matplotlib, time
# Explicitly choose normal TkAgg Backend, in case your python installation
#       does not already have a suitable choice in your matplotlibrc file.
#       This line may be deleted if the script runds without it. See
# http://matplotlib.sourceforge.net/faq/installing_faq.html#what-is-a-backend.
matplotlib.use('TKAgg')        

from matplotlib import pyplot
from numpy import append, cos,  linspace, pi, sin, zeros

# elephant parameters
p = [ 50 - 30j,
      18 +  8j,
      12 - 10j,
     -14 - 60j, 
      40 + 20j ] # Set p[4].real=0 to stop trunk wiggling

def fourier(t, C):
    f = zeros(t.shape) # initialize fourier values to zero
    for k in range(len(C)):
        f += C.real[k]*cos(k*t) + C.imag[k]*sin(k*t)
    return f

def elephant(t, p):
    npar = 6
    Cx = zeros((npar,), dtype='complex')
    Cy = zeros((npar,), dtype='complex')

    Cx[1] = p[0].real*1j
    Cy[1] = p[3].imag + p[0].imag*1j

    Cx[2] = p[1].real*1j
    Cy[2] = p[1].imag*1j

    Cx[3] = p[2].real
    Cy[3] = p[2].imag*1j

    Cx[5] = p[3].real


    x =  append(fourier(t,Cy), [p[4].imag])
    y = -append(fourier(t,Cx), [-p[4].imag])

    return x,y

fig = pyplot.figure()
plt = fig.add_subplot(111)

def LivePlot():
    trunk, = plt.plot([],[])    # initialize trunk
    # draw the body of the elephant
    x, y = elephant(linspace(0.4+1.3*pi,2*pi+0.9*pi,1000), p)
    body = plt.plot(x,y,'r.')
    # wiggle trunk
    for i in range(0,10000):
        # create trunk
        x, y = elephant(linspace(2*pi+0.9*pi,0.4+3.3*pi,1000), p)
        # move trunk to new position (but don't move eye stored at end or array)
        for ii in range(len(y)-1):
            y[ii] -= sin(((x[ii]-x[0])*pi/len(y)))*sin(float(i))*p[4].real
        plt.lines.remove(trunk) # remove old trunk before drawing at new position
        trunk, = plt.plot(x,y,"r.")
        fig.canvas.draw()
        time.sleep(0.1) # wait a bit so the trunk doesn't wiggle too fast

fig.canvas.manager.window.after(100,LivePlot) # After 100ms, call animate
pyplot.show()