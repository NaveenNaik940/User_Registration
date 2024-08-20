"""

@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to validate first, last name, email,mobile number and password of user by unit testing

"""

import unittest
from user_registration import (validate_name,validate_email,validate_mobile_number,validate_password)

class TestNameValidation(unittest.TestCase):

    def test_first_last_name(self):
        
        """
        Description:
            Checks if the first and last name is valid according to the validation rule.

        Parameter:
            self:instance of the class

        Return:
            None
        """
        
        #Test case validation for first name
        self.assertTrue(validate_name("Naveen"))
        self.assertTrue(validate_name("Girish"))
        self.assertFalse(validate_name("auhsh"))
        self.assertFalse(validate_name("sja"))

        #Test case validation for last name
        self.assertTrue(validate_name("Naik"))
        self.assertTrue(validate_name("Nekar"))
        self.assertFalse(validate_name("hjdj"))
        self.assertFalse(validate_name("isdh"))


    def test_email(self): 
        
        """
        Description:
            Checks if email is valid according to the validation rule.

        Parameter:
            self:instance of the class

        Return:
            None
        """
        #Test case validation for email
        self.assertTrue(validate_email("abc.xyz@bl.co.in"))
        self.assertTrue(validate_email("naveen@domain.co"))
        self.assertFalse(validate_email("naveen@blco"))
        self.assertFalse(validate_email("naveec@bl.co.in."))


    def test_password(self):

        """
        Description:
            Checks if password is valid according to the validation rule.

        Parameter:
            self:instance of the class

        Return:
            None
        """        
        #Test case validation for Password
        self.assertTrue(validate_password("Naveen9087"))
        self.assertTrue(validate_password("Nvaendhkl"))
        self.assertFalse(validate_password("87"))
        self.assertFalse(validate_password("aend"))
        

        
if __name__ == "__main__":
    unittest.main()
