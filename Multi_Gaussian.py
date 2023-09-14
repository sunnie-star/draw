import numpy as np
import math


def multivariate_gaussian_pdf(X, MU, SIGMA):
    '''Returns the pdf of a nultivariate gaussian distribution
     - X, MU are p x 1 vectors
     - SIGMA is a p x p matrix'''
    # Initialize and reshape
    X = X.reshape(-1, 1)
    MU = MU.reshape(-1, 1)
    p, _ = SIGMA.shape
    # Compute values
    SIGMA_inv = np.linalg.inv(SIGMA)
    denominator = np.sqrt((2 * np.pi) ** p * np.linalg.det(SIGMA))
    exponent = -(1 / 2) * ((X - MU).T @ SIGMA_inv @ (X - MU))
    # Return result
    return float((1. / denominator) * np.exp(exponent))


def multivariate_gaussian_fit(Xs):
    m, p = Xs.shape
    MU = Xs.sum(axis=0)/m
    MU = MU.reshape(-1, 1)
    SIGMA = np.zeros((p,p))
    for X in Xs:
        X = X.reshape(-1, 1)
        SIGMA = SIGMA + (X - MU) @ (X - MU).T
    SIGMA = SIGMA / m
    return MU, SIGMA


def get_Ellipse(SIGMA):
    eig, fea = np.linalg.eig(SIGMA)
    a = math.sqrt(eig[0])*2
    b = math.sqrt(eig[1])*2
    ang = math.atan(-fea[0][1]/fea[0][0])
    a = a
    b = b
    return a, b, ang/math.pi*180


if __name__ == "__main__":
    print('hello')
