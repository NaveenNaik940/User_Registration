"""

@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to validate first, last name, email and mobile number of user by unit testing

"""

import unittest
from user_registration import (validate_name,validate_email,validate_mobile_number)

class TestNameValidation(unittest.TestCase):

    def test_case(self):
        
        """
        Description:
            Checks if the first,last name,email and mobile number is valid according to the validation rule.

        Parameter:
            self:instance of the class

        Return:
            bool
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

        #Test case validation for email
        self.assertTrue(validate_email("abc.xyz@bl.co.in"))
        self.assertTrue(validate_email("naveen@domain.co"))
        self.assertFalse(validate_email("naveen@blco"))
        self.assertFalse(validate_email("naveec@bl.co.in."))

        
if __name__ == "__main__":
    unittest.main()
