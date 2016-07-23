import numpy as np
import random
import pylab as pl
import matplotlib


# define some matrices that are transformations
w1 = np.matrix([[0,0],[0,.16]])
w2 = [np.matrix([[.85, .04],[-.04, .85]]), np.matrix([[0],[1.6]])]
w3 = [np.matrix([[.2,-.26],[.23,.22]]), np.matrix([[0],[1.6]])]
w4 = [np.matrix([[-.15,.28],[.26,.24]]), np.matrix([[0],[.44]])]

# set probabilities of each transformation
p1 = .01
p2 = .85
p3 = .07
p4 = .07


# initialize
x_0 = 0 
y_0 = 0
n = 1000 # number of iterations

point = np.matrix([[x_0],[y_0]])


i=0
# pick function depending on probs
for c in range(n):

    # print r
    for c in ['b','g','r','c','m','y']:
        color = c
        #print color
        r = random.random()
        markerstyle='2'
        if r <= p1:
            point = w1 * point  
            pl.plot(point.flat[0], point.flat[1], color=color,  marker=markerstyle)
        elif r <= p1 + p2:
            point = w2[0] * point + w2[1]
            pl.plot(point.flat[0], point.flat[1], color=color,  marker=markerstyle)
            # print point
        elif r <= p1 + p2 + p3:
            point = w3[0] * point + w3[1]
            pl.plot(point.flat[0], point.flat[1], color=color,  marker=markerstyle)
        else:
            point = w4[0] * point + w4[1]
            pl.plot(point.flat[0], point.flat[1],color=color, marker=markerstyle)
    
pl.xlim(-2.4, 2.9)
pl.ylim(0,11)

pl.show()    
