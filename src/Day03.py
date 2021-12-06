def part1(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()
        file_content = [line.strip() for line in file_content]
    
    zeros = [0 for i in file_content[0]]
    ones = [0 for i in file_content[0]]

    gamma_rate = ""
    epsilon_rate = ""

    for line in file_content:
        for i in range(0,len(line)):
            if line[i] == "0":
                zeros[i] += 1
            else:
                ones[i] += 1
    
    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate,2)*int(epsilon_rate,2)


def part2(inputfile):
    with open(inputfile) as f:
        file_content = f.readlines()
        file_content = [line.strip() for line in file_content]

    

    oxygen = file_content[:]
    co2 = file_content[:]

    while(len(oxygen) > 1):
        zeros = [0 for i in file_content[0]]
        ones = [0 for i in file_content[0]]
        for line in oxygen:
            for i in range(0,len(line)):
                if line[i] == "0":
                    zeros[i] += 1
                else:
                    ones[i] += 1

        for i in range(len(zeros)):
            most_common = "1" if ones[i] > zeros[i] else "0"
    
            for line in oxygen:
                if line[i] != most_common:
                    oxygen.remove(line)
    
    while(len(co2) > 1):
        zeros = [0 for i in file_content[0]]
        ones = [0 for i in file_content[0]]
        for line in co2:
            for i in range(0,len(line)):
                if line[i] == "0":
                    zeros[i] += 1
                else:
                    ones[i] += 1

        for i in range(len(zeros)):
            least_common = "1" if ones[i] <= zeros[i] else "0"
            for line in co2:
                if line[i] == most_common:
                    co2.remove(line)

    print(oxygen,co2)
    
    return int(oxygen[0],2)*int(co2[0],2)
    
inputfile = "Day03.txt"

print(part1(inputfile))
print(part2(inputfile))