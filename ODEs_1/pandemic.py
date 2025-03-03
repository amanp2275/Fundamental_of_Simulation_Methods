#http://faculty.sfasu.edu/judsontw/ode/html-20220730/systems05.html
#https://www.nature.com/articles/s41598-021-95494-6
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 17})

a=1.0 #0.05
b=0.2

euler=True

#s=susceptible, i=infected, r=recovered (assuming that they do not get sick again)
def ode(s,i,r):
    ds=-a*s*i
    di=a*s*i-b*i
    dr=b*i
    return ds,di,dr



def euler(h,s,i,r):
    ds,di,dr=ode(s,i,r)
    
    s+=h*ds
    i+=h*di
    r+=h*dr
    return s,i,r


def midpoint(h,s,i,r):
    ds,di,dr=ode(s,i,r)
    
    k1s=0.5*h*ds
    k1i=0.5*h*di
    k1r=0.5*h*dr

    ds,di,dr=ode(s+k1s,i+k1i,r+k1r)
    k2s=h*ds
    k2i=h*di
    k2r=h*dr

    s+=k2s
    i+=k2i
    r+=k2r
    return s,i,r


##main
s=0.95
i=0.05
r=0.0


t=0.
tf=20. #10 Myr

h=0.1


fig,ax=plt.subplots(1,1)

while(t<tf):
    ax.scatter(t,s,s=17,color="blue")
    ax.scatter(t,i,s=17,color="red")
    ax.scatter(t,r,s=17,color="grey")
    #s,i,r=midpoint(h,s,i,r)
    if(euler):
        s,i,r=euler(h,s,i,r)
    else:
        s,i,r=midpoint(h,s,i,r)
    t+=h

print(s,i,r)

#ax.set_xlabel("Time (Myr)")
ax.set_xlabel("Time (days)")

ax.set_ylabel("Fraction")
ax.legend(["Susceptible","Infected","Recovered"])

plt.tight_layout()
plt.show()
    
