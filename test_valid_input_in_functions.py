import unittest
import unittest.mock as mock
import sys
import validate_input_in_functions

class test_score_input_test_score_valid(unittest.TestCase):

        def test_score_input_test_score_valid(self):
            self.assertEqual(('ian', 5), validate_input_in_functions.multiply_string('ian', 5, 'invalid'))
        def test_score_input_test_score_below_range(self):
            self.assertEqual(('ian', 'invalid'), validate_input_in_functions.multiply_string('ian', -5, 'invalid'))
        def test_score_input_test_score_above_range(self):
            self.assertEqual(('ian', 'invalid'), validate_input_in_functions.multiply_string('ian', 200, 'invalid'))
        def test_test_score_non_numeric(self):
            self.assertEqual(('ian', 'invalid'), validate_input_in_functions.multiply_string('ian', '200', 'invalid'))



if __name__ == '__main__':
    unittest.main()
