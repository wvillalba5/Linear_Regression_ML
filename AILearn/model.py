from numpy import loadtxt

import numpy as np
import computeCost 
import gradientDescent


from numpy import loadtxt

class Model:

    def __init__(self) -> None:

        pass

    def read_file(self,path_file):
        self.data= loadtxt(path_file, dtype=float,comments='#', delimiter=',',unpack=False)
        self.X=self.data[0:self.data.shape[0],0] 
        self.y=self.data[0:self.data.shape[0],1] 
        self.m=self.data.shape[0]

        

    def calling_Cost_Function(self,theta0, theta1,iter_num,Alpha):
        self.X1 = np.hstack((np.ones((self.m,1)),np.array([self.X]).T))
        self.y1= np.array([self.y]).T
        self.theta = np.array([[theta0],[theta1]])
        self.J= computeCost.J_Cost(self.X1,self.y1,self.theta)
       
        [self.theta_m, J_history] = gradientDescent.Gd(self.X1, self.y1, self.theta, Alpha, iter_num) 
        

    def predictions(self,Value_predicted):
        value_p1=np.array([1, float(Value_predicted)])
        self.predict1 = value_p1 @ self.theta_m
       

