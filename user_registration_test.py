"""

@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to validate first name of user

"""

import unittest
from user_registration import validate_firstName

class TestNameValidation(unittest.TestCase):

    def validate_test_case(self):
        
        """
        Description:
            Checks if the name is valid according to the validation rule.

        Parameter:
            self:instance of the class

        Return:
            bool:Returns True for a valid name.
        """
        
        
        self.assertTrue(validate_firstName("Naveen"))
        self.assertTrue(validate_firstName("Girish"))
        self.assertFalse(validate_firstName("Ho"))
        self.assertFalse(validate_firstName("Mi"))

        
if __name__ == "__main__":
    unittest.main()