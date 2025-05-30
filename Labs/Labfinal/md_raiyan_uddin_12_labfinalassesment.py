# -*- coding: utf-8 -*-
"""Md. Raiyan Uddin_12_LabFinalAssesment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EkqMoG2vTUpwj8r32u4QmdEtDNnOimRC
"""

NAME = "Md. Raiyan Uddin"
ID = "21301613"
SECTION = "12"

"""# Instructions:

This is your special assessment for CSE330 Lab. ***Please read the instructions carefully!***

1. You must rename this file as "ID_Name_Section_SA.ipynb". Example: "21212121_Niloy Farhan_01-SA.ipynb".
2. There are 4 tasks and each task have several substasks. This tasks are based on the content of lab 5 and lab 6.
3. You must use designated cells for each task. You should not use additional cells for codes of a task.
4. Some task may have no output. It will be mentioned in the designated cells.
5. Not a single line of code of this assessment should be written by AI. If you do, karma will hit you back. ;)
6. **Plagarism can lead to a zero mark in Final Assessment.**
7. If you have any queries, reach out to your lab faculties.


**Best of luck!**

# Task1.


Let $f(x)$ be a function of $x$.

$$f(x) = x^5 + 2.5x^4 - 2x^3 -6x^2 + x + 2\tag{1.1}$$

a. Plot the function for $$-2.5 \le x \le 1.5$$

b. What is the actual slope of $f(x)$ at $x = 0 , -1.18625$ ?  Print $f'(x)$ and plot $f'(x)$ at $ -2 \le x \le 1.2$.

For c to e, assume step size is $0.1$.

c. Use forward differntiation to figure out the slope at $x = 0 , -1.18625$.

d. Use backward differntiation to figure out the slope at $x = 0 , -1.18625$.

e. Use central differntiation to figure out the slope at $x = 0 , -1.18625$.

f. Compare the error of each method with actual differentiation at $x = 0 , -1.18625$ by showing in a Pandas Dataframe.

g. plot error vs h curves with proper label and color for each method at $x = 0$ and $h = [0.55, 0.3, .17, 0.1, 0.055, 0.03, 0.017, 0.01]$.
"""

# Import cells. This is done for you!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

#1.a This cell should plot a graph. You must use polynomial class.
coefficients = [2, 1, -6, -2, 2.5, 1]
f = Polynomial(coefficients)
x = np.linspace(-2.5, 1.5, 400)
y = f(x)
plt.plot(x, y, label="f(x) = x^5 + 2.5x^4 - 2x^3 - 6x^2 + x + 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of f(x) = x^5 + 2.5x^4 - 2x^3 - 6x^2 + x + 2")
plt.legend()
plt.grid(True)
plt.show()

#1.b This cell should print and plot a graph.
f_prime = f.deriv()
print("Derivative f'(x):", f_prime)
x_vals = [0, -1.18625]
for x in x_vals:
  print(f"f'({x}) = {f_prime(x)}")
x = np.linspace(-2, 1.2, 400)
y_prime = f_prime(x)
plt.plot(x, y_prime, label="f'(x)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Graph of f'(x) = derivative of f(x)")
plt.legend()
plt.grid(True)
plt.show()

#1.c This cell should print
def forward_differentiation(f, x, h):
  return (f(x + h) - f(x)) / h
h = 0.1
slope1 = forward_differentiation(f, 0, h)
print(f"Approximate slope at x = 0 is : {slope1}")
slope2 = forward_differentiation(f, -1.18625, h)
print(f"Approximate slope at x = -1.18625 is: {slope2}")

#1.d This cell should print
def backward_differentiation(f, x, h):
  return (f(x) - f(x - h)) / h
h = 0.1
x_vals = [0, -1.18625]

for x in x_vals:
  slope_backward = backward_differentiation(f, x, h)
  print(f"Backward slope at x = {x}: {slope_backward}")

#1.e This cell should print
def central_differentiation(f, x, h):
  return (f(x + h) - f(x - h)) / (2 * h)
