def part1(inputfile):
    with open(inputfile) as f:

        file_content = f.readlines()
        file_content = [line.replace(" ","").strip().split('->') for line in file_content]
        print(file_content)


def part2(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()


inputfile = "Day05.txt"

print(part1(inputfile))
print(part2(inputfile))