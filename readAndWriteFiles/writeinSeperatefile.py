import csv
#--------------------------from one txt file to writing in two different txt file ------------------------------
#txt file text seperated using space 
inputFile = open("IDAndName.txt", "r")
selectedstudent = open("selectedstudent.txt","w")
nonSelected = open("nonselected.txt","w")
for line in inputFile: 
    line_split = line.split()   
    if line_split[2] == "Williams":
       selectedstudent.write(line)
    else:        
       nonSelected.write(line)
inputFile.close()

#--------------------------from one CSV file to writing in two different CSV file ------------------------------
#txt file CSV seperated by (,) 
file1 = open('Student.csv', 'r', newline='')
file2 = open('selected.csv','w', newline='')
file3 = open('nonselected.csv', 'w', newline='')
data = csv.reader(file1)
for s in data:
 if s[1] == "Calgary": 
    print(s[0],s[1],s[2],s[3])   
    s1 = csv.writer(file2) 
    s1.writerow(s)
 else:
    s2 = csv.writer(file3)
    s2.writerow(s)
#and s[3] == "Registered":
file1.close()
file2.close()
file3.close()       
