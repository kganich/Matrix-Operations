# Vypocet matic
# Karina Ganich, 1. rocnik, 34 st. skupina
# zimni semestr 2022/23
# Programovani 1 NPRG030

import sys
import numpy as np

# Funkce sklada dve matice
def sum(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]): 
        return (np.asmatrix(matrix1) + np.asmatrix(matrix2)) 
    else:
        return "exception - incorrect matrix sizes"

# Funkce pro nasobeni matice vektorem
def vectorMultiplication(matrix, vector):
    answer = []
    if len(matrix[0]) == len(vector):
        for row in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[row])):
                sum += (matrix[row][j])*vector[j]
            answer.append(sum)
        return answer
    else:
        return "exception - incorrect vector size"

# Funkce pro nasobeni dvou matic
def multiplication(matrix1, matrix2):
    answer = []
    if len(matrix1[0]) == len(matrix2):
        for row in range(len(matrix1)):
            nrow = []
            for column in range(len(matrix2[0])):
                sum = 0
                for j in range(len(matrix1[row])):
                    sum += matrix1[row][j]*matrix2[j][column]
                nrow.append(sum)
            answer.append(nrow)
        return answer
    else:
        return "exception - incorrect matrix sizes"

# Funkce pro vypocet inverzni matice
def inverse(matrix):
    if len(matrix) == len(matrix[0]):
        #inicializujeme jednotkovou matici
        answer = [[0] * len(matrix) for n in range(len(matrix))]

        for n in range(len(matrix)):
            answer[n][n] = 1.0
        
        #udelame horni trojuhelnokovou matici
        for i in range(len(matrix)):
            coeff = matrix[i][i] + 0.0
            if coeff == 0.0:
                return "Matrix is singular"

            for j in range(i+1, len(matrix)):
                mult = -matrix[j][i] / coeff

                for n in range(len(matrix)):
                    matrix[j][n] += mult * matrix[i][n]
                    answer[j][n] += mult * answer[i][n]

        #diagonalizujeme
        for i in range(len(matrix)-1, -1, -1):
            coeff = matrix[i][i] + 0.0

            for j in range(i-1, -1, -1):
                mult = -matrix[j][i] / coeff

                for n in range(len(matrix)):
                    matrix[j][n] += mult * matrix[i][n]
                    answer[j][n] += mult * answer[i][n]

        #prevedeme na jednotkovou matici
        for i in range(len(matrix)):
            scaler = matrix[i][i]
            matrix[i][i] /= scaler
            for n in range(len(matrix)):
                answer[i][n] /= scaler
        
        return answer
    else:
        return "exception - incorrect matrix size"

# Funkce pro vypocet transponovane matice
def transpose(matrix):
    answer = []
    for i in range(len(matrix[0])):
        nrow = []
        for j in range(len(matrix)):
            nrow.append(matrix[j][i])
        answer.append(nrow)
    return answer

# Funkce na vypocet reseni matice
def solveGaussElimination(matrix):
    n = len(matrix[0])-1
    answer = [0 for i in range(n)]

    #udelame horni trojuhelnokovou matici
    for i in range (n):
        if len(matrix) > 1:
            if matrix[i][i] == 0: 
                if matrix[i][n] != 0:
                    return "No solution"
                else:
                    return "Infinitely many solutions"
        else:
            if n > 1:
                return "Infinitely many solutions"
        for j in range(i+1, len(matrix)):
            ratio = matrix[j][i]/matrix[i][i]
            for k in range(n+1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    
    answer[n-1] = matrix[n-1][n] / matrix[n-1][n-1]
   

    #udelame zpetnou substituci
    for i in range(n-2, -1,-1):
        answer[i] = matrix[i][n]
        for j in range(i+1, n):
            answer[i] = answer[i] - matrix[i][j]*answer[j]
        answer[i] = answer[i] / matrix[i][i]

    return answer


def readTwoMatrices():
    matrix1, matrix2 = [], []
    rows = []
    try:
        rows = [int(x) for x in input().split()]

        while rows[0]:
            matrix1.append([float(x) for x in input().split()])
            rows[0] -= 1
        while rows[1]:
            matrix2.append([float(x) for x in input().split()])
            rows[1] -= 1
    except:
        sys.exit()

    return matrix1, matrix2

def readMatrix():
    matrix = []
    try:
        rows = int(input())
    
        while rows:
            matrix.append([float(x) for x in input().split()])
            rows -= 1
    except:
        sys.exit()
    return matrix


if __name__=="__main__":
    print("1 - count the sum of two matrices\n"
        "2 - multiply matrix by vector\n"
        "3 - multiply two matrices\n"
        "4 - count the inverse matrix\n"
        "5 - count the transpose matrix\n"
        "6 - find the matrix solution using Gauss elimination method")
    try:
        command = int(input())
    
        match command:
            case 1:
                print("Write count of rows of the first and the second matrix")
                m1, m2 = readTwoMatrices()
                print(sum(m1, m2))
            case 2:
                print("Write count of rows")
                print(vectorMultiplication(readMatrix(), [int(x) for x in input().split()]))
            case 3:
                print("Write count of rows of the first and the second matrix")
                m1, m2 = readTwoMatrices()
                print(multiplication(m1, m2))
            case 4:
                print("Write count of rows")
                print(inverse(readMatrix()))
            case 5:
                print("Write count of rows")
                print(transpose(readMatrix()))
            case 6:
                print("Write count of rows")
                print(solveGaussElimination(readMatrix()))
            case _:
                print("Incorrect number")

    except:
        print("Incorrect number")

