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

def part2(clues):
    power = 1
    current_maxes = {"red": 0, "green": 0, "blue": 0}
    for clue in clues:
        denoms = clue.split(", ")
        for denom in denoms:
            num, color = denom.split(" ")
            num = int(num)
            if color[-1] == '\n':
                color = color[:-1]
            if current_maxes[color] < num:
                current_maxes[color] = num
    for col in current_maxes:
        power *= current_maxes[col]
    return power

def parse_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    possible_games = 0
    power_sum = 0
    for line in lines:
        game, records = line.split(": ")[0], line.split(": ")[1]
        id = int(game.split(" ")[1])
        # each game has a few clues
        clues = records.split("; ")
        power_sum += part2(clues)
    return power_sum
        