class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for d in range(len(self.list_2[i])):
                matr [i] [d] = self.list_1[i][d] + self.list_2[i][d]

        return str('\n'.join(['\t'.join([str(d) for d in i]) for i in matr]))


my_matrix = Matrix([[3, 12, 7],
                    [8, 21, 17],
                    [27, 44, 15]],
                   [[5, 9, 4],
                    [15, 25, 30],
                    [32, 50, 47]])


print(my_matrix.__add__())
