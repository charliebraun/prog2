import random
import matplotlib.pyplot as plt
import math
import concurrent.futures as future
from time import sleep as pause

def find_pi(n=1000, show=True):
    xs_in = []
    ys_in = []
    xs_out = []
    ys_out = []
    for i in range(n):
        #Slumpar punkt
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        #Kollar om i cirkel,lägger i rätt lista
        if (x*x+y*y) > 1:
            xs_out.append(x)
            ys_out.append(y)
        else:
            xs_in.append(x)
            ys_in.append(y)
    #Plotgrejs
    plt.gca().add_patch(plt.Circle((0,0),1,fill=False))
    plt.scatter(xs_in,ys_in,c='r')
    plt.scatter(xs_out,ys_out,c='b')
    if show:
        plt.show()
    return 4*len(xs_in)/n

def find_volume_d(n=100000, d=2):
    n_s = [[random.uniform(-1,1)**2 for i in range(d)] for ii in range(n)]
    ds = list(map((lambda x: sum(x)), n_s))
    ins = len(list(filter(lambda x: x<=1, ds)))
    print(2**d*ins/n)
    return 2**d*ins/n

def analytical_volume_d(d=2):
    return math.pi**(d/2)/(math.gamma(d/2+1))

def find_volume_d_mult(n=100000, d=2):
    s = 0
    with future.ThreadPoolExecutor() as ex:
        small_n = [n/10]*10
        results = ex.map((lambda x: find_volume_d(x,d)), small_n)
        for r in results:
            print(r)
    return s

#Del 1.1
##for i in [1000, 10000, 100000]:
##    print(find_pi(i))

#Del 1.2
##for i in [2, 5, 11, 10, 15]:
##    print(i, ': Monte-Carlo:', find_volume_d(d=i), '\t', ' - Analytical:', analytical_volume_d(i))

#Del 1.3
print(find_volume_d_mult())
