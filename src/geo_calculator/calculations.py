import numpy as np

def find_average(liste) -> float:
    return sum(liste) / len(liste)

def gardners_equation(velocity) -> float:
    alpha = 0.31
    beta = 0.25
    return alpha*(velocity**beta)

def inverse_gardners_equation(density) -> float:
    alpha = 0.31
    beta = 0.25
    return (density/alpha)**(1/beta)