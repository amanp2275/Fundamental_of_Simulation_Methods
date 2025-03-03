import numpy as np

import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 17})


def explicit_euler(x0, alpha, h, tf):
    num_steps = int(tf/h)
    time = np.linspace(0, tf, num_steps+1)
    x = np.zeros(num_steps+1)
    x[0] = x0

    for i in range(num_steps):
        x[i+1] = x[i] * (1.0 - alpha * h)

    return time, x



def implicit_euler(x0, alpha, h, tf):
    num_steps = int(tf/h)
    time = np.linspace(0, tf, num_steps+1)
    x = np.zeros(num_steps+1)
    x[0] = x0

    for i in range(num_steps):
        x[i+1] = x[i]/(1.0 + alpha * h)

    return time, x

# Input parameters:
x0 = 1.0
alpha = [0.1,0.5,1.0,1.01]
h = 2.0
tf = 100.0

for i in range(len(alpha)):


    time_e, sol_e = explicit_euler(x0, alpha[i], h, tf)
    time_i, sol_i = implicit_euler(x0, alpha[i], h, tf)

    t=np.linspace(0, tf, int(1e6))
    plt.plot(time_e, sol_e, label='Explicit Euler', color="blue")
    plt.plot(time_i, sol_i, label='Implicit Euler', color="red")
    plt.scatter(time_e, sol_e, marker="o", color="blue")
    plt.scatter(time_i, sol_i, marker="o", color="red")
    plt.plot(t, np.exp(-alpha[i]*t), label="Analytic", color="black")
    plt.text(10.,1.1*max(sol_e),"$h= $"+str(h)+", $2./\\alpha=$ "+str(2./alpha[i]), fontsize=13)
    plt.ylim([1.2*min(sol_e),1.2*max(sol_e)])
    plt.xlabel('Time $t$')
    plt.ylabel('$x(t)$')
    if(alpha[i]<=1.0):
        plt.legend(loc="center right",fontsize=13)
    else:
        plt.legend(loc="lower left",fontsize=13)
    plt.tight_layout()
    plt.show()
