class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        new_matrix = []
        if not len(self.lists) == len(other.lists):
            raise ValueError('matrix sizes do not match')
        else:
            for i in range(len(self.lists)):
                new_matrix.append([])
                for k in range(len(self.lists[0])):
                    new_matrix[i].append(self.lists[i][k] + other.lists[i][k])
        return Matrix(new_matrix)


pre_matrix_1 = [[9, 6, 3], [7, 8, 2], [43, 22, 1]]
pre_matrix_2 = [[1, 2, 3], [5, 2, 3], [-5, -8, 22]]

matrix1 = Matrix(pre_matrix_1)
matrix2 = Matrix(pre_matrix_2)

print(f"first matrix: \n{matrix1}")
print(f"second matrix: \n{matrix2}")
print(f"matrix sum: \n{(matrix2 + matrix1)}")
