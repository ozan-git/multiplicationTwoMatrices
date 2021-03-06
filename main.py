# Performs Multiplication of two array.
# Using Iterative algorithm.
# It was created on October 12, 2021.

# Written by Orhan Ozan Yildiz.
# Random variable generators.
import random


# Checking of matrix dimensions. Matrix sizes are provided to be between 1 and 20.
def check_entered_matrix_dimensions():
	while True:
		reader = input()
		try:
			reader = int(reader)
			if 20 >= reader > 0:
				break
			print("Please enter a value between 1 and 20.")
		except ValueError:
			print("Please enter a valid dimension.")
	return reader


# It creates a matrix of all 0s.
def init_matrix(rows, columns):
	# Python program to create a (m x n) matrix with all 0s
	# input => print([[0 for x in range(5)] for x in range(4)])
	# output => [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	multi_list = [[0 for _ in range(columns)] for _ in range(rows)]
	return multi_list


# It is checked whether the value entered by the user is a number.
# If it is not a number, it is asked to enter a numeric value again.
def check_float():
	while True:
		user_input = input()
		try:
			user_input = float(user_input)
			break
		except ValueError:
			print("Not applicable. Please enter a number.")
	return user_input


# The text from the function is printed on the screen.
# A 2-dimensional matrix is created with nested for loops.
def print_matrix(text, matrix):
	print(text)
	print("::::::::")
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(str(matrix[i][j]) + " ", end=" ")
		print()
	print("::::::::\n")


def user_matrices_data(text, rows, columns):
	print(text)
	matrix = init_matrix(rows, columns)
	for i in range(rows):
		for j in range(columns):
			#  f"" is improved way to format strings.
			print(f"[{i + 1}][{j + 1}]:")
			matrix[i][j] = check_float()
		print_matrix(text, matrix)
	return matrix


def user_matrices(col_of_first, row_of_first, col_of_second, row_of_second):
	first_matrix = user_matrices_data("First matrix is: ", row_of_first, col_of_first)
	second_matrix = user_matrices_data("Second matrix is: ", row_of_second, col_of_second)
	return first_matrix, second_matrix


def matrix_bounds():
	while True:
		print("Enter lower bound of matrix: ")
		lower_bound = check_float()
		print("Enter upper bound of matrix: ")
		upper_bound = check_float()
		if lower_bound < upper_bound:
			break
		print("Not Applicable: The upper bound of the matrix must be greater than its lower bound.")
	return lower_bound, upper_bound


# It generates a random matrix based on the information received from the user.
# The limits of the random numbers to be used are determined by the lower_bound and upper_bound data.
def generate_random_matrix_data(text, rows, columns, lower_bound, upper_bound):
	matrix = init_matrix(rows, columns)

	for i in range(rows):
		for j in range(columns):
			matrix[i][j] = random.uniform(lower_bound, upper_bound)
	print_matrix(text, matrix)
	return matrix


# Data is sent to the random number generating function.
def generate_random_matrices(row_of_first, col_of_first, row_of_second, col_of_second, lower_bound, upper_bound):
	first_matrix = generate_random_matrix_data(
		"First matrix is: ", row_of_first, col_of_first, lower_bound, upper_bound)
	second_matrix = generate_random_matrix_data(
		"Second matrix is: ", row_of_second, col_of_second, lower_bound, upper_bound)
	return first_matrix, second_matrix


# Iterative algorithm
# Input: matrices first matrix and second matrix
# Let C be a new matrix of te appropriate size
# For i from 1 to n:
#     For j from 1 to p:
#        Let sum = 0
#        For k from 1 to m:
#            Set sum <- sum + firstMatrix[i][k] * secondMatrix[k]*[j]
#        Set C[i][j] <- sum
# Return C
# https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm
def matrix_multiplication(first_matrix, second_matrix):
	result_matrix = init_matrix(len(first_matrix), len(second_matrix[0]))

	for i in range(len(first_matrix)):
		for j in range(len(second_matrix[0])):
			temp = 0
			for k in range(len(second_matrix)):
				temp += first_matrix[i][k] * second_matrix[k][j]
			result_matrix[i][j] = temp

	return result_matrix


def main():
	while True:
		# Take the user choices
		print("""
Press 1 to create the matrices yourself, 
Press 2 to randomly generate or 
Press 3 to exit. 
""")
		# The value entered by the user is guaranteed to be 1, 2 or 3.
		user_input = check_input()

		if user_input == '3':
			break
		elif user_input == '1' or user_input == '2':
			print("Enter the column of first matrix (|||): ")
			col_of_first = check_entered_matrix_dimensions()
			print("Enter the row of first matrix (---): ")
			row_of_first = check_entered_matrix_dimensions()

			is_valid = True
			while is_valid:
				print("Enter the row of second matrix (---): ")
				row_of_second = check_entered_matrix_dimensions()

				# For matrix multiplication, the number of columns in the first matrix must be equal to the number of
				# rows in the second matrix. The result matrix has the number of rows of the first and the number of
				# columns of the second matrix.
				if col_of_first == row_of_second:
					print("Enter the column of second matrix (|||): ")
					col_of_second = check_entered_matrix_dimensions()

					is_valid = False
					print("The matrices are valid.")

					# User manual input.
					if user_input == '1':
						first_matrix, second_matrix = \
							user_matrices(col_of_first, row_of_first, col_of_second, row_of_second)
					# User wants to generate random matrix.
					else:
						lower_bound, upper_bound = matrix_bounds()
						first_matrix, second_matrix = generate_random_matrices(
							row_of_first, col_of_first, row_of_second, col_of_second, lower_bound, upper_bound)

					result_matrix = matrix_multiplication(first_matrix, second_matrix)
					print_matrix("Result matrix is: ", result_matrix)

				else:
					print(
						"Not applicable: The column of the first matrix must be equal to the row of the second matrix.\n")


# The value received from the user is expected to be 1 2 or 3. If not, it will be asked again.
def check_input():
	while True:
		reader = input()
		if reader == '1' or reader == '2' or reader == '3':
			break
		else:
			print("The entered value is not valid. Please select 1, 2 or 3 values.")
	return reader


if __name__ == "__main__":
	main()
