
from csp import *


class SudokuCSP(CSP):

    def __init__(self, board):

        self.domains = {}
        self.neighbors = {}

        for v in range(81):
            self.neighbors.update({'CELL' + str(v): {}})
        for i in range(9):
            for j in range(9):
                name = (i * 9 + j)
                var = "CELL"+str(name)
                self.add_neighbor(var, self.get_row(i) | self.get_column(j) | self.get_square(i, j))
                if board[i][j] != 0:
                    self.domains.update({var: str(board[i][j])})
                else:
                    self.domains.update({var: '123456789'})

        CSP.__init__(self, None, self.domains, self.neighbors, different_values_constraint)


    def get_square(self, i, j):
        if i < 3:
            if j < 3:
                return self.get_square_box(0)
            elif j < 6:
                return self.get_square_box(3)
            else:
                return self.get_square_box(6)
        elif i < 6:
            if j < 3:
                return self.get_square_box(27)
            elif j < 6:
                return self.get_square_box(30)
            else:
                return self.get_square_box(33)
        else:
            if j < 3:
                return self.get_square_box(54)
            elif j < 6:
                return self.get_square_box(57)
            else:
                return self.get_square_box(60)


    def get_square_box(self, index):
        tmp = set()
        tmp.add("CELL"+str(index))
        tmp.add("CELL"+str(index+1))
        tmp.add("CELL"+str(index+2))
        tmp.add("CELL"+str(index+9))
        tmp.add("CELL"+str(index+10))
        tmp.add("CELL"+str(index+11))
        tmp.add("CELL"+str(index+18))
        tmp.add("CELL"+str(index+19))
        tmp.add("CELL"+str(index+20))
        return tmp

    def get_column(self, index):
        return {'CELL'+str(j) for j in range(index, index+81, 9)}

    def get_row(self, index):
            return {('CELL' + str(x + index * 9)) for x in range(9)}

    def add_neighbor(self, var, elements):

        self.neighbors.update({var: {x for x in elements if x != var}})

