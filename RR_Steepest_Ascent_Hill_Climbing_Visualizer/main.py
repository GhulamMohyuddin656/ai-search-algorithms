import random
import gui as g
def f(x):
    return -x**4 + 4*x**2 + x

def steepestAscentHillClimbing(ax,x,step):
    while True:
        g.plotPoint(ax,x,f(x))
        current_value=f(x)
        left=x-step
        right=x+step
        best=max(f(left),f(right))
        if best>current_value:
            if best==f(left):
                x=left
            else:
                x=right    
        else:
            break
    return x


def exit_program(event):
    g.p.close()
    print("\nBest Solution Found")
    print("Starting point:", round(best_start,2))
    print("Best x:", round(best_x,2))
    print("Best f(x):", round(best_value,2))

def random_restart(event):

    global restart_count,ax,restarts,step,best_start,best_value,best_x
    if restart_count>=restarts:
        print("All restarts finished")
        exit_program(None)
        return
    
    g.reset_plot(ax)
    restart_count+=1
    restart_text = ax.text(
        0.02, 0.95,
        f"Restarts Left: {restarts - restart_count}",
        transform=ax.transAxes,
        fontsize=12
    )
    g.p.draw()
    start=random.uniform(-10,10)
    result=steepestAscentHillClimbing(ax,start,step)
    value=f(result)
    print("Start: ",round(start,2),
            "Final: ",round(result,2),
            "Value: ",round(value,2))
    if value>best_value:
        best_value=value
        best_start=start
        best_x=result
    
    
  
fig,ax,start_btn,end_btn=g.gui()

best_x=None
best_value=float('-inf')
best_start=None    
restarts=10
restart_count=0
step=0.1    
restart_text = ax.text(
    0.02,0.95,
    f"Restarts Left: {restarts}",
    transform=ax.transAxes,
    fontsize=12
) 

start_btn.on_clicked(random_restart)
end_btn.on_clicked(exit_program)
g.p.show(block=True)