h = 0.1
x_vals = [0, -1.18625]
for x in x_vals:
  slope_central = central_differentiation(f, x, h)
  print(f"Central slope at x = {x}: {slope_central}")

#1.f This cell should show a table
from tabulate import tabulate

def compare(f, f_prime, h, x):
    Result = {'x' : [], "Actual" : [],"FD": [], "BD" : [], "CD": [], "FD Error" : [], "BD Error": [], "CD Error" : []}     #
    #Write code here

    for x in x_vals:
      actual_slope = f_prime(x)
      forward_slope = (f(x + h) - f(x)) / h
      forward_error = abs(forward_slope - actual_slope)


      backward_slope = (f(x) - f(x - h)) / h
      backward_error = abs(backward_slope - actual_slope)


      central_slope = (f(x + h) - f(x - h)) / (2 * h)
      central_error = abs(central_slope - actual_slope)


      Result['x'].append(x)
      Result['Actual'].append(actual_slope)
      Result['FD'].append(forward_slope)
      Result['BD'].append(backward_slope)
      Result['CD'].append(central_slope)
      Result['FD Error'].append(forward_error)
      Result['BD Error'].append(backward_error)
      Result['CD Error'].append(central_error)

    return pd.DataFrame(Result)

coefficients = [2, 1, -6, -2, 2.5, 1]
f = Polynomial(coefficients)
f_prime = f.deriv()


h = 0.1
x_vals = [0, -1.18625]
compare(f, f_prime, h, x_vals)

#1g This cell should plot a graph.
h_values = [0.55, 0.3, 0.17, 0.1, 0.055, 0.03, 0.017, 0.01]
x = 0
actual_slope = f_prime(x)
fd_errors = []
bd_errors = []
cd_errors = []


for h in h_values:

  forward_slope = forward_differentiation(f, x, h)
  forward_error = abs(forward_slope - actual_slope)
  fd_errors.append(forward_error)


  backward_slope = backward_differentiation(f, x, h)
  backward_error = abs(backward_slope - actual_slope)
  bd_errors.append(backward_error)


  central_slope = central_differentiation(f, x, h)
  central_error = abs(central_slope - actual_slope)
  cd_errors.append(central_error)

plt.plot(h_values, fd_errors, label='Forward Differentiation Error', marker='o', color='red')
plt.plot(h_values, bd_errors, label='Backward Differentiation Error', marker='o', color='green')
plt.plot(h_values, cd_errors, label='Central Differentiation Error', marker='o', color='black')

plt.xscale('log')
plt.yscale('log')
plt.title('Error vs Step Size (h) for Forward, Backward, and Central Differentiation at x=0')
plt.xlabel('Step Size (h)')
plt.ylabel('Error')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()

"""# Task 2.

a. Propose a better technique for numerical differentiation that provides higher accuracy than the methods you have worked so far. You need to write a function for your proposed technique.

Let, $$f(x) = x^5 + 2.5x^4 - 2x^3 -6x^2 + x + 2\tag{2.1}$$

b. Using your proposed method, what is the slope of $f(x)$  at $x=0,−1.18625$ and step size = 0.1?

c. Compare the error of your method with  actual, forward, backward and central differentiation at  $x=0,−1.18625$  by showing in Pandas Dataframe.

d. Plot actual derivative, Forward derivative, Backward derivative, Central derivative and the derivative from your proposed method in a graph. Here, $$h = 0.1, -2 \le x \le 1.2$$
"""

#2a. This cell should not have any output.
Proposed_Method_Name = "Richardson Extrapolation"

#Write Code here
def richardson_extrapolation(f, x, h):
  d1 = central_differentiation(f, x, h)
  d2 = central_differentiation(f, x, h/2)
  return (4*d2 - d1) / 3

#2b. This cell should print
h = 0.1
x1 = 0
x2 = -1.18625
slope1 = richardson_extrapolation(f, x1, h)
slope2 = richardson_extrapolation(f, x2, h)

