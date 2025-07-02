import numpy as np


def find_average(liste: list) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(liste) / len(liste)


def gardners_equation(velocity: float) -> float:
    """Calculate the density
    Args:
        velocity: float number
    Returns:
        The density
    Raise:
        ValueError: In case a negative velocity is provided
    """
    alpha = 0.31
    beta = 0.25
    if velocity < 0:
        raise ValueError
    return alpha * (velocity**beta)


def inverse_gardners_equation(density: float) -> float:
    """Calculate the velocity
    Args:
        density: float number
    Returns:
        The velocity
    Raise:
        ValueError: In case a negative density is provided
    """
    alpha = 0.31
    beta = 0.25
    if density < 0:
        raise ValueError
    return (density / alpha) ** (1 / beta)
