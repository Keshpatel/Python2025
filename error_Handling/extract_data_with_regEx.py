import re
from re import *

phoneNumRegEx = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "contact number is:  403-744-0129."

result = phoneNumRegEx.search(example)

if result:
    print("Phone number  found : ", result.group())
    print("Area code ", result.group()[0:3])


pattern = compile( '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)' ) 
         
#( '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)' )
                

def get_emailAddress():
    address = input("Enter your email address:" )
    is_valid = pattern.match(address)

    if is_valid:
        print("Valid Email Address ", is_valid.group())
    else:
        print('Invalid Email Address ! Please Retry ....\n')
        get_emailAddress()

#Calling get_emialaddress
get_emailAddress()            


