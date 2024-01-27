'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - 

'''
#***************Code of the Program****************
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data = np.random.poisson(lam=6, size=1000)  


def poisson_distribution(x, mu):
    return poisson.pmf(x, mu)


params, covariance = curve_fit(poisson_distribution, np.arange(max(data)+1), np.bincount(data))

lambda_fit = params[0]


x_fit = np.arange(0, max(data) + 1)


y_fit = poisson_distribution(x_fit, lambda_fit)

plt.hist(data, bins=np.arange(-1, max(data) + 1.5, 1), density=True, label='Data Histogram')


plt.plot(x_fit, y_fit, 'r-', label=f'Fitted Poisson Distribution (lambda={lambda_fit:.2f})')


plt.xlabel('X')
plt.ylabel('P(X)')
plt.legend()


plt.show()



'''
********* OUTPUT **********


'''