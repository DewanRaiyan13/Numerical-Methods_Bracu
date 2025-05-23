# -*- coding: utf-8 -*-
"""Md. Raiyan Uddin_12_Lab3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V56JzKG8Ldf_MXROPTTlIQWg3LFlGUmb

Make sure you remove `raise NotImplementedError()` and fill in any place that says `# YOUR CODE HERE`, as well as your `NAME`, `ID`, and `SECTION` below:
"""

NAME = "Md. Raiyan Uddin"
ID = "21301613"
SECTION = "12"

"""---

# CSE330 Lab: Polynomial Interpolation using Lagrange Form
---

### Importing necessary libraries
"""

import numpy as np
import matplotlib.pyplot as plt

"""### The Lagrange_Polynomial class
General form of an $n$ degree Lagrange polynomial:

\begin{equation}
p_n(x) = \sum_{k=0}^{n} f(x_k)l_k(x) = \sum_{k=0}^{n} y_kl_k(x),\tag{1}
\end{equation}

where
\begin{equation}
l_k(x) = \prod_{j=0, j\neq k}^{n} \frac{x-x_j}{x_k-x_j}. \tag{2}
\end{equation}

Note that the Lagrange method is more efficient than the matrix method because *we do not need to calculate any inverse matrices*.

1. **The constructor `__init__(self, data_x, data_y)` is written for you.**

     * Here, we check whether the input vectors (numpy arrays) are equal or not.
     * We store `data_x` and `data_y`
     * We calculate and store the degree of the polynomial.
$$\$$

2. **The `_repr__(self)` function has been written for you.**

    * This is similar to the `toString()` method in Java. This returns a formatted string of the object whenever the object is printed.
$$\$$

3. **You have to implement the `l(self, k, x)` function.**
    * This function would take `k` and `x` as inputs and calculate the Lagrange basis using the Equation $(2)$.
$$\$$

4. **You have to implement the `__call__(self, x_arr)` function.**
    * This function makes an object of a class callable.
    * The function calculates the lagrange polynomial from a set of given nodes. `self.data_x` and `self.data_y` contains the coordinates of the given nodes of the original function. Using Equation $(1)$, you have to use `self.data_x`, `self.data_y`, and the `l(k, x_k, x)` function to find the interpolated output of the polynomial for all elements of `x_arr`.
`x_arr` is a numpy array containing points through which we want to plot our polynomial.
"""

class Lagrange_Polynomial:
    def __init__(self, data_x, data_y):
        '''
        First we need to check whether the input vectors (numpy arrays) are equal
        or not.
        assert (condition), "msg"
        this command checks if the condition is true or false. If true, the code
        runs normally. But if false, then the code returns an error message "msg"
        and stops execution
        '''
        assert len(data_x) == len(data_y), "length of data_x and data_y must be equal"

        '''
        Lagrange polynomials do not use coefficeints a_i, rather the nodes
        (x_i, y_i). Hence, we just need to store these inside the object
        '''

        self.data_x = data_x
        self.data_y = data_y

        self.degree = len(data_x) - 1
        # we assume that the inputs are numpy array, so we can perform
        # element wise operations

    def __repr__(self):
        # method for string representation
        # you don't need to worry about the following code if you don't understand
        strL = f"LagrangePolynomial of order {self.degree}\n"
        strL += "p(x) = "
        for i in range(len(self.data_y)):
            if self.data_y[i] == 0:
                continue
            elif self.data_y[i] >= 0:
                strL += f"+ {self.data_y[i]}*l_{i}(x) "
            else:
                strL += f"- {-self.data_y[i]}*l_{i}(x) "

        return strL

    def l(self, k, x):


        l_k = 1.0 # Initialization

        # --------------------------------------------
        # YOUR CODE HERE
        for i in range(len(self.data_x)):
            if i != k:
              l_k*=(x - self.data_x[i]) / (self.data_x[k] - self.data_x[i])

        #raise NotImplementedError()

        return l_k


    def __call__(self, x_arr):

        # initialize with zero
        p_x_arr  = np.zeros(len(x_arr))


        # --------------------------------------------
        # YOUR CODE HERE
        '''for j in range (len(x_arr)):
           for i in range(self.degree + 1):
                p_x_arr[j]+=self.l(i,x_arr[j])*self.data_y[i]'''

        for i in range(self.degree + 1):
            p_x_arr+=self.l(i,x_arr)*self.data_y[i]
        #raise NotImplementedError()

        return p_x_arr

"""### Calling the LagrangePolynomial object and plotting the polynomial.

*Note that in the plot the given nodes will be marked in red.*
"""

import numpy as np

data_x = np.array([-3.5, -2.231, -1.152, -0.5, 0.198, 0.785, 1.6])
data_y = np.array([4.0, 1.193, 6.156, 2.0, 1.803, 2.558, 0.0])

p = Lagrange_Polynomial(data_x, data_y)
print(p)

#generating 40 points from -3.5 to 1.6 in order to create a smooth line
x_arr = np.linspace(-3.5, 1.6, 40)
p_x_arr = p(x_arr)

# plot to see if your implementation is correct
#google the functions to understand what each parameters mean, if not apparent
plt.plot(x_arr, p_x_arr)
plt.plot(data_x, data_y, 'ro')
plt.legend(['interpolated', 'node points'], loc = 'lower right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial')

plt.show()

"""###Problem related Lagrange interpolation

> Suppose, you have a function f(x) = 4x and three nodes (2, 8), (4, 16), (6, 24). Using Lagrange basis, print out the value of the interpolating polynomial at x = -1.5. Also, display the actual interpolation error at x = -1.5.

Hint: Interpolation error = | f(-1.5) - p(-1.5) | where p is the interpolating polynomial.

`You have to solve this problem using Lagrange_Polynomial class`
"""

#your code here

#your code here
data_x = np.array([2,4,6])
data_y = np.array([8,16,24])

pol = Lagrange_Polynomial(data_x, data_y)

print(f'Intrepolation_Error={abs((4*(-1.5))-pol([-1.5])[0])}')
print(pol)

def f(x):
    return 4 * x

data_x = np.array([2, 4, 6])
data_y = np.array([8, 16, 24])
lagrange_poly = Lagrange_Polynomial(data_x, data_y)

x_val = np.array([-1.5])

interpolated_value = lagrange_poly(x_val)
print("Interpolating polynomial value at x = -1.5:", interpolated_value[0])

# The actual interpolation error at x = -1.5
actual_value = f(-1.5)
print ("Actual value at x:",actual_value)
interpolation_error = np.abs(actual_value - interpolated_value[0])
print("Actual interpolation error at x = -1.5:", interpolation_error)