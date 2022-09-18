import unittest
import translator

class TestCases(unittest.TestCase):
    def test_e2f_null(self):
        self.assertIsNone(translator.english_to_french(None))

    def test_f2e_null(self):
        self.assertIsNone(translator.french_to_english(None))

    def test_hello_to_bonjour(self):
        self.assertEqual(translator.english_to_french("Hello"),'Bonjour')
        
    def test_bojour_to_hello(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")



if __name__=='__main__':
    unittest.main()

