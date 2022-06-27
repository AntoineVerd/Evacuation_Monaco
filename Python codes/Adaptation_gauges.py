import os

cont = 0
timesSaved = []


for file in os.listdir('C:/Users/loren/Desktop/_output/_output/txt'):
    
    
    if file.endswith(".txt"):
        print(file)
        print("---------------------------------")
        finalFile = open("C:/Users/loren/Desktop/_output/_output/txt/finalFiles/" + file, 'a')
        with open("C:/Users/loren/Desktop/_output/_output/txt/" + file, 'r') as oldFileReading:
            for line in oldFileReading:
                print(line)
                if not line.startswith("#"):
                    splitted_line = line.split()
                    time = int(float(splitted_line[1]))
                    if (time % 30 == 0 and time<3600 and (time not in timesSaved)):
                        timesSaved.append(time)
                        q1 = round(float(splitted_line[2]), 2)
                        eta = round(float(splitted_line[5]), 2)
                        final_string = str(round(int(float(splitted_line[1])),2)) + " " + str(eta) + "\n"
                        finalFile.write(final_string)

    finalFile.close