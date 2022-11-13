from simplex import SimplexSolver

count = 0

def SolveTest(c, Ab, debug=False):
  global count

  A = []
  b = []
  for line in Ab:
    A.append(line[:-1])
    b.append(line[-1])

  ss = SimplexSolver(c, A, b, debug=debug)
  print("============== " + str(count) + " ==============")
  ss.solve()
  print()
  count += 1

test_cases = [1, 2, 3, 4]


print("--------------- STARTING TESTS ---------------")
if 5 in test_cases:
  c = [3, 2]
  Ab = [[2, 1, 8], [1, 2, 8], [1, 1, 5]]
  SolveTest(c, Ab, debug=True)

if 6 in test_cases:
  c = [1,2,-1,3]
  Ab = [[1,5,2,1,7], [-2,-9,0,3,-13]]
  SolveTest(c, Ab, debug=False)

# ESPECIFICAÇÃO

if 1 in test_cases:
  c = [2, 4, 8]
  Ab = [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]
  SolveTest(c, Ab, debug=False)

if 2 in test_cases:
  c = [1, 1, 1]
  Ab = [[1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1], [1, 1, 1, -1]]
  SolveTest(c, Ab, debug=False)

if 3 in test_cases:
  c = [1, 0, 0]
  Ab = [[-1, 1, 0, 5], [-1, 0, 1, 7]]
  SolveTest(c, Ab, debug=False)

if 4 in test_cases:
  c = [-3, -4, 5, -5]
  Ab = [[1, 1, 0, 0, 5],[-1, 0, -5, 5, -10],[2, 1, 1, -1, 10],[-2, -1, -1, 1, -10]]
  SolveTest(c, Ab, debug=False)
