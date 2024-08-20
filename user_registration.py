"""
@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to check user entered first, last name,email,mobile number and password is valid

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

    pattern = r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'


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


def validate_password(password: str):

    """
    Description:
        Validates the password according to the given rule.

    Parameter:
        password(str): The password to validate.

    Return:
        bool
    """

    #Rule
    #1.Password must have 8 character
    #2.Password must have 1 uppercase letter
    #3.Password must have 1 numerical
    #4.Password must contain exactly one special character

    pattern=r'(?=.*[A-Z])(?=.*[0-9]).{8,}'

    if not re.search(pattern,password):
        return False
    
    special_char_count = re.findall(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~]',password)
    if not len(special_char_count)==1:
        return False
    
    return True


def main():
    try:
        attempt=0
        print("Hi user. You have 4 attempt to register correctly....\n")
        while attempt<4:

            if attempt==0:
                first_name = input("Enter first name (first letter should be upper case): \n")
                last_name=input("Enter Last name (first letter should be upper case ):\n")
                email=input("Enter email id:(eg:abc@gmail.com): \n")
                mobile_number=input("Enter mobile number(eg:91 8537865438): \n")
                password=input("Enter atleast 8 character password with one uppercase letter,one numerical number and exactly one special character: \n")

            else:
                if not validate_name(first_name):
                    first_name = input("\nEnter first name (first letter should be upper case): ")
                if not validate_name(last_name):
                    last_name = input("\nEnter Last name (first letter should be upper case )") 
                if not validate_email(email):
                    email = input("\nEnter email id:(eg:abc@gmail.com) ")
                if not validate_mobile_number(mobile_number):
                    mobile_number = input("\nEnter mobile number(eg:91 8537865438) ")    
                if not validate_password(password):
                    password=input("\nEnter atleast 8 character password with one uppercase letter,one numerical number and exactly one special character: ")  


            if (validate_name(first_name) and validate_name(last_name) and 
                   validate_email(email) and validate_mobile_number(mobile_number) and validate_password(password)):

                   logger.info(f"\nHi {first_name} {last_name} your Registration Successfull.....Enjoy")
                   break
                
            else:
                if not validate_name(first_name):
                    logger.info("\nFirst name is invalid")
                if not validate_name(last_name):
                    logger.info("\nLast name is invalid")  
                if not validate_email(email):  
                    logger.info("\nEmail is invalid")  
                if not validate_mobile_number(mobile_number):
                    logger.info("\nMobile number is invalid")   
                if not validate_password(password):
                    logger.info("\nPassword is incorrect")  
                attempt+=1
                print(f"\nyou used {attempt} attempt out of 4")   

        if attempt==4:
            print(f"\nYou used all the attempt....")  
            print("try to run it again.....")                 


    except ValueError as ve:
        print("ve")  

    except Exception as e:
        print("e")  

if __name__ == "__main__":
    main()