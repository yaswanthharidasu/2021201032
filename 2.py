from tabulate import tabulate
from helper import *

if __name__ == "__main__":
    n, u, v, tableau, b = readInput()
    if v == 0:
        simplex(n, u, tableau, b)
    else:
        twoPhaseSimplex(n, u, v, tableau, b)

