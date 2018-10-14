#! /usr/bin/python3

start_num = 10
end_num = 32

square = input("Enter number: ")

one_digit_squares = {"1" : 1, "4" : 2, "9" : 3, "16" : 4, "25" : 5, "36" : 6, "49" : 7, "64" : 8, "81" : 9}

last_digit = square[2]
first_digit = square[0]

found_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in one_digit_squares:
    if int(x) > 9:
        if str(int(x)%10) == last_digit:
            found_numbers[one_digit_squares[str(int(x)%10)]-1] = one_digit_squares[str(x)]
    else:
        if x == last_digit:
            found_numbers[one_digit_squares[str(int(x)%10)]-1] = one_digit_squares[str(x)]
print(found_numbers)
# prove theory of finding squareroot for 3 digit number in range
# above