print(f"The slope at x = 0 is {slope1}")
print(f"The slope at x = -1.18625 is {slope2}")

#2c.This cell should print

def compare1(f1, f_prime, h, x):
    Result = {'x' : [], "Actual" : [],"FD": [], "BD" : [], "CD": [],"RE": [], "FD Error" : [], "BD Error": [], "CD Error" : [], "RE Error" : []}
    #Write code here
    for i in range(len(x)):
      Result['x'].append(x[i])
      Result['Actual'].append(f_prime(x[i]))
      Result['FD'].append(forward_differentiation(f, x[i], h))
      Result['BD'].append(backward_differentiation(f, x[i], h))
      Result['CD'].append(central_differentiation(f, x[i], h))
      Result['RE'].append(richardson_extrapolation(f, x[i], h))
      Result['FD Error'].append(abs(f_prime(x[i]) - forward_differentiation(f, x[i], h)))
      Result['BD Error'].append(abs(f_prime(x[i]) - backward_differentiation(f, x[i], h)))
      Result['CD Error'].append(abs(f_prime(x[i]) - central_differentiation(f, x[i], h)))
      Result['RE Error'].append(abs(f_prime(x[i]) - richardson_extrapolation(f, x[i], h)))
    return pd.DataFrame(Result)

x_val = [0, -1.18625]
h = 0.1
f1 = Polynomial(coefficients)
f_prime = f1.deriv()

compare1(f1, f_prime, h, x_val)

#2.d This cell should plot a graph.
h = 0.1
x = np.linspace(-2, 1.2, 100)
f_prime = f.deriv()

actual_derivative = f_prime(x)
forward_derivative = [forward_differentiation(f, i, h) for i in x]
backward_derivative = [backward_differentiation(f, i, h) for i in x]
central_derivative = [central_differentiation(f, i, h) for i in x]
richardson_derivative = [richardson_extrapolation(f, i, h) for i in x]

plt.plot(x, actual_derivative, label='Actual Derivative')
plt.plot(x, forward_derivative, label='Forward Derivative')
plt.plot(x, backward_derivative, label='Backward Derivative')
plt.plot(x, central_derivative, label='Central Derivative')
plt.plot(x, richardson_derivative,label="Richardson")

plt.xlabel("x")
plt.ylabel("Derivative")
plt.title("Comparison of Numerical Differentiation Methods")
plt.legend()
plt.show()

"""# Task 3.

Given,
$f(x) = \frac{-1}{13}x^3 + 2x^2 - 9.5x - 10\tag{3.1}$

a. (i) Write a python function that takes an input function and a list of intervals as a list and returns a dictionary that contains either root exists or not in each intervals.
Determine if root exists in $[(-20,-10),(-10,0), (0,10), (10,20), (20,30)]$.

(ii) Verify your method by ploting the function and the intervals.
"""

#3a_i This cell should print
intervals = [(-20,-10),(-10,0), (0,10), (10,20), (20,30)]  #  This snippet will be given in the question

def f(x):
    return (-1/13)*(x**3) + 2*x**2 - 9.5*x - 10

def check_root(f, intervals):
    result = {}
    for interval in intervals:
        a, b = interval
        if f(a) * f(b) < 0:
            result[interval] = "Root Exists"
        else:
            result[interval] = "No Root"
    return result

intervals = [(-20, -10), (-10, 0), (0, 10), (10, 20), (20, 30)]

find_roots= check_root(f, intervals)
print(find_roots)

