from simplex import SimplexSolver
import os

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

def SolveFile(input, debug=False):
  with open("Testes/" + filename, 'r') as file:
      input = []
      for line in file:
        input.append(line)

      n, m = [int(i) for i in input[0].split()]
      c = [int(i) for i in input[1].split()]
      A = []
      b = []
      for l in range(n):
        inAb = [int(i) for i in input[2+l].split()]
        A.append(inAb[:-1])
        b.append(inAb[-1])
      ss = SimplexSolver(c, A, b, debug=debug)
      ss.solve()


test_cases = []
files_tests = True
file_test_cases = []
debug = False


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

if files_tests:
  i = 1
  tests = os.listdir("Testes")
  tests.sort()
  for filename in tests:
    if len(file_test_cases) != 0 and int(filename) not in file_test_cases:
      continue
    print("============== " + filename + " ==============")
    i+=1
    print("         My result:")
    SolveFile("Testes/" + filename, debug=debug)

    print("         Correct:")
    with open("Saidas/" + filename, 'r') as file:
      for line in file:
        if line[-1] == '\n':
          line = line[0:-1]
        print(line)



