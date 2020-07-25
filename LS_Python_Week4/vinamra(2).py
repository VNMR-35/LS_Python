import numpy as np
from matplotlib import pyplot as plt

#Defining the population
popul = np.zeros((100, 150), dtype=int)
popul[50, 75] = 1
#Plot parameters
n = 0
ones = [1]
change = [0]

#Iterations
while True:
    prob = np.zeros((100, 150))    #This array stores probability for each 0 to convert to 1
    change.append(0)
    ones.append(0)
    
    for i in range(8):  #Swapping 8 random elements with 8 other
        a = np.random.randint(0, 100)
        b = np.random.randint(0, 150)
        c = np.random.randint(0, 100)
        d = np.random.randint(0, 150)
        popul[a, b], popul[c, d] = popul[c, d], popul[a, b]
    
    for i in range(100):    #Probability calculation for each 0 to convert to 1
        for j in range(150):
            if popul[i, j] == 1:
                continue
            else:
                for k in range(max(i-2, 0), min(i+3, 100)):
                    for l in range(max(j-2, 0), min(j+3, 150)):
                        if (k,l) == (i,j):
                            continue
                        if k==i-2 or k==i+2 or l==j-2 or l==j+2:
                            prob[i, j] += popul[k, l]*0.08
                        else:
                            prob[i, j] += popul[k, l]*0.25
    
    for i in range(100):    #Mass infection!
        for j in range(150):
            if popul[i, j] == 0:
                p = np.array([prob[i, j], 1.00-prob[i, j]])
                popul[i, j] = np.random.choice([1, 0], size=1, p=p)     #Facing the error 'Probabilities are not non-negative' here :(
                if popul[i, j] == 1:
                    change[n] += 1
            else:
                ones[n] += 1
            ones[n] += change[n]
    n += 1
    
    check = 0
    for i in range(100):
        check += all(popul[i])
    if check == 100:
        break

plt.figure()
plt.plot(range(n+1), ones)
plt.plot(range(n+1), change, color='red')
plt.show()