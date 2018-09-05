
import unittest
from register import SignUp
class testRegister(unittest.TestCase):
    def setUp(self):
        self.signup = SignUp()
        self.signup.firstName("fname","Haruna")
        self.signup.lastName("lname","hks")
        self.signup.emailAddress("email","user@email.com")
    
    
    def test_creation(self):
        self.assertIsInstance(self.signup,SignUp)
    
    def test_add_first_name(self):
        self.signup.firstName("fname","dZD")
        self.assertTrue(self.signup.firstName)
        # self.assertEqual(len(signup.firstName),1)
    
    def test_add_last_name(self):
        self.signup.lastName("lname","dexcnkvnzk/nl")
        self.assertTrue(self.signup.lastName)
        # self.assertEqual(len(signup.lastName),1)

    def test_add_email(self):
        self.signup.emailAddress("email","user@email.com")
        self.assertTrue(self.signup.email_address)

    def test_is_string(self):
        self.assertRaises(TypeError,self.signup.firstName)
        self.assertRaises(TypeError,self.signup.lastName)
        self.assertRaises(TypeError,self.signup.emailAddress)

    def test_few_characters(self):
        self.assertTrue(self.signup.firstName)
        self.assertTrue(self.signup.lastName)
        self.assertTrue(self.signup.emailAddress)

    def test_email_validation(self):
        self.assertIn('@', self.signup.email_address["email"])
    
    def test_add_user(self):
        self.signup.add("John@email.com","mypass123")
        # self.assertEqual(len(signup.user_password),1)
    
    def test_missing_key(self):
        with self.assertRaises(KeyError):
            self.signup.getPassword("tuasdds")

if __name__ == '__main__':
    unittest.main()