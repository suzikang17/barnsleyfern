import numpy as np
import random
import pylab as pl
import matplotlib


# define some matrices that are transformation
w1 = [np.matrix([[.7,-.5242],[.2121,.8]]), np.matrix([[1.5],[1.4]])]
w2 = [np.matrix([[-.32,.3424],[.1212,.15]]), np.matrix([[5],[.5]])]
w3 = [np.matrix([[.18,-.14],[.09,.18]]), np.matrix([[1],[1]])]
w4 = [np.matrix([[-.7,0],[0,-.7]]), np.matrix([[-.1],[15]])]

# set probabilities of each transformation
p1 = .9
p2 = .1

p3 = .05
p4 = .3


# initialize
x_0 = 0 
y_0 = 0
n = 10000 # number of iterations

point = np.matrix([[x_0],[y_0]])


i=0
# pick function depending on probs
for c in range(n):
#        for c in ['b','g','r','c','m','y']:

    # color = 'y'
    r = random.random()
    markerstyle='*'
    if r <= p1:
        point = w1[0] * point + w1[1]
        if c > 5000:
            pl.plot(point.flat[0], point.flat[1], color='k',  marker=markerstyle)
    elif r <= p1 + p2:
        point = w2[0] * point + w2[1]
        if c > 5000:
            pl.plot(point.flat[0], point.flat[1], color='y',  marker=markerstyle)
        # print point
    elif r <= p1 + p2 + p3:
        point = w3[0] * point + w3[1]
        pl.plot(point.flat[0], point.flat[1], color=color,  marker=markerstyle)
    else:
        point = w4[0] * point + w4[1]
        pl.plot(point.flat[0], point.flat[1],color='m', marker=markerstyle)

#pl.xlim(-2.4, 2.9)
#pl.ylim(0,11)

pl.show()    
