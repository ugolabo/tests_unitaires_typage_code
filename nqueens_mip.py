from sys import stdout
from mip import Model, xsum, BINARY
import time

# https://docs.python-mip.com/en/latest/examples.html#n-queens

def scenarios(queens=4):
    ####################
    # Interface
    ####################
    # number of queens
    n = queens
    
    ####################
    # Modélisation
    ####################
    queens = Model()
    
    x = [[queens.add_var('x({},{})'.format(i, j), var_type=BINARY)
          for j in range(n)] for i in range(n)]
    
    # one per row
    for i in range(n):
        queens += xsum(x[i][j] for j in range(n)) == 1, 'row({})'.format(i)
    
    # one per column
    for j in range(n):
        queens += xsum(x[i][j] for i in range(n)) == 1, 'col({})'.format(j)
    
    # diagonal \
    for p, k in enumerate(range(2 - n, n - 2 + 1)):
        queens += xsum(x[i][i - k] for i in range(n)
                       if 0 <= i - k < n) <= 1, 'diag1({})'.format(p)
    
    # diagonal /
    for p, k in enumerate(range(3, n + n)):
        queens += xsum(x[i][k - i] for i in range(n)
                       if 0 <= k - i < n) <= 1, 'diag2({})'.format(p)
    
    ####################
    # Optimisation
    ####################
    queens.optimize()
    
    if queens.num_solutions:
        stdout.write('\n')
        for i, v in enumerate(queens.vars):
            stdout.write('O ' if v.x >= 0.99 else '. ')
            if i % n == n-1:
                stdout.write('\n')

for i in range(1, 11, 1):
    print(f"QUEENS={i}----------------------------------------------------------")
    print(" ")
    scenarios(queens=i)
    time.sleep(1.0)
