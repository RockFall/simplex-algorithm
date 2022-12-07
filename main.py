from simplex import SimplexSolver

def main():
  n, m = [int(i) for i in input().split()]
  c = [int(i) for i in input().split()]
  A = []
  b = []
  for _ in range(n):
    inAb = [int(i) for i in input().split()]
    A.append(inAb[:-1])
    b.append(inAb[-1])

  ss = SimplexSolver(c, A, b)
  ss.solve()

if __name__ == "__main__":
  main()
