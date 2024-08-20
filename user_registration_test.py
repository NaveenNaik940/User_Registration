"""

@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to validate first name and last name of user

"""

import unittest
from user_registration import validate_name

class TestNameValidation(unittest.TestCase):

    def validate_test_case(self):
        
        """
        Description:
            Checks if the first and last name is valid according to the validation rule.

        Parameter:
            self:instance of the class

        Return:
            bool:Returns True for a valid name.
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

        
if __name__ == "__main__":
    unittest.main()