"""
@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to check user entered first, last name and email is valid

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


def validate_email(email: str) :

    """
    Description:
        Validates the email format according to given rule

    Parameter:
        email (str): The email to validate.

    Return:
        object
    """

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'
    return re.search(pattern, email)



def main():

    first_name = input("Enter first name (first letter should be upper case): ")
    last_name=input("Enter Last name (first letter should be upper case )")
    email=input("Enter email id:(eg:abc@gmail.com) ")

    if validate_name(first_name) and validate_name(last_name) and validate_email(email):
        logger.info("First name ,Last name and Email is valid")
    else:
        if not validate_name(first_name):
            logger.info("First name is invalid")
        if not validate_name(last_name):
            logger.info("Last name is invalid")  
        if not validate_email(email):  
            logger.info("Email is invalid")    


if __name__ == "__main__":
    main()