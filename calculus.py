"""
This module implements different integration and root finding algorithms
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def dummy():
    """ 
    dummy function for template file
    """
    return 0

def trapezoid_numpy(func, l_lim, u_lim, steps=10000):
    '''
    Function to implement trapezoidal rule using numpy and plot the result
    '''
    x = np.linspace(l_lim, u_lim, steps+1)  # create a linear grid between upper and lower limit
    y = func(x) # evaluate the function on the grid
    integral_value = np.trapezoid(y, x) # calculate the integral using numpy

    integral_function = np.zeros(len(x))    # a zero array for integral at each point

    for i in range(1, len(x)):
        # calculate the integral at each x for plotting
        integral_function[i] = np.trapezoid(y[:i+1], x[:i+1])

    # plotting the original and integrated functions
    plt.plot(x, y, label = '$f(x)$')
    # plt.plot(x[:-1], integral_function, label = '$\\int_a^b f(x) dx$')
    plt.plot(x, integral_function,
             label = 'shaded area under $y = f(x)$: $\\int f(t) dt = $'+str(integral_value))
    plt.fill_between(x, y, 0)
    plt.ylabel('y(x)')
    plt.xlabel('x')
    plt.title('integral using numpy trapezoidal method; steps = '+str(steps))
    plt.legend()

    return integral_value

def trapezoid_scipy(func, l_lim, u_lim, steps=10000):
    '''
    Function to implement trapezoidal rule using scipy and plot the result
    '''
    x = np.linspace(l_lim, u_lim, steps+1)  # create a linear grid between upper and lower limit
    y = func(x)    # evaluate the function on the grid
    integral_value = sp.integrate.trapezoid(y, x)   # calculate the integral using numpy

    integral_function = np.zeros(len(x))    # a zero array for integral at each point

    for i in range(1, len(x)):
        # calculate the integral at each x for plotting
        integral_function[i] = sp.integrate.trapezoid(y[:i+1], x[:i+1])

    # plotting the original and integrated functions
    plt.plot(x, y, label = '$f(x)$')
    plt.fill_between(x, y, 0)
    # plt.plot(x[:-1], integral_function, label = '$\\int_a^b f(x) dx$')
    plt.plot(x, integral_function,
             label = 'shaded area under $y = f(x)$: $\\int f(t) dt = $'+str(integral_value))
    plt.title('integral using scipy trapezoidal method; steps = '+str(steps))
    plt.ylabel('y(x)')
    plt.xlabel('x')
    plt.legend()

    return integral_value
