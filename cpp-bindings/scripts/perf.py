from typing import List, Callable
import numpy as np
import time
import linalg


def py_matrix_multiply(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    if len(mat1[0]) != len(mat2):
        raise ValueError("Uncompatible matrix shapes")
    result = []
    for i in range(len(mat1)):
        row_result = []
        for j in range(len(mat2[0])):
            sum_val = 0
            for k in range(len(mat2)):
                sum_val += mat1[i][k] * mat2[k][j]
            row_result.append(sum_val)
        result.append(row_result)
    return result

def numpy_cosine(mat1: List[int], mat2: List[int]) -> float:
    return np.dot(mat1, mat2) / (np.linalg.norm(mat1) * np.linalg.norm(mat2))


def test_timings(func: Callable, *args):
    _ = func(*args)
    start_time = time.time()
    _ = func(*args)
    end_time = time.time()
    return round(end_time - start_time, 5)


def compare(matrix_size: int) -> None:
    matrix_a = np.random.rand(matrix_size, matrix_size)
    matrix_b = np.random.rand(matrix_size, matrix_size)

    list_a = matrix_a.tolist()
    list_b = matrix_b.tolist()

    print(
        "Mat mul (Pure Python), size={0}x{0}: {1} seconds".format(
            matrix_size, test_timings(py_matrix_multiply, list_a, list_b)
        )
    )
    print(
        "Mat mul (Pure C++), size={0}x{0}: {1} seconds".format(
            matrix_size, test_timings(linalg.LinearAlgebra.matmulPure, list_a, list_b)
        )
    )
    print(
        "Mat mul (C++ BLAS), size={0}x{0}: {1} seconds".format(
            matrix_size, test_timings(linalg.LinearAlgebra.matmulBlas, list_a, list_b)
        )
    )
    print(
        "Mat mul (Python numpy), size={0}x{0}: {1} seconds\n".format(
            matrix_size, test_timings(np.dot, np.array(list_a), np.array(list_b))
        )
    )

def check_cosine(matrix_size: int) -> None:
    matrix_a = np.random.rand(matrix_size, matrix_size)
    matrix_b = np.random.rand(matrix_size, matrix_size)

    list_a = matrix_a.tolist()
    list_b = matrix_b.tolist()

    print(
        "Cosine (C++ BLAS), size={0}x{0}: {1} seconds".format(
            matrix_size, test_timings(linalg.LinearAlgebra.cosineBlas, list_a, list_b)
        )
    )

    print(
        "Cosine (numpy), size={0}x{0}: {1} seconds".format(
            matrix_size, test_timings(numpy_cosine, list_a, list_b)
        )
    )


if __name__ == "__main__":
    for size in [10, 50, 100, 300, 500, 700]:
        check_cosine(size)
