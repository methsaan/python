#! /usr/bin/python3

start_num = 10
end_num = 32

square = input("Enter number: ")

one_digit_squares = {"1" : 1, "4" : 2, "9" : 3, "16" : 4, "25" : 5, "36" : 6, "49" : 7, "64" : 8, "81" : 9}

last_digit = square[2:3]
first_digit = square[0:1]

cnt = 1
cnt2 = 1
cnt3 = cnt
while cnt < 100:
    cnt2 = cnt2 + 2
    cnt += cnt2
    cnt3 = cnt
    cnt3 %= 10
# prove theory of finding squareroot for 3 digit number in range
# above


