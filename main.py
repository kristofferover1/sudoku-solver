# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from mip import Model, xsum, maximize, BINARY

I = range(9) #rows
J = range(9) #columns
K = range(9) #possible values

m = Model()

#Decision variable: Boolean: Value is k in square i,j
x = [[[m.add_var("x({},{},{})".format(i, j, k), var_type=BINARY) for k in K] for j in J] for i in I]

# each square shall have exactly one value
for i in I:
    for j in J:
        m += xsum(x[i][j][k] for k in K) == 1

# each value shall be represented exaclty once per row
for i in I:
    for k in K:
        m += xsum(x[i][j][k] for j in J) == 1

# each value shall be represented exaclty once per column
for j in J:
    for k in K:
        m += xsum(x[i][j][k] for i in I) == 1

# # each value shall be represented exactly once per 3x3 sub-board
for u in range(3):
    for v in range(3):
        for k in K:
            m += xsum(x[3*u+i][3*v+j][k] for i in range(3) for j in range(3)) == 1


#Input given values (readability must be improved..)

m += x[0][4][7] == 1

m += x[0][8][1] == 1


m += x[1][0][7] == 1
m += x[1][2][3] == 1
m += x[1][3][2] == 1
m += x[1][8][0] == 1


m += x[2][0][8] == 1
m += x[2][1][1] == 1

m += x[3][5][8] == 1
m += x[3][8][3] == 1

m += x[4][1][4] == 1

m += x[5][3][6] == 1
m += x[5][4][0] == 1
m += x[5][6][4] == 1
m += x[5][7][1] == 1

m += x[6][1][3] == 1
m += x[6][5][6] == 1
m += x[6][7][7] == 1

m += x[7][3][1] == 1
m += x[7][4][5] == 1
m += x[7][7][4] == 1

m += x[8][3][0] == 1
m += x[8][6][2] == 1
m += x[8][8][6] == 1


# solve feasibility problem
m.optimize()


#print solution
for i in I:
    lst = []
    for j in J:
        for k in K:
            if x[i][j][k].x == 1:
                lst.append(k+1)
    print(lst)

