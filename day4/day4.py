def part1(lines):
    card_nums = dict(zip([i+1 for i in range(len(lines))], [[] for _ in range(len(lines))]))
    for i in range(len(lines)):
        line = lines[i]
        if line[-1] == '\n': line = line[:-1]
        divided = line.split("|")
        divided[0] = divided[0].split(':')[-1]
        for s in range(len(divided)):
            div = divided[s]
            nums = div.split(" ")
            new_nums = []
            for n in nums:
                if n != '':
                    new_nums.append(int(n))
            if s == 0:
                card_nums[i+1].append(set(new_nums))
            else:
                card_nums[i+1].append(new_nums)

    matches = [0 for _ in range(len(lines))]
    for card in card_nums:
        for num in card_nums[card][-1]:
            if num in card_nums[card][0]:
                matches[card-1] += 1

    cardinalities = [0 for _ in range(len(lines))]
    part1_result = 0
    for m in range(len(matches)):
        num_matches = matches[m]
        cardinalities[m] += 1
        if num_matches > 0:
            for nm in range(1, num_matches+1):
                cardinalities[m+nm] += cardinalities[m]
            part1_result += 2**(num_matches-1)

    print("PART 1: {}".format(part1_result))
    print("PART 2: {}".format(sum(cardinalities)))


def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return part1(lines)