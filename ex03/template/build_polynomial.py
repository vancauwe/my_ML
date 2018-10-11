# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: 
    theta=np.zeros((x.shape[0],degree))     
    
    for j in range(degree):
        theta[:,j]=x**(j+1)
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    return theta
