#discover automation of input vlaidation
# Understand its role as shield 
#run on > terminal pip install pyinputplus : config correct interpreter 
import pyinputplus as pyip

def integerInputValidation():
    result = pyip.inputInt("enter Number of shopping bags you will need for your items: ", min=0)
    print("\n You will use ", result, "store bags.")    

def menuInputValidation():
    result = pyip.inputMenu(["red", "blue", "green"], lettered = True , numbered = False)
    print("\n you have selected :", result , "marker.")

def inputEmailValidation():
    result = pyip.inputEmail("enter your Email ")
    print("\nyou have Entered", result)

#------------------Date validation using pyip.inputdate()------------------------
def inputDateValidation1():
# Prompt for a date, but only accept 'MM/DD/YYYY' by default formate only  
    date_input = pyip.inputDate("Please enter MM/DD/YYYY formate ")
    print(f"You entered: {date_input} is valid Date ")

    date_input = pyip.inputDate("Enter a date: in 'YYYY-MM-DD' or 'MM/DD/YY' formats only ", formats=['%Y-%m-%d', '%m/%d/%Y']) 
    print(f"You entered: {date_input} is valid Date ")

def inputDateValidation2():
# Prompt the user for a date until they enter a valid one  YYYY-MM-DD fromat 
    date_input = pyip.inputDate("Enter a date in dd-mm-yy formate only ", formats=['%d-%m-%y', '%Y-%m-%d'])
    print("You entered: {date_input} is valid date")
    # date_input = pyip.inputDate("Enter a date in mm/dd/yy formate only ", formats=['%m/%d/%y'])
    # print(f"You entered: {date_input} is valid date")
    
integerInputValidation()
menuInputValidation()
inputEmailValidation()
inputDateValidation1()
inputDateValidation2()







