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

    num_of_added = 3
    count = 0

    for i in range(0,len(file_content)-3):
        if sum(file_content[i:i+num_of_added]) > sum(file_content[i+1:i+num_of_added+1]):
            count += 1
    return count

inputfile = "Day01.txt"

print(part1(inputfile))
print(part2(inputfile))