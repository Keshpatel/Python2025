import csv
#-------------------------- CSV file seperated by comma (,)----------------
def addRecord():
   file1 = open('Project.csv','w',newline = '')
   s = csv.writer(file1,delimiter = ',')
   col_heading = ['NAME','MANAGER','LEAD','DEVELOPER1','TESTER1']
   s.writerow(col_heading)
   while True :
      p = input('\nEnter ProjectName: ')
      m = input('Enter Manager name: ')
      l = input('Enter Lead: ')
      D1 = input('Enter Developer : ')
      T1 = input('Enter Tester: ')

      row = [p,m,l,D1,T1]
      s.writerow(row)
      choice = input("\n Press 'n' OR 'N' to stop Entry")
      if choice in ['n','N']:
         break

   file1.close()

#Function calling 
addRecord() 
#----------------Read from Project Team File;(with do not req. to close file )------------------
def viewRecord():
    with open('Project.csv','r') as Project:
        data = csv.reader(Project,delimiter =',')

        for row in data:
            print(row)
     
        
# Function Calling 
# 
viewRecord()
 
