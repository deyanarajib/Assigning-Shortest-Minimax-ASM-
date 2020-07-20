# Assigning-Shortest-Minimax-ASM-
A method for solving Transportation Problem

ASM Method Algorithm
Step 1: Construct the transportation table from given transportation problem.
Step 2: Subtract each row entries of the transportation table from the respective row minimum and then subtract each column entries of the resulting transportation table from respective column minimum.
Step 3: Now there will be at least one zero in each row and in each column in the reduced cost matrix. Select the first zero (row-wise) occurring in the cost matrix. Suppose (i, j)th zero is selected, count the total number of zeros (excluding the selected one) in the ith row and jth column. Now select the next zero and count the total number of zeros in the corresponding row and column in the same manner. Continue it for all zeros in the cost matrix.
Step 4: Now choose a zero for which the number of zeros counted in step 3 is minimum and supply maximum possible amount to that cell. If tie occurs for some zeros in step 3 then choose a (k.l)th zero breaking tie such that the total sum of all the elements in the kth row and lth column is maximum. Allocate maximum possible amount to that cell.
Step 5: After performing step 4, delete the row or column for further calculation where the supply from a given source is depleted or the demand for a given destination is satisfied.
Step 6: Check whether the resultant matrix possesses at least one zero in each row and in each column. If not, repeat step 2, otherwise go to step 7.
Step 7: Repeat step 3 to step 6 until and unless all the demands are satisfied and all the supplies are exhausted.

Source: B. Satheesh Kumara,*, R. Nandhinib and T. Nanthinic: "A comparative study of ASM and NWCR method in transportation problem", Malaya J. Mat. 5(2)(2017) 321–327.

Algorithm of the revised version of ASM-Method
Step 1 : Construct the transportation tableau from given TP. Check whether the problem is balanced or not. If the problem is balanced, go to Step 4, otherwise go to Step 2.
Step 2 : If the problem is not balanced, then any one of the following two cases may arise:
	a) If total supply exceeds total demand, introduce an additional dummy column to the transportation table to absorb the excess supply. The unit transportation cost for the cells in this dummy column is set to ‘M’, where M > 0 is a very large but finite positive quantity. or
	b) If total demand exceeds total supply, introduce an additional dummy row to the transportation table to satisfy the excess demand. The unit transportation cost for the cells in this dummy row is set to ‘M’, where M>0 is a very large but finite positive quantity.
Step 3 : 
	a) In case (a) of Step 2, identify the lowest element of each row and subtract it from each element of the respective row and then, in the resulting tableau, identify the lowest element of each column and subtract it from each element of the respective column and go to Step 5. or
	b) In case (b) of Step 2, identify the lowest element of each column and subtract it from each element of the respective column and then, in the resulting tableau, identify the lowest element of each row and subtract it from each element of the respective row and go to Step 5.
Step 4 : Identify the lowest element of each row and subtract it from each element of the respective row and then, in the resulting tableau, identify the lowest element of each column and subtract it from each element of the respective column.
Step 5 : In the reduced tableau, each row and each column contains at least one zero. Now, select the first zero (say zero) and count the number of zeros (excluding the selected one) in the row and column and record as a subscript of selected zero. Repeat this process for all zeros in the transportation tableau.
Step 6 : Now, choose the cell containing zero for which the value of subscript is minimum and supply maximum possible amount to that cell. If tie occurs for 268 Abdul Quddoos et al. some zeros in Step 5, choose the cell of that zero for breaking tie such that the sum of all the elements in the row and column is maximum. Supply maximum possible amount to that cell.
Step 7 : Delete that row (or column) for further consideration for which the supply from a given source is exhausted (or the demand for a given destination is satisfied). If, at any stage, the column demand is completely satisfied and row supply is completely exhausted simultaneously, then delete only one column (or row) and the remaining row (or column) is assigned a zero supply (or demand) in further calculation.
Step 8 : Now, check whether the reduced tableau contains at least one zero in each row and each column. If this does not happens, repeat Step 4 otherwise go to Step 9.
Step 9 : Repeat Step 5 to Step 8 till all the demands are satisfied and all the supplies are exhausted.

Source: Abdul Quddoos, Shakeel Javaid* and M. M. Khalid: "A Revised Version of ASM-Method for Solving Transportation Problem", Int. J. Agricult. Stat. Sci. Vol. 12, Supplement 1, pp. 267-272, 2016.
