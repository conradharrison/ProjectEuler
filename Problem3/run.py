from math import sqrt

def f_not_divisible_by_primelist(L, f):
    for i in L:
        if (f%i == 0):
            return False
    return True

N = 13195
N = 600851475143

done = False
f = 2
maxf = f
L = []

while (not done):
    if (N % f == 0):
        if (f==2 or f_not_divisible_by_primelist(L, f)):
            L.append(f)
            if (f > maxf):
                maxf = f
    f = f + 1
    if (f > sqrt(N)):
        done = True

print maxf

        
