RED = 12
GREEN = 13
BLUE = 14

COLOR_DICT = {"red": RED, "green": GREEN, "blue": BLUE}

def part1(clues):
    possible = True
    for clue in clues:
        denoms = clue.split(", ")
        for denom in denoms:
            num, color = denom.split(" ")
            if color[-1] == '\n':
                color = color[:-1]
            if int(num) > COLOR_DICT[color]:
                possible = False
    return possible

def parse_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    possible_games = 0
    for line in lines:
        game, records = line.split(": ")[0], line.split(": ")[1]
        id = int(game.split(" ")[1])
        clues = records.split("; ")
        if part1(clues):
            possible_games += id
    return possible_games
        