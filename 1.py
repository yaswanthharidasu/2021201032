from tabulate import tabulate
from helper import *


if __name__ == "__main__":
    n, u, v, tableau, b = readInput()
    if v == 0:
        val, basicVars, tableau = simplex(n, u, tableau, b)
        if val == -1: 
            print("Infeasible")
        elif val == 1:
            print("Unbounded")
        else:
            if val == 2:
                print("Cycling detected") 
            print(round(tableau[0][-1], 7))
            ans = [0]*n
            for i in range(1, len(tableau)):
                if basicVars[i]-1 < n:
                    ans[basicVars[i]-1] = round(tableau[i][-1], 7)
            print(*ans)
    else:
        val, basicVars, tableau = twoPhaseSimplex(n, u, v, tableau, b)
        if val == -1: 
            print("Infeasible")
        elif val == 1:
            print("Unbounded")
        else :
            if val == 2:
                print("Cycling detected") 
            print(round(tableau[0][-1], 7))
            ans = [0]*n
            for i in range(1, len(tableau)):
                if basicVars[i]-1 < n:
                    ans[basicVars[i]-1] = round(tableau[i][-1], 7)
            print(*ans)
