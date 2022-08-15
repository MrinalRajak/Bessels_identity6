
#Bessel's identity
#(6) x*jn'(n,x) + n*jn(n,x) = x*jn(n-1,x)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=int(input("Enter the n: "))
x=float(input("Enter the x: "))

def Bessels(x):
    return jn(n,x)
def der_Bessels(x):
    return derivative(Bessels,x,order=39)

LHS=x*der_Bessels(x)+n*jn(n,x)
RHS=x*jn(n-1,x)

print("LHS: ",LHS)
print("RHS: ",RHS)
