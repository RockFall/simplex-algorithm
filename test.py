from simplex import SimplexSolver

count = 0

def SolveTest(c, Ab):
  global count

  A = []
  b = []
  for line in Ab:
    A.append(line[:-1])
    b.append(line[-1])

  ss = SimplexSolver(c, A, b)
  print("============== " + str(count) + " ==============")
  ss.solve()
  print("=================================\n")
  count += 1


print("--------------- STARTING TESTS ---------------")
c = [3, 2]
Ab = [[2, 1, 8], [1, 2, 8], [1, 1, 5]]
SolveTest(c, Ab)

c = [2, 4, 8]
Ab = [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]
SolveTest(c, Ab)

c = [1, 1, 1,]
Ab = [[1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1], [1, 1, 1, -1]]
SolveTest(c, Ab)
