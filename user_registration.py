"""
@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to check user entered first name is valid

"""


import re
import mylogging

logger=mylogging.logger_init("user_registration.py")

def validate_firstName(first_name: str):
    
    """
    Descripton: 
        Checks for the valid name
    
    Parameter: 
        first_name:The user's name to validate.

    return: 
        object
    """
    
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return re.search(pattern, first_name)



def main():

    first_name = input("Enter first name first letter should be upper case: ")

    if validate_firstName(first_name):
        logger.info("First name is valid")
    else:
        logger.info("First name is invalid")


if __name__ == "__main__":
    main()