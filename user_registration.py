"""
@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to check user entered first name and last name is valid

"""


import re
import mylogging

logger=mylogging.logger_init("user_registration.py")

def validate_name(name: str):
    
    """
    Descripton: 
        Checks for the valid name
    
    Parameter: 
        name:The user's name to validate.

    return: 
        object
    """
    
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return re.search(pattern, name)



def main():

    first_name = input("Enter first name (first letter should be upper case): ")
    last_name=input("Enter Last name (first letter should be upper case )")

    if validate_name(first_name) and validate_name(last_name):
        logger.info("First name and Last name is valid")
    else:
        if not validate_name(first_name):
            logger.info("First name is invalid")
        if not validate_name(last_name):
            logger.info("Last name is invalid")    


if __name__ == "__main__":
    main()