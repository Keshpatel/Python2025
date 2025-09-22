#Using try-except Blocks:
def try_exceptExample():
 try:
    fullNum = int(input("Enter a Number: "))
    result = 10/ fullNum 
    print("The result is :", result)
 except ValueError:
    print("You must enter a valid integer")
 except ZeroDivisionError:
    print("You can not divide by zero")  

def assert_Example():
   years = [2003, 2006, 2004, 2012, 2014, 2020, 2008, 2007, 2022]
   # years.reverse()  #->  This will give an error...(In order to verify: First element is greater then last element) use sort()
   years.sort()
   print(years)
   assert years[4] <= years[-1], "First element is greater then last element ."
       
  

#try_exceptExample()
assert_Example()
