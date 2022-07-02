import numpy as np
import matplotlib.pyplot as plt

N = 8
matrix = np.zeros((N, N), dtype=int)
print(matrix)

usedRow = np.zeros(N)
usedCol = np.zeros(N)
usedFirstDiagonal = np.zeros(2*N)
usedSecondDiagonal = np.zeros(2*N)

def choose(row, col):
    matrix[row, col] = 1
    usedRow[row] = usedCol[col] = True
    usedFirstDiagonal[row-col+N] = True
    usedSecondDiagonal[row+col] = True


def unchoose(row, col):
    matrix[row, col] = 0
    usedRow[row] = usedCol[col] = False
    usedFirstDiagonal[row - col + N] = False
    usedSecondDiagonal[row + col] = False


def conflict(row, col):
    return usedRow[row] or usedCol[col] or usedFirstDiagonal[row - col + N] or usedSecondDiagonal[row + col]


def draw():
    x = []
    y = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                x.append(i+0.5)
                y.append(j+0.5)

    area = (30 * 1) ** 2
    colors = np.random.rand(N)
    plt.scatter(x, y, s=area, c=colors, alpha=0.7)

    plt.xticks(range(N+1))
    plt.yticks(range(N+1))

    plt.grid(True)
    plt.show()


found = 0

def backtrack(col):
    global found

    if col == N:
        found = 1
        print('found')
        print(matrix)
        draw()
        return

    for row in range(N):
        if found:
            return

        if conflict(row, col):
            continue

        choose(row, col)
        backtrack(col+1)
        unchoose(row, col)


backtrack(0)
