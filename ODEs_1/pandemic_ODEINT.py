import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 17})

a=1.0 #0.05
b=0.2


#s=susceptible, i=infected, r=recovered (assuming that they do not get sick again)
def ode(y,t,a,b):
    
    s,i,r = y
    
    ds=-a*s*i
    di=a*s*i-b*i
    dr=b*i
    
    return (ds,di,dr)


t=np.linspace(0.,20.,200)

s=0.95
i=0.05
r=0.0
y=(s,i,r)

sol = odeint(ode,y,t,args=(a,b))





plt.plot(t, sol[:, 0], 'b', label='susceptible')

plt.plot(t, sol[:, 1], 'r', label='infected')

plt.plot(t, sol[:, 2], 'grey', label='recovered')

plt.legend()

plt.xlabel("Time (days)")

plt.ylabel("Fractions")

plt.show()
