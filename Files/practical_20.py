'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP to implement Linear Regression using Python.

'''
#***************Code of the Program****************

print("Welcome to the program")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
x = 50 * np.random.random((20, 1))
y = 2 * x + 1.0 + np.random.normal(size=x.shape)

model = LinearRegression() 
model.fit(x, y)

x_new = np.linspace(0, 50, 100)
y_new = model.predict(x_new[:, np.newaxis])

plt.figure(figsize=(5, 5)) 
ax = plt.axes() 
ax.scatter(x, y) 
ax.plot(x_new, y_new)

ax.set_xlabel('x') 
ax.set_ylabel('y')

plt.show()

'''
********* OUTPUT **********


'''