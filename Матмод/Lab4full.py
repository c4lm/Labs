import numpy as np
import sys
def norm_U(i=10):
    a=[[0 for x in range(0,i)]for x in range(0,i)]
    for x in range(0,i):
        for y in range(0,i):
            if(x<y):
                a[x][y]=0
            elif(x==y):
                a[x][y]=1
            elif(x>y):
                a[x][y]=-2
    print(a)
    max=0
    for l in a:
        t=sum(l)
        if(max<t):
            max=t
    #print(max)
    u=max
    inverse=np.linalg.inv(a)
    max=0
    for l in inverse:
        t=sum(l)
        if(max<t):
            max=t
    print(max*u)
    
print("Normas: ")
for x in range(3,11):
    norm_U(x)
'''                    
9.0
27.0
81.0
243.0
729.0
2187.0
6561.0
19683.0'''
print()

i=32
b=[]
a=[[0 for x in range(0,i)]for x in range(0,i)]
for x in range(0,i):
    if(x%2 == 0):
        b.append(1)
    else:
        b.append(-1/3)
    for y in range(0,i):
        if(x<y):
            a[x][y]=0
        elif(x==y):
            a[x][y]=1
        elif(x>y):
            a[x][y]=-2
x_np=np.linalg.solve(a,b)
print("X Via numpy: ")
print(x_np)
y=[]
y.append(b[0])
for x in range(1,32):
    s=0
    row=a[x]
    for j in range(0,x):
        s=s+row[j]*y[j]
    y.append(b[x]-s)
print("X=Y from LUX=B :")
print(y) # Lx=y, our L,U from LUX=Y are UEX=Y, U is diagonal => Y==X
x_lu=y
b_approx=[]
for row in a:
    s=0
    for x in range(0,32):
        s=s+row[x]*x_lu[x]
    b_approx.append(s)
residual_lu=[]
for x in range(0,32):
    residual_lu.append(b[x] - b_approx[x])
print("Residual for LU:")
print(residual_lu)
print("\n \n \n")
q_np,r_np=np.linalg.qr(a)
print("Q via numpy: ")
print(q_np)
print("R via numpy: ")
print(r_np)
y=np.dot(q_np.T,b)
x_qr=np.linalg.solve(r_np,y)
print("X for QR: ")
print(x_qr)
b_approx=[]
for row in a:
    s=0
    for x in range(0,32):
        s=s+row[x]*x_qr[x]
    b_approx.append(s)
residual_qr=[]
for x in range(0,32):
    residual_qr.append(b[x] - b_approx[x])
print("Residual for LU again: ")
print(residual_lu)
print("Residual for QR: ")
print(residual_qr)
print("Epsilon: {0}".format(sys.float_info.epsilon))

