
import numpy as np
import random
import pylab as pl
import matplotlib


# define some matrices that are transformations
w1 = np.matrix([[.5,0],[0,.5]])
w2 = [np.matrix([[.5,0],[0,.5]]), np.matrix([[.5],[0]])]
w3 = [np.matrix([[.5,0],[0,.5]]), np.matrix([[0],[.5]])]
w4 = [np.matrix([[.5,0],[0,.5]]), np.matrix([[.5],[.5]])]

# set probabilities of each transformation
p1 = .33
p2 = .33
p3 = .34
p4 = 1


# initialize
x_0 = 0 
y_0 = 0
n = 5000 # number of iterations

point = np.matrix([[x_0],[y_0]])


i=0
# pick function depending on probs
for c in range(n):

    # print r
    for c in ['b','k','g']:
        color = c
        #print color
        r = random.random()
        markerstyle='^'
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
    
#pl.xlim(-2.4, 2.9)
#pl.ylim(0,11)

pl.show()    
