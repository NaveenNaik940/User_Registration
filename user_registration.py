"""
@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to check user entered first, last name, email and  is valid

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


def validate_mobile_number(mobile_number: str):

    """
    Description:
        Validates the mobile number format according to the given rule.

    Parameter:
        mobile_number (str): The mobile number to validate.

    Return:
        object
    """

    pattern = r'^\d{2} \d{10}$'
    return re.search(pattern, mobile_number)


def main():

    first_name = input("Enter first name (first letter should be upper case): ")
    last_name=input("Enter Last name (first letter should be upper case )")
    email=input("Enter email id:(eg:abc@gmail.com) ")
    mobile_number=input("Enter mobile number(eg:91 8537865438) ")

    if validate_name(first_name) and validate_name(last_name) and validate_email(email) and validate_mobile_number(mobile_number):
        logger.info("First Name ,Last Name, Email and Mobile Number is valid")
    else:
        if not validate_name(first_name):
            logger.info("First name is invalid")
        if not validate_name(last_name):
            logger.info("Last name is invalid")  
        if not validate_email(email):  
            logger.info("Email is invalid")  
        if not validate_mobile_number(mobile_number):
            logger.info("Mobile number is invalid")      


if __name__ == "__main__":
    main()