inputFile = open("IDandName.txt", "r")
# print(inputFile.read())
for line in inputFile:
     line_split = line.split()
     if line_split[1] == 'Daniel':
          print(line)
          
inputFile.close()
