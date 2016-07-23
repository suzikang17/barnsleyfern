import numpy as np
import random
import pylab as pl
import matplotlib


# define some matrices that are transformations
# from peitgen table 5.60
w1 = [np.matrix([[0,0],[0,.16]]), np.matrix([[0.5],[0]])]
w2 = [np.matrix([[.849, .037],[-.037, .849]]), np.matrix([[0.075],[0.1830]])]
w3 = [np.matrix([[.197,-.226],[.226,.197]]), np.matrix([[0.4],[0.049]])]
w4 = [np.matrix([[-.15,.283],[.26,.237]]), np.matrix([[0.575],[-0.084]])]

# set probabilities of each transformation
p1 = .01
p2 = .85
p3 = .07
p4 = .07


# initialize
x_0 = 0.5 
y_0 = 0
n = 10000 # number of iterations

point = np.matrix([[x_0],[y_0]])


# pick function depending on probs
for c in range(n):
    r = random.random()
    markerstyle='2'
    if c > 7000:
        if r <= p1:
            point = w1[0] * point + w1[1] 
            pl.plot(point.flat[0], point.flat[1], color='k',  marker=markerstyle)
        elif r <= p1 + p2:
            point = w2[0] * point + w2[1]
            pl.plot(point.flat[0], point.flat[1], color='g',  marker=markerstyle)
            # print point
        elif r <= p1 + p2 + p3:
            point = w3[0] * point + w3[1]
            pl.plot(point.flat[0], point.flat[1], color='b',  marker=markerstyle)
        else:
            point = w4[0] * point + w4[1]
            pl.plot(point.flat[0], point.flat[1],color='m', marker=markerstyle)

pl.xlim(.2,.9)
pl.ylim(0,1.1)

pl.show()    
