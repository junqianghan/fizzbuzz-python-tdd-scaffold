from FizzBuzz import transform
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_nomal(self):
        self.assertEqual(transform(2),'2')
    def test_times_3(self):
        self.assertEqual(transform(3),'Fizz')

    def test_times_5(self):
        self.assertEqual(transform(5),'Buzz')

    def test_times_3_5(self):
        self.assertEqual(transform(15),'FizzBuzz')



if __name__ == '__main__':
    unittest.main()