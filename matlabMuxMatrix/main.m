% Performs Multiplication of two array.
% It was created on October 12, 2021.

% Written by Orhan Ozan Yildiz.
%% Clear memory and screen.
clear, clc, close all;

while true
% Ask the user to select an option. 
	disp("Press 1 to create the matrices manually,")
    disp("press 2 to generate random, or")
    disp("press 3 to exit.")
    
    user_input = check_input();
    
    if user_input == '3'
        break
        
    elseif (user_input == '1' || user_input == '2')
        
        row_of_first = check_entered_matrix_dimensions ...
            ('Enter the row of first matrix (---): ');
        
        col_of_first = check_entered_matrix_dimensions ...
            ('Enter the column of first matrix (|||): ');
        
        is_valid = true;
        while is_valid

            row_of_second = check_entered_matrix_dimensions ... 
                ('Enter the row of first matrix (---): ');
            
            if (col_of_first == row_of_second)

                col_of_second = check_entered_matrix_dimensions ...
                    ('Enter the column of second matrix (|||): ');
                
                is_valid = false;
                disp('')
                disp("The matrices are valid.")
                
                % User manual input.
                if (user_input == '1')
                    [first_matrix, second_matrix] = user_matrices ...
                        (row_of_first, col_of_first, ...
                         row_of_second, col_of_second);
                else
                    [lower_bound, upper_bound] = matrix_bounds();
                    [first_matrix, second_matrix] = generate_random_matrices ...
                        (row_of_first, col_of_first, row_of_second, col_of_second, ...
                         lower_bound, upper_bound);
                end
                result = matrix_multiplication(first_matrix, second_matrix);
                print_matrix('Result matrix is: ', result)
            else
                disp("Not applicable: The column of the first matrix must be equal to the row of the second matrix.")
                disp(" ")
            end
        end
    end
end

% Iterative algorithm
% Input: matrices first matrix and second matrix
% Let C be a new matrix of te appropriate size
% For i from 1 to n:
%     For j from 1 to p:
%        Let sum = 0
%        For k from 1 to m:
%            Set sum <- sum + firstMatrix[i][k] * secondMatrix[k]*[j]
%        Set C[i][j] <- sum
% Return C
% https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm
function result = matrix_multiplication(first_matrix, second_matrix)
    % It creates a matrix of all 0s.
    result = zeros(size(first_matrix, 1), size(second_matrix, 2));
    
    for i = 1:size(first_matrix, 1)
        for j = 1:size(second_matrix, 2)
            temp = 0;
            for k = 1:size(second_matrix, 1)
                temp = temp + first_matrix(i,k) * second_matrix(k,j);
            result(i,j) = temp;
            end
        end
    end
end

% The value received from the user is expected to be 1 2 or 3. If not, it will be asked again.
function reader = check_input
    while true
        reader = input('', 's');
        try
            if (reader ~= '1' && reader ~= '2' && reader ~= '3')
                throw(MException('MATLAB:invalidInputValue', ...
                   'Error invalid input.'))
            end
            break
        catch
            disp("The entered value is not valid. Please select 1, 2 or 3 values.")
        end
    end      
end

% It is checked whether the value entered by the user is a number.
% If it is not a number, it is asked to enter a numeric value again.
function doubleInput = check_float(text)
    disp(text)
    while true
        reader = input('', 's');
        try
            doubleInput = str2double(reader);
            if (isnan(doubleInput))
                throw(MException('Matlab:InvalidDoubleNumber','Error invalid input.'))
            end
            break
        catch
            disp('Please enter a number.')
        end
    end
end

% Checking of matrix dimensions. Matrix sizes are provided to be between 1 and 20.
function reader = check_entered_matrix_dimensions(text)
    disp(text)
    while true
        try
            reader = check_float('');
            if (~(isinf(reader)) && (floor(reader) == reader))
                if  21 > reader && 0 < reader
                    break
                end
                disp('Please enter a value between 1 and 20.')
            else
                disp('Please enter a number.')
            end
        catch
            disp('Please enter a valid dimension.')
        end
    end
end


function matrix = user_matrices_data(text, rows, columns)
    disp(text)
    % It creates a matrix of all 0s.
    matrix = zeros(rows, columns);
    
    for i = 1:rows
        for j = 1:columns
            fprintf('[%d][%d]: ', i, j)
            matrix(i, j) = check_float('');
        end
    end
    print_matrix(text, matrix)
end


function [first_matrix, second_matrix] = user_matrices  ...
    (row_of_first, col_of_first, ...
     row_of_second, col_of_second)
              
    first_matrix = user_matrices_data('First matrix is: ', ...
        row_of_first, col_of_first);
    
    second_matrix = user_matrices_data('Second matrix is: ', ...
        row_of_second, col_of_second);
end


function [lower_bound, upper_bound] = matrix_bounds
    while true
        lower_bound = check_float('Enter lower bound of matrix: ');
        upper_bound = check_float('Enter upper bound of matrix: ');
        
        if lower_bound < upper_bound
            break
        end
        disp('Not Applicable: The upper bound of the matrix must be greater than its lower bound.')
    end
end

% It generates a random matrix based on the information received from the user.
% The limits of the random numbers to be used are determined by the lower_bound and upper_bound data.
function matrix = generate_random_matrix_data ...
    (text, rows, columns, lower_bound, upper_bound)
    % It creates a matrix of all 0s.
    matrix = zeros(rows, columns);
    
    for i = 1:rows
        for j = 1:columns
            matrix(i, j) = randi([lower_bound, upper_bound]);
        end
    end
    print_matrix(text, matrix)
end

function [first_matrix, second_matrix] = generate_random_matrices ...
    (row_of_first, col_of_first, row_of_second, col_of_second, ...
     lower_bound, upper_bound)
    
	first_matrix = generate_random_matrix_data ...
        ("First matrix is: ", row_of_first, col_of_first, lower_bound, upper_bound);
    
	second_matrix = generate_random_matrix_data ...
        ("Second matrix is: ", row_of_second, col_of_second, lower_bound, upper_bound);
end
    
% The text from the function is printed on the screen.
% A 2-dimensional matrix is created with nested for loops.
function print_matrix(text, matrix)
    disp(' ')
    disp(text)
	disp("**************")
    for i = 1:size(matrix, 1)
        for j = 1:size(matrix, 2)
            fprintf('%d ', matrix(i, j))
        end
        disp(' ')
    end
    disp('**************')
end