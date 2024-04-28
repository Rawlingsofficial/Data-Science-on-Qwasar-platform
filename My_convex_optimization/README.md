# Optimization Techniques Project

This project explores various optimization techniques implemented in Python for finding roots, minimizing functions, and solving linear programming problems.

## Prerequisites

Ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [NumPy](https://numpy.org/)
- [SciPy](https://www.scipy.org/)

## Introduction

The project covers the following optimization techniques:

1. **Brent's Method for Root Finding**: Utilizes Brent's method to find the root of a function.
2. **Bisection Method**: Implements the bisection method to find the root of a given function.
3. **Newton-Raphson Method**: Implements the Newton-Raphson method to find the root of a function.
4. **Gradient Descent**: Implements gradient descent for minimizing a function.
5. **Linear Programming Solver**: Uses linear programming techniques to solve optimization problems.

## Usage

1. Clone the repository to your local machine.
2. Install the required libraries using pip:
3. Run the `optimization_techniques.py` script using Python.
4. Follow the prompts to interact with each optimization technique.

## Functions Implemented

- `custom_function`: Defines a custom function to be optimized.
- `plot_function`: Plots a given function over a specified range.
- `find_root_bisection`: Implements the bisection method to find the root of a function.
- `find_root_newton_raphson`: Implements the Newton-Raphson method to find the root of a function.
- `gradient_descent`: Implements gradient descent for function minimization.
- `solve_linear_problem`: Solves linear programming problems using the simplex method.
- `find_minimum_gradient_descent`: Finds the minimum of a function using gradient descent.

## Sample Usage

Here's how you can use the provided functions:

```python
# Example usage of the functions
optimization_result = minimize_scalar(custom_function, method='brent')
root_bisection = find_root_bisection(custom_function, -2, 3)
root_newton_raphson = find_root_newton_raphson(custom_function, custom_function_derivative, -1)
minimum_x, minimum_f = find_minimum_gradient_descent(custom_function, custom_function_derivative, -1)
optimal_value, optimal_arg = solve_linear_problem(custom_A_matrix, custom_b_vector, custom_c_vector)
```
# Contributor
[Mbah Rawling Mukhen](https://github.com/Rawlingsofficial)
