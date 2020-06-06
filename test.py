import Function
import unittest
class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(Function.Function({'2019-01-10': 10, '2019-01-11': 20, '2019-01-13': 10}),
                         {'2019-01-10': 10, '2019-01-11': 20, '2019-01-12': 15, '2019-01-13': 10}, 'TestCase Failed!!!')

    def test_function_2(self):
        self.assertEqual(Function.Function({'2019-01-01': 100, '2019-01-04': 115}),
                         {'2019-01-01': 100, '2019-01-02': 105, '2019-01-03': 110, '2019-01-04': 115},
                         "TestCase Failed!!!")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)