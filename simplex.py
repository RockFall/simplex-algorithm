from fractions import Fraction
import numpy as np

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

x = get_solution()

def get_solution():
    return np.array()

def is_optimal():
    # returns True if all elements on 'c_N' are <= 0
    return False



def SimplexSolve(c, A, b):

    # Assert shapes are OK
    assert A.shape[0] == b.shape[0], 'first dims of A and b must match, check input!'
    assert A.shape[1] == c.shape[0], 'second dim of A must match first dim of c, check input'

    # ensure A is full rank, drop redundant rows if not



