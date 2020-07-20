import sys
import numpy as np

from Setup import Transportation

class AssigningShortestMinimax:

    def __init__(self, trans):

        self.trans = trans
        self.table = trans.table.copy()
        self.alloc = []

    def allocation(self, x, y):
        
        mins = min([self.table[x, -1], self.table[-1, y]])
        self.alloc.append([self.table[x, 0], self.table[0, y], mins])
        
        if self.table[x, -1] < self.table[-1, y]:
            #delete row and supply x then change value of demand y
            self.table = np.delete(self.table, x, 0)
            self.table[-1, y] -= mins
            
        elif self.table[x, -1] > self.table[-1, y]:
            #delete column and demand y then change value of supply x
            self.table = np.delete(self.table, y, 1)
            self.table[x, -1] -= mins
            
        else:
            #delete row and supply x, column and demand y
            self.table = np.delete(self.table, x, 0)
            self.table = np.delete(self.table, y, 1)

    def reduce_rows(self):
        mins = np.min(self.table[1:-1, 1:-1], 1).reshape(-1, 1)
        self.table[1:-1, 1:-1] -= mins

    def reduce_cols(self):
        mins = np.min(self.table[1:-1, 1:-1], 0)
        self.table[1:-1, 1:-1] -= mins

    def select_index(self):
        zeros = np.argwhere(self.table[1:-1, 1:-1] == 0)
        n = zeros.shape[0]

        a, b, c = np.zeros((3, n))
        for i, (x, y) in enumerate(zeros):
            xx = list(self.table[x + 1, 1:-1])
            yy = list(self.table[1:-1, y + 1])
            
            a[i] = (xx.count(0) - 1) + (yy.count(0) -1)
            b[i] = sum(xx) + sum(yy)
            c[i] = (self.table[x + 1, -1] + self.table[-1, y + 1]) / 2

        mask = a == min(a)
        if len(a[mask]) > 1:
            select = np.zeros(n)
            select[mask] = b[mask]

            mask = np.all([mask, b == max(b)], 0)
            if len(select[mask]) > 1:
                
                select = np.array([np.inf] * n)
                select[mask] = c[mask]
                return zeros[np.argmin(select)]
            else:
                return zeros[np.argmax(select)]
        else:
            return zeros[np.argmin(a)]

    def revision(self):

        if self.table[-2, 1:-1].sum() == 0:
            #table has dummy row
            mins = np.min(self.table[1:-2, 1:-1], 0)
            self.table[1:-2, 1:-1] -= mins
            self.table[-2, 1:-1] = mins.copy()
            self.reduce_rows()
            self.table[-2, 1:-1] = max(self.table[-2, 1:-1]) - self.table[-2, 1:-1]

        elif self.table[1:-1, -2].sum() == 0:
            #table has dummy column
            mins = np.min(self.table[1:-1, 1:-2], 1)
            self.table[1:-1, 1:-2] -= mins.reshape(-1, 1)
            self.table[1:-1, -2] = mins.copy()
            self.reduce_cols()
            self.table[1:-1, -2] = max(self.table[1:-1, -2]) - self.table[1:-1, -2]
            
    def solve(self, show_iter=False, revision=False):

        if revision:
            #use ASM revision algorithm
            self.revision()
            if show_iter:
                self.trans.print_frame(self.table)

        while self.table.shape != (2, 2):

            self.reduce_rows()
            self.reduce_cols()
            x, y = self.select_index()
            self.allocation(x + 1, y + 1)

            if show_iter:
                self.trans.print_frame(self.table)
            
        return np.array(self.alloc, dtype=object)


if __name__ == "__main__":

    #example 1 balance problem
    cost = np.array([[11, 13, 17, 14],
                    [16, 18, 14, 10],
                    [21, 24, 13, 10]])
    supply = np.array([250, 300, 400])
    demand = np.array([200, 225, 275, 250])

    #example 2 unbalance problem
    cost = np.array([[2, 7, 14],
                     [3, 3,  1],
                     [5, 4,  7],
                     [1, 6,  2]])
    supply = np.array([5, 8, 7, 15])
    demand = np.array([7, 9, 18])

    #initialize transportation problem
    trans = Transportation(cost, supply, demand)

    #setup transportation table.
    #minimize=True for minimization problem, change to False for maximization, default=True.
    #ignore this if problem is minimization and already balance
    trans.setup_table(minimize=True)

    #initialize ASM method with table that has been prepared before.
    ASM = AssigningShortestMinimax(trans)

    #solve problem and return allocation lists which consist n of (Ri, Cj, v)
    #Ri and Cj is table index where cost is allocated and v it's allocated value.
    #(R0, C1, 3) means 3 cost is allocated at Row 0 and Column 1.
    #show_iter=True will showing table changes per iteration, default=False.
    #revision=True will using ASM Revision algorithm for unbalance problem, default=False.
    allocation = ASM.solve(show_iter=False, revision=False)

    #print out allocation table in the form of pandas DataFrame.
    #(doesn't work well if problem has large dimension).
    trans.print_table(allocation)

#Result from example problem above
'''
example 1 balance problem
             C0       C1       C2       C3 Supply
R0       11(25)  13(225)       17       14    250
R1      16(175)       18       14  10(125)    300
R2           21       24  13(275)  10(125)    400
Demand      200      225      275      250    950

TOTAL COST: 12075

example 2 unbalance problem
          C0    C1    C2 Dummy Supply
R0         2  7(4)    14  0(1)      5
R1         3     3  1(8)     0      8
R2         5  4(5)  7(2)     0      7
R3      1(7)     6  2(8)     0     15
Demand     7     9    18     1     35

TOTAL COST: 93

example 2 unbalance problem (revision)
          C0    C1     C2 Dummy Supply
R0      2(2)  7(2)     14  0(1)      5
R1         3     3   1(8)     0      8
R2         5  4(7)      7     0      7
R3      1(5)     6  2(10)     0     15
Demand     7     9     18     1     35

TOTAL COST: 79
'''
