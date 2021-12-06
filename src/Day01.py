def part1(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()
        #print(file_content)

    count = 0

    for i in range(0,len(file_content)-1):
        if int(file_content[i+1]) > int(file_content[i]):
            count += 1

    return count



def part2(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()

    slice_count = 3
    count = 0

    for i in range(0,len(file_content)-3):
        if sum([int(x) for x in file_content[i:i+slice_count]]) < sum([int(x) for x in file_content[i+1:i+slice_count+1]]):
            count += 1

    return count

inputfile = "Day01.txt"

print(part1(inputfile))
print(part2(inputfile))