nums = {} # (start_x, start_y) : number (as a string)

def part1(lines):
    # nums = [] # in the form [((start_x, start_y), (end_x, end_y)), ((start_x, start_y), (end_x, end_y)),...]
    prev_is_num = True
    prev_num_start_ind = (0,0)
    for i in range(len(lines)):
        # print(lines[i])
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
            # print(start_x, idx, added)
            # if start_x == 4 and idx == 2:
                # print("HERE")
            for x, y in directions:
                new_x, new_y = start_x + x, idx + y
                if 0 <= new_x < len(lines) and 0 <= new_y < len(lines[0]):
                    if lines[new_x][new_y] not in '1234567890' and lines[new_x][new_y] != '.' and lines[new_x][new_y] != '\n':
                        part_nums.append(int(nums[start_ind]))
                        # print("ADDED = TRUE:", new_x, new_y)
                        added = True
                        break
            if added:
                added = False
                break
    # print(part_nums)
    return sum(part_nums)


def parse_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return part1(lines)
    