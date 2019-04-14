"""A module to calculate the Fibonacci numbers
"""

def fib(number: int) -> int:
    """Calculates the nth Fibonacci number

    Parameters
    ----------
    n : int
        Which Fibonacci number to calculate


    Returns
    -------
    int
        The nth Fibonacci number
    """
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fib(number - 1) + fib(number - 2)
