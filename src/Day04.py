from dataclasses import dataclass

@dataclass
class Number:
    value: int
    marked: bool

@dataclass
class NumberBingo:
    value: int
    marked: bool
    bingo: bool

def part1(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()
        file_content = [line.strip().replace("  ", " ") for line in file_content]

    draw_order = file_content[0].split(',')

    #remove draw order and empty lines from input
    file_content = list(filter(lambda item: item != "", file_content[1:]))

    board_size = 5

    boards = [file_content[i:i + board_size] for i in range(0, len(file_content), board_size)]

    marked_rows = []

    for board in boards:
        for row in board:
            numbers = row.split(" ")
            marked_rows.append([Number(int(num),False) for num in numbers])

    marked_boards = [marked_rows[i:i + board_size] for i in range(0, len(marked_rows), board_size)]
    
    bingo = False

    for number in draw_order:
        if bingo:
            break
        for board in marked_boards:
            for row in board:
                for num in row:
                    if num.value == int(number):
                        num.marked = True

                    row_bingo = all(num.marked for num in row)

                    column_bingo = False
                    for i in range(board_size):
                        if not all(row[i].marked for row in board):
                            continue
                        column_bingo = True

                    if row_bingo or column_bingo:
                        bingo = True
                        winning_board = board
                        winning_number = int(number)

    score = 0
    for row in winning_board:
        for num in row:
            if num.marked:
                continue
            score += num.value
    
    print(score, winning_number)

    return score*winning_number

def part2(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()
        file_content = [line.strip().replace("  ", " ") for line in file_content]

    draw_order = file_content[0].split(',')

    #remove draw order and empty lines from input
    file_content = list(filter(lambda item: item != "", file_content[1:]))

    board_size = 5

    boards = [file_content[i:i + board_size] for i in range(0, len(file_content), board_size)]

    marked_rows = []

    for board in boards:
        for row in board:
            numbers = row.split(" ")
            marked_rows.append([NumberBingo(int(num),False, False) for num in numbers])

    marked_boards = [marked_rows[i:i + board_size] for i in range(0, len(marked_rows), board_size)]

    last_one_left = False
    
    for number in draw_order:
        if last_one_left:
            break
        for board in marked_boards[:]:
            for row in board:
                for num in row:
                    if num.value == int(number):
                        num.marked = True

                    row_bingo = all(num.marked for num in row)

                    column_bingo = False
                    for i in range(board_size):
                        if not all(row[i].marked for row in board):
                            continue
                        column_bingo = True

                    if row_bingo or column_bingo:
                        if len(marked_boards) > 1:
                            num.marked = False
                            marked_boards.remove(board)

                        else:
                            last_winning_board = board
                            last_winning_number = int(number)
                            last_one_left = True

    score = 0
    for row in last_winning_board:
        for num in row:
            if num.marked:
                continue
            score += num.value
    
    print(score, last_winning_number)
    
    return score*last_winning_number
    
inputfile = "Day04.txt"

print(part1(inputfile))
print(part2(inputfile))