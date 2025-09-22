#discover automation of input vlaidation
# Understand its role as shield 
#run on > terminal pip install pyinputplus : config correct interpreter 
import pyinputplus as pyip
from datetime import datetime

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
def inputDateValidation():
# Prompt for a date, but only accept 'MM/DD/YYYY' by default formate only  
    date_input = pyip.inputDate("Please enter MM/DD/YYYY formate ")
    print(f"You entered: {date_input} is valid Date ")

    date_input = pyip.inputDate("Enter a date: in 'YYYY-MM-DD' or 'MM/DD/YYYY' formats only ", formats=['%Y-%m-%d', '%m/%d/%Y']) 
    print(f"You entered: {date_input} is valid Date ")
    date_input = pyip.inputDate("Enter a date in dd-mm-YYYY Or YYYY-mm-dd format only ", formats=['%d-%m-%Y', '%Y-%m-%d'])
    print("You entered: {date_input} is valid date")

def inputDayValidation():
    while True:
        date_str = input("Enter a date (YYYY-MM-DD): ")
        try:
            # Parse the input string into a datetime object
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            
            # Get the full name of the day
            day_name = date_obj.strftime("%A")
            print(f"The day of the week for {date_str} is: {day_name}")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")



integerInputValidation()
menuInputValidation()
inputEmailValidation()
inputDateValidation()
inputDayValidation()







