# Strassen's algorithm for matrix multiplication
# Square-Matrix-Multiply(A,B)
# n = A.rows
# let C be a new n * n matrix
# for i = 1 to n
# 	for j = 1 to n
# 		Cij = 0
#		for k = 1 to n
# 			Cij = Cij + Aik * Bkj
# return C

# Performs Multiplication of two array.
# It was created on October 12, 2021.

# Written by Orhan Ozan Yildiz.
def strassen(A: List, B: List) --> List:
