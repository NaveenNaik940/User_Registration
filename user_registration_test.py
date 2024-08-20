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
        self.assertTrue(validate_email("abc@yahoo.com"))
        self.assertTrue(validate_email("abc-100@yahoo.com"))
        self.assertTrue(validate_email("abc.100@yahoo.com"))
        self.assertTrue(validate_email("abc111@abc.com"))
        self.assertTrue(validate_email("abc111@abc.net"))
        self.assertTrue(validate_email("abc.100@abc.com.au"))
        self.assertTrue(validate_email("abc@1.com"))
        self.assertTrue(validate_email("abc@gmail.com.com"))
        self.assertTrue(validate_email("abc+100@gmail.com"))

        self.assertFalse(validate_email("abc"))
        self.assertFalse(validate_email("abc@.com.my"))
        self.assertFalse(validate_email("abc123@gmail.a"))
        self.assertFalse(validate_email("abc123@.com"))
        self.assertFalse(validate_email("abc123@.com.com"))
        self.assertFalse(validate_email(".abc@abc.com"))
        self.assertFalse(validate_email("abc()*@gmail.com"))
        self.assertFalse(validate_email("abc@%*.com"))
        self.assertFalse(validate_email("abc..2002@gmail.com"))
        self.assertFalse(validate_email("abc.@gmail.com"))
        self.assertFalse(validate_email("abc@abc@gmail.com"))
        self.assertFalse(validate_email("abc@gmail.com.1a"))
        self.assertFalse(validate_email("abc@gmail.com.aa.au"))


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
        self.assertTrue(validate_password("sjksAndj1%"))
        self.assertTrue(validate_password("Nahduiisk1["))
        self.assertFalse(validate_password("87djdskA"))
        self.assertFalse(validate_password("askkendA]%"))
        

        
if __name__ == "__main__":
    unittest.main()
