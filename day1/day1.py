def part1(line):
    line_length = len(line) - 1
    p1, p2 = 0, line_length - 1
    num1, num2 = '', ''
    p1_parsed = False
    p2_parsed = False
    while (not p1_parsed) or (not p2_parsed):
        if line[p1] in "1234567890" and (not p1_parsed):
            num1 = line[p1]
            p1_parsed = True
        if line[p2] in "1234567890" and (not p2_parsed):
            num2 = line[p2]
            p2_parsed = True
        p1 += 1
        p2 -= 1
    print("NUM1, NUM2", num1 + num2)
    return int(num1 + num2)

def part2(line):
    valid_nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    line_length = len(line) - 1
    p1, p2 = 0, line_length - 1
    num1, num2 =  0, 0
    p1_parsed = False
    p2_parsed = False

    while (not p1_parsed) or (not p2_parsed):
        if p1 <= line_length - 3:
            if line[p1:p1+3] in valid_nums and (not p1_parsed):
                num1 = valid_nums[line[p1:p1+3]]
                p1_parsed = True
        if p2 <= line_length - 3:
            if line[p2:p2+3] in valid_nums and (not p2_parsed):
                num2 = valid_nums[line[p2:p2+3]]
                p2_parsed = True
        if p1 <= line_length - 4:
            if line[p1:p1+4] in valid_nums and (not p1_parsed):
                num1 = valid_nums[line[p1:p1+4]]
                p1_parsed = True
        if p2 <= line_length - 4:
            if line[p2:p2+4] in valid_nums and (not p2_parsed):
                num2 = valid_nums[line[p2:p2+4]]
                p2_parsed = True
        if p1 <= line_length - 5:
            if line[p1:p1+5] in valid_nums and (not p1_parsed):
                num1 = valid_nums[line[p1:p1+5]]
                p1_parsed = True
        if p2 <= line_length - 5:
            if line[p2:p2+5] in valid_nums and (not p2_parsed):
                num2 = valid_nums[line[p2:p2+5]]
                p2_parsed = True
        if line[p1] in "1234567890" and (not p1_parsed):
            num1 = int(line[p1])
            p1_parsed = True
        if line[p2] in "1234567890" and (not p2_parsed):
            num2 = int(line[p2])
            p2_parsed = True
        p1 += 1
        p2 -= 1
    print("NUM1, NUM2:", num1*10 + num2)
    return num1*10 + num2

def parse_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    running_total = 0
    for i in range(len(lines)):
        line = lines[i]
        # note: added a space to the end of the last line of input.txt
        running_total += part2(line)
    return running_total
