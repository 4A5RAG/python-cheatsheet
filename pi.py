from numpy import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000 #darts thrown

circlex = []
circley = []

squarex = []
squarey = []

i = 1

while i< N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2 <= 1):
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
    i += 1
    
pi = 4*len(circlex)/float(N)
    
print("Pi is appoximately ", pi)

print("Pi is actually ", np.pi)

plt.plot(circlex,circley, 'b.')
plt.plot(squarex,squarey,'g.')
plt.savefig("Pi")
