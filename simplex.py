import numpy as np
from tabulate import tabulate

class SimplexSolver:
    def __init__(self, c, A, b=[]):
        self.A = np.array(A)
        self.c = np.array(c)

        if len(b) == 0:
            # we must get b from last col of A
            b = A[:,-1]
            self.Ab = np.copy(self.A)
            self.A = np.delete(self.A, -1, 1)
        else:
            self.b = np.array(b)
            # only catenating b as last column of A
            self.Ab = np.column_stack((self.A,self.b))

        self.numVars = self.c.size
        self.numRestr = self.A.shape[0]


    def solve(self):
        self._debug_ite_count = 0 # !: DEBUG ONLY

         # it creates the self.tableau variable
        self._build_initial_tableau()
        self._print_tableau() # !: DEBUG ONLY

        # starts solving
        while self._is_optimal() == False:
            #if self._is_unlimited_all():
            #    self.type = "ilimitada"
            #    self._print_results()
            #    return False

            pivot = self._find_next_pivot()
            self._do_pivot(pivot)

            self._print_tableau() # !: DEBUG ONLY
            self._debug_ite_count += 1 # !: DEBUG ONLY

        self.optimal_obj_value = self.tableau[0,-1]

        if self.optimal_obj_value >= 0:
            self.type = "otima"
            z = np.zeros(self.tableau.shape[1])
            z[self.identity_columns] = self.tableau[1:, -1]
            self.optimal_solution = z[self.numRestr:-(1+self.numRestr)]
        else:
            self.type = "inviavel"

        self._print_results()
        return True

    def _build_initial_tableau(self):
        # Creating top section i.e. [0 0 | -c1 -c2 -c3 -c4 0 0 | 0]
        restr_count = self.numRestr
        top = np.concatenate(([0 for i in range(restr_count)], np.negative(self.c)))
        top = np.append(top, [0 for i in range(restr_count)])
        top = np.append(top, 0)

        # adding slack variables, b and top
        tableau = np.column_stack((np.identity(restr_count), self.A))
        tableau = np.hstack((tableau, np.identity(restr_count)))
        tableau = np.column_stack((tableau, self.b))
        tableau = np.vstack((top, tableau))

        self.identity_columns = np.arange(tableau.shape[1]-(restr_count+1), tableau.shape[1]-1)
        self.tableau = tableau

    def _is_optimal(self):
        has_negative = np.any((self.tableau[0][self.numRestr:-1] < 0))
        return not has_negative

    def _get_cadidates(self):
        # finds all negative entries on the valid top section
        neg_idxs = np.where(self.tableau[0] < 0)[0]
        neg_idxs = neg_idxs[neg_idxs >= self.numRestr]
        return neg_idxs

    def _find_next_pivot(self):
        # picks the index of the first negative entry on the top
        candidates = self._get_cadidates()
        for candidate in candidates:
            column_idx = candidate
            # select the index of the min of each (b_i / A_i)
            np.seterr(divide='ignore')
            possibilities = self.tableau[1:,-1]/self.tableau[1:,column_idx]
            if np.all((possibilities < 0)|(possibilities == np.inf)):
                continue
            row_idx = np.argmin(possibilities) + 1
            return [row_idx, column_idx]

        # if we get here then all candidates lead to impossible choices



    def _is_unlimited(self, idx):
        all_negative = (self.tableau[1:, idx]).all(axis=0)
        return all_negative

    def _is_unlimited_all(self):
        any_full_negative_cadidate = np.any((self.tableau[1:,self._get_cadidates()] < 0).all(axis=0))
        return any_full_negative_cadidate

    def _do_pivot(self, pivot):
        # Divide pivot line by itself
        self.tableau[pivot[0]] = self.tableau[pivot[0]] / (self.tableau[pivot[0], pivot[1]])
        # Gaussian elimination
        multiplier = np.divide(np.negative(self.tableau[:,pivot[1]]), (self.tableau[pivot[0], pivot[1]]))
        multiplier = np.delete(multiplier, pivot[0])
        self.tableau[np.arange(self.numRestr+1) != pivot[0], :] += np.dot(multiplier.reshape(self.numRestr,1), self.tableau[pivot[0]].reshape(1,self.tableau[0].size))

        # Mark this column as an identity one
        self.identity_columns[pivot[0]-1] = pivot[1]

    def _print_tableau(self): # !: DEBUG ONLY
        print("Iteration: " + str(self._debug_ite_count))
        print(tabulate(self.tableau, headers='firstrow', stralign='center', tablefmt='fancy_grid'))
        print("\n\n")

#
#   _________________________________________________
# [ 0.     0.     0.     1.     9.124 -1.     5.     0.   ]
# ------------------------------------------------
# | 1.000 0.000 0.000 || 1.523 2.897 2.329 | 9.121

    def _print_results(self):
        print(self.type)
        if self.type == "otima":
            print(self.optimal_obj_value)
            # Print arrays as: [1. 1. 1.] -> 1 1 1
            solution = ""
            for num in self.optimal_solution:
                solution += str(int(num)) + " "
            print(solution[:-1])
            solution = ""
            for num in self.tableau[0][:self.numRestr]:
                solution += str(int(num)) + " "
            print(solution[:-1])
        elif self.type == "ilimitada":
            print("certificado")
        elif self.type == "inviavel":
            print(self.tableau[0][:self.numRestr])
