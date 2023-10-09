import math

N1=100 # number of people in group 1
N2=100 # number of people in group 2
X1=7 # number of events in group 1
X2=0 # number of events in group 2
l1=X1/N1 # rate of events in our period for group 1
l2=X2/N2 # rate of events in our period for group 2

Z=(l2-l1)/math.sqrt(l1/N1+l2/N2)

print(Z)