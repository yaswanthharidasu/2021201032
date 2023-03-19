from tabulate import tabulate
from helper import *


if __name__ == "__main__":
    n, u, v, tableau, b = readInput()
    if v == 0:
        val, basicVars, tableau = simplex(n, u, tableau, b)
    else:
        val, basicVars, tableau = twoPhaseSimplex(n, u, v, tableau, b)
        
    if val == -1: 
        print("Infeasible")
    elif val == 1:
        print("Unbounded")
    else :
        printAns(n, val, basicVars, tableau)
