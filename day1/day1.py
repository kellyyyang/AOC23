def part1(line):
    line_length = len(line) - 1
    p1, p2 = 0, line_length - 1
    num1, num2 = '', ''
    p1_parsed = False
    p2_parsed = False
    # print(line_length)
    while (not p1_parsed) or (not p2_parsed):
        # print("p1, p2", line[p1], line[p2])
        if line[p1] in "1234567890" and (not p1_parsed):
            # print("NUM1:", line[p1])
            num1 = line[p1]
            p1_parsed = True
        if line[p2] in "1234567890" and (not p2_parsed):
            # print("NUM2:", line[p2])
            num2 = line[p2]
            p2_parsed = True
        p1 += 1
        p2 -= 1
    print("NUM1, NUM2", num1 + num2)
    return int(num1 + num2)


def parse_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    running_total = 0
    for i in range(len(lines)):
        line = lines[i]
        if i == len(lines) - 1:
            line += ''
        running_total += part1(line)
    return running_total
