from tabulate import tabulate
from helper import *
import math


def dualSimplex(row, basicVars, tableau):
    # Adding the new row
    # gomoryRow = [0]*len(tableau[row])

    gomoryRow = []
    for col in range(len(tableau[row])):
        gomoryRow.append(tableau[row][col] - math.floor(tableau[row][col]))
    gomoryRow = list(map(lambda x: -1 * x, gomoryRow))
    
    # Adding slack variable
    for i in range(len(tableau)):
        last = tableau[i][-1]
        tableau[i][-1] = 0
        tableau[i].append(last)

    last = gomoryRow[-1]
    gomoryRow[-1] = 1
    gomoryRow.append(last)
    tableau.append(gomoryRow)

    basicVars.append(len(tableau[0]))
    exitingInd = len(tableau)-1
    enteringInd = -1
    enteringVal = float("inf")

    for col in range(0, len(tableau[0])-1):
        if tableau[exitingInd][col] < 0:
            ratio = tableau[0][col]/tableau[exitingInd][col]
            if tableau[0][col] < 0 and ratio < enteringVal:
                enteringVal = ratio
                enteringInd = col

    basicVars[exitingInd] = enteringInd+1
    pivot = tableau[exitingInd][enteringInd]
    pivotRow = copy.deepcopy(tableau[exitingInd])

    for j in range(0, len(tableau[exitingInd])):
        tableau[exitingInd][j] /= pivot


    for i in range(0, len(tableau)):
        pivotColVal = tableau[i][enteringInd]
        for j in range(0, len(tableau[0])):
            if i == exitingInd:
                continue
            else:
                tableau[i][j] -= pivotColVal * tableau[exitingInd][j]

    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # print("Selcted row: ", row)
    # for i in range(len(tableau)):
    #     print(*tableau[i], sep='\t')
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    return basicVars, tableau

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
    else:
        while True:
            # Check for fractional values 
            fraction = float('-inf')
            row = -1
            for i in range(1, len(tableau)):
                temp = tableau[i][-1]
                temp = round(temp, 7)
                if math.ceil(temp) != math.floor(temp):
                    temp = tableau[i][-1] - math.floor(tableau[i][-1])
                    if temp > fraction:
                        fraction = temp
                        row = i

            # Integer solutions
            if row == -1:
                printAns(n, val, basicVars, tableau)
                break
            else:
                basicVars, tableau = dualSimplex(row, basicVars, tableau)
                # print("================================================================")
                # for i in range(len(tableau)):
                #     print(*tableau[i], sep='\t')
                # print("================================================================")
                


