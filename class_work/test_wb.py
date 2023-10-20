from unittest import TestCase, main
from wb import FizzBuzz

class TestFizzBuzz(TestCase):

  def test_div_by_15(self):
    result_1 = FizzBuzz(15)
    self.assertEqual(result_1, 'FizzBuzz')
    result_2 = FizzBuzz(30)
    self.assertEqual(result_2, 'FizzBuzz')
    self.assertEqual(FizzBuzz(60), 'FizzBuzz')

  def test_div_by_3(self):
    
    pass

  def test_div_by_5(self):
    self.assertEqual(FizzBuzz(25), 'Buzz')
    self.assertEqual(FizzBuzz(5), 'Buzz')
    pass

  def test_negative(self):
    pass


if __name__ == '__main__':
  main()
  










