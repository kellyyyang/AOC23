nums = {} # (start_x, start_y) : number (as a string)

def part1(lines):
    prev_is_num = True
    prev_num_start_ind = (0,0)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in '1234567890' and prev_is_num:
                if prev_num_start_ind not in nums:
                    nums[prev_num_start_ind] = lines[i][j]
                else:
                    nums[prev_num_start_ind] += lines[i][j]
            elif lines[i][j] in '1234567890' and not prev_is_num:
                prev_num_start_ind = (i, j)
                nums[prev_num_start_ind] = lines[i][j]
                prev_is_num = True
            elif lines[i][j] not in '1234567890':
                prev_is_num = False
    directions = [(0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1), (1, 0), (-1, 0)]
    part_nums = []
    added = False
    for start_ind in nums:
        start_x, start_y = start_ind
        num_length = len(nums[start_ind])
        for idx in range(start_y, start_y+num_length):
            for x, y in directions:
                new_x, new_y = start_x + x, idx + y
                if 0 <= new_x < len(lines) and 0 <= new_y < len(lines[0]):
                    if lines[new_x][new_y] not in '1234567890' and lines[new_x][new_y] != '.' and lines[new_x][new_y] != '\n':
                        part_nums.append(int(nums[start_ind]))
                        added = True
                        break
            if added:
                added = False
                break
    return sum(part_nums)

def part2(lines):
    directions = [(0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1), (1, 0), (-1, 0)]
    potential_gears = {}
    added = False
    for start_ind in nums:
        start_x, start_y = start_ind
        num_length = len(nums[start_ind])
        for idx in range(start_y, start_y+num_length):
            for x, y in directions:
                new_x, new_y = start_x + x, idx + y
                if 0 <= new_x < len(lines) and 0 <= new_y < len(lines[0]):
                    if lines[new_x][new_y] not in '1234567890' and lines[new_x][new_y] == '*' and lines[new_x][new_y] != '\n':
                        if (new_x, new_y) not in potential_gears:
                            potential_gears[(new_x, new_y)] = [int(nums[start_ind])]
                        else:
                            potential_gears[(new_x, new_y)].append(int(nums[start_ind]))
                        added = True
                        break
            if added:
                added = False
                break
    result = 0
    for gear in potential_gears:
        if len(potential_gears[gear]) == 2:
            result += potential_gears[gear][0] * potential_gears[gear][1]
    return result


def parse_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    part1(lines)
    # print(nums)
    return part2(lines)
    