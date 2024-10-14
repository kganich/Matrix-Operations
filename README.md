### Overview
This program performs various matrix operations. It can:
- Add two matrices.
- Multiply a matrix by a vector.
- Multiply two matrices.
- Calculate the inverse of a matrix.
- Transpose a matrix.
- Solve a matrix using Gaussian elimination.

### User Instructions
1. Run the program by executing `matrix.py`.
2. A menu will appear with a list of available operations. The user needs to input a number (1-6) corresponding to the desired operation.
3. The program will prompt for the number of rows in the matrix. If two matrices are required, the user will enter the number of rows for both matrices in one line, separated by a space.
4. The program will then ask for the matrix input, row by row. If a vector is required, the user should input it in one line.
5. After the calculations, the program will display the result.
6. The program will terminate.

### Example Operations
1. Add two matrices.
2. Multiply a matrix by a vector.
3. Multiply two matrices.
4. Find the inverse of a matrix.
5. Transpose a matrix.
6. Solve a matrix using Gaussian elimination.

### Developer Section
Upon running `matrix.py`, the program displays a menu of available operations. Once the user inputs the number corresponding to their desired function, it is stored in the variable `command`.

1. **Addition of Two Matrices (`command = 1`)**  
   The program prompts the user to input two matrices, which are stored using the function `readTwoMatrices(rows)`. The function `sum(matrix1, matrix2)` is then called to check if the matrices have the correct dimensions and, if valid, calculates their sum. If the dimensions are incorrect, an error is displayed.

2. **Matrix-Vector Multiplication (`command = 2`)**  
   The user inputs a matrix and a vector, which are stored using `readMatrix(rows)` for the matrix. The function `vectorMultiplication(matrix, vector)` verifies the dimensions and performs the multiplication. If dimensions are invalid, an error is shown.

3. **Matrix-Matrix Multiplication (`command = 3`)**  
   After inputting two matrices, the program stores them using `readTwoMatrices(rows)` and calls the function `multiplication(matrix1, matrix2)`. This function checks the dimensions and performs the multiplication similar to `vectorMultiplication`.

4. **Inverse of a Matrix (`command = 4`)**  
   The user inputs a matrix, and the program calls `inverse(matrix)`. The function checks if the matrix is square and, if valid, computes the inverse. If the matrix is not square, an error is displayed.

5. **Transpose of a Matrix (`command = 5`)**  
   The function `transpose(matrix)` is called with the input matrix, transposing it row by row, and returns the transposed matrix.

6. **Gaussian Elimination (`command = 6`)**  
   The program calls `solveGaussElimination(matrix)`, which solves the matrix by transforming it into an upper triangular form followed by back substitution. The result is then displayed.

### Conclusion
This program provides various matrix operations with error handling for invalid inputs such as incorrect matrix dimensions or non-square matrices for operations that require them. It uses basic matrix manipulation techniques implemented in Python.