#3a_ii This cell should plot a graph.
# Plot the function
x_vals = np.linspace(-25, 35, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')

# Mark the intervals
for interval in intervals:
    a, b = interval
    plt.axvline(a, color='red', linestyle='--', alpha=0.6)
    plt.axvline(b, color='red', linestyle='--', alpha=0.6)

plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.title('Function Plot with Intervals')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

"""b. Using Bisection method, find roots of the function $3.1$ in these intervals $[(−20,−10),(−10,0),(0,10),(10,20),(20,30)]$ where root exists. The value of machine epsilon is, $\epsilon < 10^{-6}$


You can reuse the function of Task 3.a to find out the intervals that contains root.
Note: You should return 3 different roots for the function (3.1).
"""

#3b This cell should print
def bisection_method(f, a, b, epsilon=1e-6):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    while (b - a) / 2 > epsilon:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2
for interval in intervals:
    a, b = interval
    if find_roots[interval] == "Root Exists":
        root = bisection_method(f, a, b)
        print(f"Root found in interval {interval}: {root}")

"""c. Plot the f(x) along with the roots to check if your method is working correctly."""

#3c This cell plot a graph.
roots = []

for interval in intervals:
    a, b = interval
    if find_roots[interval] == "Root Exists":
        root = bisection_method(f, a, b)
        roots.append(root)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')

for root in roots:
    plt.plot(root, f(root), 'ro', label=f'Root at x = {root:.6f}')

plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.title('Function Plot with Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

"""Task4.


Let $f(x)$ be a function of $x$.

$$f(x) = x^5 + 2.5x^4 - 2x^3 -6x^2 + \frac{x}{2} + 2\tag{4.1}$$

a. Find the actual roots of $f(x)$ and print them.

b. Plot the function for $-2.5 \le x \le 1.5$, also point out the the found roots in the plot

c. The following $g_{1}(x)$ is given which is derived from Eq$(4.1)$, \\
   Use Contraction Mapping Theorem and calculate the value of λ for the given $g(x)$ $$g_{1}(x)= \frac{1}{2}(-x^5 - 2.5x^4 + 2x^3 + 6x^2 - 2)\tag{4.2}$$

d. Compute the convergence/divergence table using all the calculated roots for the given $g_{1}(x)$ and prove the whole $g_{1}(x)$ is divergent

Given,

$$g_{2}(x)= \sqrt{\frac{1}{6}(x^5 + 2.5x^4 -2x^3 + \frac{1}{2}x + 2)}\tag{4.3}$$
$$g_{3}(x) = \sqrt[\leftroot{-1}\uproot{2}\scriptstyle 4]{\frac{1}{2.5}(-x^5 + 2x^3 + 6x^2 - \frac{1}{2}x - 2)}\tag{4.4}$$
e. Derive 2 more separate $g_{4}(x)$ and $g_{5}(x)$ from the given $f(x)$. Implement $g_{2}(x)$, $g_{3}(x)$, $g_{4}(x)$ and $g_{5}(x)$.

f. Apply Fixed Point Method on the $g_{2}(x)$, $g_{3}(x)$, $g_{4}(x)$ and $g_{5}(x)$. and find the approprate roots, show 20 iterations for each $g(x)$ for $x_{0}$ = 0.8 and show the convergence table using data from each iteration

g. Plot the $g(x)$s where actual roots were found along with $f(x)$.
"""

#4a This cell should print
from scipy.optimize import fsolve
coeff= [1, 2.5, -2, -6, 0.5, 2]
roots = np.roots(coeff)
print("Roots of f(x) are:")
for root in roots:
    print(root)

#4b This cell should print plot a graph
coeff = [1, 2.5, -2, -6, 0.5, 2]
polynomial = np.poly1d(coeff)
x = np.linspace(-2.5, 1.5, 400)
y = polynomial(x)

roots = np.roots(coeff)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label='f(x)', color='blue')

for root in roots:
    plt.plot(root, polynomial(root), 'ro')
    plt.text(root, polynomial(root), f'{root:.2f}', fontsize=10, ha='left')

plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
plt.axvline(0, color='black', linestyle='--', linewidth=0.7)
plt.title('Plot of f(x) and Its Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.xlim(-2.5, 1.5)
plt.ylim(min(y), max(y))
plt.legend()
plt.show()

#4c This cell should print
g1_x=Polynomial([-1,0,3,1,-1.25,-.5])
print(g1_x)
prime_g1_x=g1_x.deriv(1)
print(prime_g1_x)
lemda=abs(prime_g1_x(roots))
print(f'Lemda is {lemda}')

#4d This cell should print
def f(x):
    return x**5 + 2.5*x**4 - 2*x**3 - 6*x**2 + 0.5*x + 2

def g1(x):
    return 0.5 * (-x**5 - 2.5*x**4 + 2*x**3 + 6*x**2 - 2)

def g2(x):
    return np.sqrt(1/6) * (x**5 + 2.5*x**4 - 2*x**3 + 0.5*x + 2)

def g3(x):
    return 4 * np.sqrt(1/2.5) * (-x**5 + 2*x**3 + 6*x**2 - 0.5*x - 2)

coeffs_g1 = [1, 2.5, -2, -6, 0.5, 2]
roots_g1 = np.roots(coeffs_g1)

print(f"{'Root':<20} {'g2(root)':<20} {'g2 Convergence':<15} {'g3(root)':<20} {'g3 Convergence':<15}")
print("-" * 100)

for root in roots:
    g2_value = g2(root)
    g3_value = g3(root)

    g2_convergence = 'Convergent' if abs(g2_value) < 1e-5 else 'Divergent'
    g3_convergence = 'Convergent' if abs(g3_value) < 1e-5 else 'Divergent'

    print(f"{root:<20} {g2_value:<20} {g2_convergence:<15} {g3_value:<20} {g3_convergence:<15}")

#4e This cell have no outputs
np.cbrt((x**5 + 2.5*x**4 - 6*x**2 + x/2 + 2) / 2)
def g4(x):
    p=Polynomial([-2,-0.5,6,2,-2.5])
    return np.power(p(x),1.0/5.0)
def g5(x):
    return ((x**5 + 2.5*x**4 - 6*x**2 + x/2 + 2) / 2)**(1/3)
def g2(x):
    p = Polynomial([2.0, .5, 0.0, -2.0, 2.5, 1.0])
    return np.sqrt(p(x)/6)
def g3(x):
    p = Polynomial([-2.0, -.5, 6.0, 2.0, 0.0, -1.0])
    return np.power(p(x)/2.5, 1.0/4.0)

#4f This cell should print
a2 = 0.80
g2_a = []
a3 = 0.80
g3_a = []
a4 = 0.80
g4_a = []
a5 = 0.80
g5_a = []
for i in range(21):
  p = g2(a2)
  g2_a.append(p)
  a2= p
  q = g3(a3)
  g3_a.append(q)
  a3= q
  r = g4(a3)
  g4_a.append(r)
  a4= r
  s = g5(a5)
  g5_a.append(s)
  a5= s
print(pd.DataFrame({'g2(x)':g2_a, 'g3(x)':g3_a, 'g4(x))': g4_a,'g5(x)':g5_a}))
g2_root = g2_a[-1]
g3_root = g3_a[-1]
g4_root = g4_a[-1]
g5_root = g5_a[-1]
print(f'Roots are {g2_root}, {g3_root}, {g4_root}, {g5_root}')

#4g This cell should plot a graph. Do not plot those g(x) which will not converge.
x= np.linspace(-2.3, 1.5, 100)
y = f(x)
dic = { 'x': x,  'y': y}
plt.axhline(y=0, color='r')
plt.plot(x, f(x), label='f(x)', color='y')
plt.plot(x, g2(x), label='g2(x)', color='g')
plt.plot(x, g3(x), label='g3(x)', color ='b')
plt.plot(x, g4(x), label='g4(x)', color = 'm' )
plt.plot(x, g5(x), label='g5(x)', color = 'c')
plt.legend()
if len(g2_a) > 0:
    root = np.array([g2_a[len(g2_a)-1], g3_a[len(g3_a)-1], g4_a[len(g4_a)-1],g5_a[len(g5_a)-1]])
    plt.plot(root, f(root), 'ko')