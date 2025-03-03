### example by MMapelli ###
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.rcParams.update({'font.size': 17})


scheme="rk4"

def ode(x,t):
    dx=-x**3+np.sin(t)
    return dx

def euler(x,t,h):
    k1=ode(x,t)
    x=x+h*k1
    return x

def mid(x,t,h):
    k1=ode(x,t)
    k2=ode(x+0.5*h*k1,t+0.5*h)
    x=x+h*k2
    return x

def rk2(x,t,h):
    k1=ode(x,t)
    k2=ode(x+h*k1,t+h)
    x=x+h*0.5*(k1+k2)
    return x

def rk4(x,t,h):
    k1=ode(x,t)
    k2=ode(x+0.5*h*k1,t+0.5*h)
    k3=ode(x+0.5*h*k2,t+0.5*h)
    k4=ode(x+h*k3,t+h)
    x=x+h*(k1+2.*k2+2.*k3+k4)/6.
    return x

#main
x=0.0
h=0.1
t=0.0
tf=100.


xp=[x]
tp=[t]
while(t<tf):
    if(scheme=="euler"):
        x=euler(x,t,h)
    elif(scheme=="midpoint"):
        x=mid(x,t,h)
    elif(scheme=="rk2"):
        x=rk2(x,t,h)
    elif(scheme=="rk4"):
        x=rk4(x,t,h)
    else:
        print("I do not understand this scheme. Please tell me more about it. :)")
        exit()
    t+=h
    xp.append(x)
    tp.append(t)


## now with scipy.integrate.odeint()
t=0
x=0
tnew=np.arange(t,tf,h)    
sol=odeint(ode,x,tnew)
plt.plot(tp,xp,color="blue",lw=5)
plt.plot(tnew,sol,ls="-.",color="red",lw=2)

plt.xlabel("Time (s)")
plt.ylabel("x(t)")
plt.tight_layout()
plt.show()
