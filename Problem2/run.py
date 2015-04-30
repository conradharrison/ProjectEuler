sum = 0
previous = 0
current = 1
while(sum <= 4000000):
        f = previous + current
        if (f%2 == 0):
                sum = sum + f
        previous = current
        current = f
print sum
