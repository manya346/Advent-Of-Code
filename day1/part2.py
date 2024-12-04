def part2(input_file):
    input = open(input_file, "r").readlines()
    left = sorted(int(num.split()[0]) for num in input)
    right = sorted(int(num.split()[1]) for num in input)
    prod = 0
    for index in left:
        if index in right:
            prod = prod + index*right.count(index)
    return prod

input_file = r"c:\Users\DELL\Pictures\Camera imports\College Stuff\Advent Of Code\day1\input.txt"
print(part2(input_file))