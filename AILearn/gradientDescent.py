# Williams Villalba - January, 6th 2022
# Compute the Gradient Descendent
import numpy as np
import computeCost

def Gd(X, y, theta, alpha, num_iters):
    
    m1=len(y)
    
    J_history=np.zeros((num_iters,1))
    h=np.zeros((X.shape[0],1))
    
    for iter in range(0,num_iters):  
        for k in range(0,m1):
            h[k,0]=theta[0]*X[k,0] + theta[1]*X[k,1]
        
        theta[0]= theta[0]-alpha*(1/m1)*(np.sum(h-y))
    
        p1=X[:,1]
        p2=np.array([p1]).T
   
        theta[1] = theta[1]-alpha*(1/m1)*(np.sum((h-y)*p2)) 
    
        J_history[iter]= computeCost.J_Cost(X,y,theta)  
   
    return(theta,J_history)