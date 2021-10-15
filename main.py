# Strassen's algorithm for matrix multiplication
# Square-Matrix-Multiply(A,B)
# n = A.rows
# let C be a new n * n matrix
# for i = 1 to n
# 	for j = 1 to n
# 		Cij = 0
#       for k = 1 to n
# 			Cij = Cij + Aik * Bkj
# return C

# Performs Multiplication of two array.
# It was created on October 12, 2021.

# Written by Orhan Ozan Yildiz.


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


def main():
    while True:
        # Take the user choices
        print("""
        Press 1 if you want to enter the matrices manually, 
        press 2 to generate random, and
        press 3 to exit.
        """)

        user_input = check_input()

        if user_input == '3':
            break
        elif user_input == '1' or user_input == '2':
            print("Enter the row and column of first matrix")
            col_of_first, row_of_second = check_entered_matrix_dimensions()


def check_input():
    while True:
        reader = input()
        if reader == '1' or reader == '2' or reader == '3':
            print("The entered value is not valid. Please select 1, 2 or 3 values.")
        else:
            break
    return reader
