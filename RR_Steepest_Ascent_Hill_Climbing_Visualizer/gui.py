import matplotlib.pyplot as p
import numpy as np
from matplotlib.widgets import Button
import Function as F
xs=[]
ys=[]
line=None
def createWindow():
    fig,ax=p.subplots()
    fig.set_size_inches(8,6)
    fig.canvas.manager.set_window_title("Simple Hill Climb Visualization")
    ax.set_title("Empty Graph")
    ax.set_xlim(-20,20)
    ax.set_ylim(-100,100)
    
    x=np.linspace(-10,10,400)
    y=F.f(x)
    ax.plot(x,y,'b')
    return fig,ax

def plotPoint(ax, x, y):
    global line, xs, ys
    xs.append(x)
    ys.append(y)
    if line is not None:
        line.remove()
    line, = ax.plot(xs, ys, 'ro-')
    p.draw()
    p.pause(0.01)
    
def exit_program(event):
    p.close()



def reset_plot(ax):
    global line, xs, ys
    xs.clear()
    ys.clear()
    line = None
    ax.cla()                      
    ax.set_title("Simple Hill Climb")
    ax.set_xlim(-20, 20)
    ax.set_ylim(-100, 100)
    x = np.linspace(-10, 10, 400)
    y = F.f(x)
    ax.plot(x, y, 'b')
    p.draw()
    
    
def gui():
    p.ion()
    fig,ax=createWindow()
     # START BUTTON
    start_ax=p.axes([0.7,0.02,0.1,0.05])
    start_button=Button(start_ax,"Start")

    # EXIT BUTTON
    exit_ax=p.axes([0.82,0.02,0.1,0.05])
    exit_button=Button(exit_ax,"Exit")

    p.show()

    return fig,ax,start_button,exit_button