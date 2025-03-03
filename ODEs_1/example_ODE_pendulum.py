### example by MMapelli ###
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.rcParams.update({'font.size': 17})

gl=1. #g/l

scheme="rk4"

def ode(qw):
    dq=qw[1]
    dw=-gl*np.sin(qw[0])
    return np.array([dq,dw],float)

def euler(qw,h):
    k1=ode(qw)
    qw=qw+h*k1
    return qw

def mid(qw,h):
    k1=ode(qw)
    k2=ode(qw+0.5*h*k1)
    qw=qw+h*k2
    return qw

def rk2(qw,h):
    k1=ode(qw)
    k2=ode(qw+h*k1)
    qw=qw+h*0.5*(k1+k2)
    return qw

def rk4(qw,h):
    k1=ode(qw)
    k2=ode(qw+0.5*h*k1)
    k3=ode(qw+0.5*h*k2)
    k4=ode(qw+h*k3)
    qw=qw+h*(k1+2.*k2+2.*k3+k4)/6.
    return qw

def ode2(qw,t):
    dq=qw[1]
    dw=-gl*np.sin(qw[0])
    return np.array([dq,dw],float)


#main
q0=60.*np.pi/180.
w0=0.0
h=0.1
t=0.0
tf=30.

tp=[t]
q=[q0]
w=[w0]
qw=np.array([q0,w0],float)

while(t<tf):
    if(scheme=="euler"):
        qw=euler(qw,h)
    elif(scheme=="midpoint"):
        qw=mid(qw,h)
    elif(scheme=="rk2"):
        qw=rk2(qw,h)
    elif(scheme=="rk4"):
        qw=rk4(qw,h)
    else:
        print("I do not understand this scheme. Please tell me more about it. :)")
        exit()
    t+=h

    q.append(qw[0])
    w.append(qw[1])
    tp.append(t)





## now with scipy.integrate.odeint()
t=0.0
qw=np.array([q0,w0],float)

tnew=np.arange(t,tf,h)    
sol=odeint(ode2,qw,tnew)

plt.plot(tp,q,color="green",lw=5,label="$q(t)$")
plt.plot(tp,w,color="red",lw=5,label="$\\frac{dq}{dt}(t)$")
plt.plot(tnew,sol[:,0],ls="-.",color="black",lw=2)
plt.plot(tnew,sol[:,1],ls="-.",color="black",lw=2)
plt.legend()

plt.xlabel("Time (s)")
plt.ylabel("")
plt.tight_layout()
plt.show()
