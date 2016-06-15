import math,sys
def f(x,a):
    return math.pow(x,2)-a

def get_eps():
    eps=1.0
    while((1.0+eps/2)>1.0):
        eps=eps/2
    return eps

def newton_sqrt(a=10.0002, step=0.2):
    x=1.0
    if(step<0):
        step=0.1
    if(a<0):
        a=10
    while(a<100):
        eps=get_eps()*a
        while(abs(f(x,a)) > eps):
            x=x-(f(x,a)/(2*x))
        a=a+step
    #print("Machine epsilon: %.52f" % (7./3 - 4./3 -1))
    #print("Machine epsilon from sysinfo: %.52f" % (sys.float_info.epsilon))
    print("Absolute epsilon by division %.52f" % (get_eps()))
    print("Root of number %.52f" % a)
    print("Epsilon is %.52f" % eps)
    print("root is %.52f" % (math.sqrt(a)))
    print("Calculated root is %.52f" % x)
    print("Calculated eps is %.52f" % (abs(x-math.sqrt(a))/math.sqrt(a)))
    print()

if(__name__=="__main__"):
    newton_sqrt(a=50.005,step=1.0)
    newton_sqrt(a=50.005,step=0.2)
    newton_sqrt(a=10.005,step=1.0)
    newton_sqrt(a=10.005,step=0.2)
    
