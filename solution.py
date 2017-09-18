import numpy as np


def reader(matrix):
    file = open("sudoku")
    i = 0
    j = 0
    k = 0
    for line in file:
        i = np.mod(k, 9)
        j = int(k/9)
        matrix[i][j] = line
        k += 1
    return matrix


def printer(matrix):
    print("-----------------------------")
    for j in range(3):
        for i in range(9):
            if np.mod(i, 3) == 0:
                print("|", end=" ")
            print(matrix[i][j], end=" ")
            if np.mod(i, 9) == 8:
                print("|")
            elif np.mod(i, 3) == 2:
                print("|", end=" ")
    print("-----------------------------")
    for j in range(3, 6):
        for i in range(9):
            if np.mod(i, 3) == 0:
                print("|", end=" ")
            print(matrix[i][j], end=" ")
            if np.mod(i, 9) == 8:
                print("|")
            elif np.mod(i, 3) == 2:
                print("|", end=" ")
    print("-----------------------------")
    for j in range(6, 9):
        for i in range(9):
            if np.mod(i, 3) == 0:
                print("|", end=" ")
            print(matrix[i][j], end=" ")
            if np.mod(i, 9) == 8:
                print("|")
            elif np.mod(i, 3) == 2:
                print("|", end=" ")
    print("-----------------------------")


def solution(matrix):
    # Initialisation of all possible solutions
    sltspace = np.ones((9, 9, 9), dtype=int)
    slt = np.zeros((9, 9), dtype=int)

    # Removing impossible solutions
    for j in range(9):
        for i in range(9):
            v = matrix[i][j]
            # Update solution space when it finds a nonzero entry
            if v > 0:
                # Update rule 1: No duplicated numbers in one row
                sltspace[:, j, v-1] = 0
                # Update rule 2: No duplicated numbers in one column
                sltspace[i, :, v-1] = 0
                # Update rule 3: No duplicated numbers in one 3*3 cubenj
                p = int(i/3)*3   # Locate the 3*3 cube in 9*9 cube
                q = int(j/3)*3
                for n in range(q, q+3):
                    for m in range(p, p+3):
                        sltspace[m, n, v-1] = 0
                # Re-initialise itself it there is already a number
                sltspace[i, j, :] = 0
                sltspace[i, j, v-1] = 1

    # Confirm solution when there is only one possible solution
    for j in range(9):
        for i in range(9):
            if np.sum(sltspace[i, j, :]) == 1:
                slt[i, j] = int(np.where(sltspace[i, j, :] == 1)[0]) + 1
    return slt


def main():
    problem = np.zeros((9, 9), dtype=int)
    reader(problem)
    print("The original puzzle is :")
    printer(problem)
    counter = 0
    while True:
        temp = solution(problem)
        if np.array_equal(temp, problem):
            break
        else:
            problem = temp
            counter += 1
    print("The solution is :")
    printer(problem)
    print("It took {} loops to solve.".format(counter))

if __name__ == main():
    main()
