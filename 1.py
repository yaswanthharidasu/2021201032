from tabulate import tabulate
import copy

def readInput():
    n, u, v = map(int, input().split())

    # Cost vector
    tableau = []
    tableau.append(list(map(int, input().split())))

    # <= constraints 
    for i in range(u):
        tableau.append(list(map(int, input().split())))

    # >= constraints 
    for i in range(v):
        tableau.append(list(map(int, input().split())))

    # RHS vector for all constraints
    b = list(map(int, input().split()))

    return n, u, v, tableau, b


def solve(basicVars, tableau):
    # Solve until there is no positive value in the first row .i.e. optimal solution is reached
    while max(tableau[0]) > 0:
        # Find the entering variable
        enteringInd = tableau[0].index(max(tableau[0]))

        # Find the exiting variable
        exitingInd = -1
        exitingVal = float('inf')

        for i in range(1, len(tableau)):
            num = tableau[i][-1]
            den = tableau[i][enteringInd]
            if den <= 0:
                continue
            ratio = round(num/den)
            if ratio < exitingVal:
                exitingInd = i
                exitingVal = ratio

        # Unbounded case
        if exitingInd == -1:
            print("Unbounded")
            return
        
        basicVars[exitingInd] = enteringInd+1
        print(basicVars)

        pivot = tableau[exitingInd][enteringInd]
        pivotRow = copy.deepcopy(tableau[exitingInd])

        # Updating the tableau
        # new value = old value - (corresponding key row val * col val) / pivot ele
        for i in range(len(tableau)):
            pivotColVal = tableau[i][enteringInd]
            # print(pivotColVal)
            for j in range(len(tableau[i])):
                if i == exitingInd:
                    tableau[i][j] = tableau[i][j]/pivot
                else:
                    tableau[i][j] = tableau[i][j] - (pivotColVal * pivotRow[j])/pivot


        print(tabulate(tableau))
        print("==================================================")
        



def simplex(n, u, tableau, b):
    # Adding -1 for the first row
    basicVars = [-1]

    # Add zeroes and b value for each row
    zeroes = [0]*(u+1)
    tableau[0].extend(zeroes)

    for i in range(1, u+1):
        zeroes = [0]*(u+1)
        zeroes[i-1] = 1
        zeroes[-1] = b[i-1]
        tableau[i].extend(zeroes)
        basicVars.append(n+i)

    tableau[0] = list(map(lambda x: -1 * x, tableau[0]))
    
    print("==================================================")
    print(basicVars)
    print(tabulate(tableau))
    print("==================================================")
    solve(basicVars, tableau)


def twoPhaseSimplex():
    # for i in range(v):
    #     col = [0]*(u+v+1)
    #     col[u+i+1] = -1
    pass

if __name__ == "__main__":
    n, u, v, tableau, b = readInput()
    if v == 0:
        simplex(n, u, tableau, b)
    else:
        twoPhaseSimplex()

