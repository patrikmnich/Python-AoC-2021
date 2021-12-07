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

    bitlength = len(file_content[0])

    done = False
    o2_done = False
    co2_done = False

    while not done:
        for i in range(bitlength):
            
            if not o2_done:
                ones = 0
                zeros = 0
                for line in oxygen:
                    if line[i] == "0":
                        zeros += 1
                    else:
                        ones += 1
        
                most_common = "1" if ones >= zeros else "0"
    
            
                for line in oxygen[:]:
                    if line[i] == most_common:
                        oxygen.remove(line)
                    if len(oxygen) == 1:
                        o2_done = True

            if not co2_done:

                ones = 0
                zeros = 0

                for line in co2:
                    if line[i] == "0":
                        zeros += 1
                    else:
                        ones += 1
        
                least_common = "0" if zeros <= ones else "1"
        
                for line in co2[:]:
                    if line[i] == least_common:
                        co2.remove(line)
                    if len(co2) == 1:
                        co2_done = True
        
        if co2_done and o2_done:
            done = True
    
    print(oxygen,co2)
    
    return int(oxygen[0],2)*int(co2[0],2)
    
inputfile = "Day03.txt"

print(part1(inputfile))
print(part2(inputfile))