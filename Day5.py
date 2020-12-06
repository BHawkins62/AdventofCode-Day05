import math as mt

def calc_seat_pos(code,min,max):
    for char in code:
        if char == 'F' or char == 'L':
            max = max - mt.ceil((max - min)/2)
        elif char == 'B' or char == 'R':
            min = min + mt.ceil((max - min)/2)
        else:
            print(f'Corrupt data, check entry: {code}')
            break
    return min

seat_id = 0
highest_seat_id = 0
lowest_seat_id = 1023
seats_taken = set()


try:
    with open('input.txt', 'r') as data:
        boarding_pass = data.readline()
        while boarding_pass:
            row_code = boarding_pass[:7]
            row = calc_seat_pos(row_code,min=0,max=127)
            column_code = boarding_pass[7:10]
            column = calc_seat_pos(column_code,min=0,max=7)
            seat_id = row * 8 + column
            seats_taken.add(seat_id)
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
            if seat_id < lowest_seat_id:
                lowest_seat_id = seat_id
            # print(f'row is {row} and the column is {column} and the seat number is {seat_id}')
            boarding_pass = data.readline()
        print(f'The highest seat id is {highest_seat_id}')
        all_possible_seats = set(range(0,1024))
        temp_set1 = set(range(0,lowest_seat_id+1))
        temp_set2 = set(range(highest_seat_id,1024))
        temp_set3 = temp_set1.union(temp_set2)
        all_unavailable_seats = temp_set3.union(seats_taken)
        open_seats = all_possible_seats.difference(all_unavailable_seats)
        print(open_seats)
except FileNotFoundError as e:
    print('File Not Found!')
    raise e



