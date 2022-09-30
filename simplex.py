from fractions import Fraction
import numpy as np

class SimplexSolver:
    def __init__(self, c, A, b=[]):
        self.A = np.array(A)

        if len(b) == 0:
            # we must get b from last col of A
            b = A[:,-1]
            self.Ab = np.copy(self.A)
            self.A = np.delete(self.A, -1, 1)
        else:
            self.b = np.array(b)
            # only catenating b as last column of A
            self.Ab = np.hstack((A,b[:,None]))


    def solve(self):
         # it creates the self.tableau variable
        self._build_initial_tableau()

    def _build_initial_tableau(self):
        pass


# Input
n = 2 # nº Restrições
m = 2 # nº Variáveis
c_input = [1, 1] # Vetor de custo c^T
Ab_input = [[1, 0, 3], [2, 3, 24]] # Restrictions + b

A = np.array()
b = np.array()
c = np.array(c_input)

# Restrições do sistema
# 0 <= n <= 100
# 0 <= m <= 100
# for i in range(n+1)
#    b[i] <= 100
#    c[i] <= 100
#    for j in range(m+1)
#       a[i][j] <= 100

# Primeiro vamos assumir a corrute completa do 
# input e depois com tempo adicionamos as restrições
# de forma explícita



def get_solution():
    return np.array()

def is_optimal():
    # returns True if all elements on 'c_N' are <= 0
    return False



def SimplexSolve(c, A, b):
    tableau = build_initial_tableau()

    x = get_solution()



