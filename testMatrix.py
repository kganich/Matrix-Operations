import unittest
from matrix import sum, vectorMultiplication, multiplication, inverse, transpose, solveGaussElimination
import numpy as np

class MatrixTest(unittest.TestCase):
    def test_sum_square_matrices(self):
        matrix = sum([[1,2],[2,3]], [[1,1],[1,1]])
        np.testing.assert_allclose(matrix, np.asmatrix([[2,3], [3,4]]))

    def test_sum_nm_matrices(self):
        matrix = sum([[1,2],[2,3],[1,1]], [[1,1],[1,1],[1,1]])
        np.testing.assert_allclose(matrix, np.asmatrix([[2,3], [3,4], [2,2]]))

    def test_vectorMultiplication_simple(self):
        matrix = vectorMultiplication([[1,2,3],[2,3,-1],[1,1,6]], [1,1,1])
        np.testing.assert_allclose(matrix, [6,4,8])

    def test_vectorMultiplication(self):
        matrix = vectorMultiplication([[1,2],[2,3],[1,1]], [2,-1])
        np.testing.assert_allclose(matrix, [0,1,1])

    def test_multiplication_square_matrices(self):
        matrix = multiplication([[1,2],[2,3]], [[1,1],[1,1]])
        np.testing.assert_allclose(matrix, [[3,3], [5,5]])

    def test_multiplicaton(self):
        matrix = multiplication([[1,2],[2,3],[1,1]], [[1,1,1,1],[1,1,1,1]])
        np.testing.assert_allclose(matrix, [[3,3,3,3], [5,5,5,5],[2,2,2,2] ])

    def test_inverse_2(self):
        matrix = inverse([[1,2],[2,3]])
        np.testing.assert_allclose(matrix, np.asmatrix([[-3,2],[2,-1]]))

    def test_inverse_3(self):
        matrix = inverse([[1,2,3],[2,3,4],[-2,4,3]])
        np.testing.assert_allclose(matrix, np.asmatrix([[-1,6/7,-1/7],[-2,9/7,2/7],[2,-8/7,-1/7]]))

    def test_inverse_f(self):
        matrix = inverse([[0.5,1],[1,1.5]])
        np.testing.assert_allclose(matrix, np.asmatrix([[-6,4],[4,-2]]))

    def test_transpose_square(self):
        matrix = transpose([[1,4],[2,3]])
        np.testing.assert_allclose(matrix, [[1,2],[4,3]])

    def test_transpose(self):
        matrix = transpose([[1,4],[2,3], [5,6]])
        np.testing.assert_allclose(matrix, [[1,2,5],[4,3,6]])

    def test_gaussElimination(self):
        matrix = solveGaussElimination([[1,4, 0],[2,3,0]])
        np.testing.assert_allclose(matrix, [0,0])

    def test_gaussElimination_3(self):
        matrix = solveGaussElimination([[1,1,1,9],[2,-3,4,13], [3,4,5,40]])
        np.testing.assert_allclose(matrix, [1,3,5]) 

    def test_gaussElimination_Float(self):
        matrix = solveGaussElimination([[0.5,2, 0],[1,1.5,0]])
        np.testing.assert_allclose(matrix, [0,0])
    

if __name__=="__main__":
    unittest.main()


