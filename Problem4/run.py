maxc = 810000
for a in range(900, 999):
    for b in range(900, 999):
        c = a*b
        if (c%10 == int(c/100000)%10 and 
            int(c/10)%10 == int(c/10000)%10 and
            int(int(c/10)/10)%10  == int(c/1000)%10):
            if (c > maxc):
                maxc = c

print maxc
