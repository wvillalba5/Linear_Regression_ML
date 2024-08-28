
# Williams Villalba - January, 6th 2022
# COMPUTECOST Compute cost for linear regression
def  J_Cost(X,y,theta):
    J = 0.0
    h=X @ theta

    for i in range(0,len(y),1):
        J = J + (h[i] - y[i])**2   
    J = J/(2*len(y))
    return (J)
