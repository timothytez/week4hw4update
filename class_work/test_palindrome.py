from unittest import TestCase, main
from check_palindrome import check_palindrome

class TestCheckPalindrome(TestCase):

  def test_palindrome(self):
    self.assertTrue(check_palindrome('racecar'))
    self.assertTrue(check_palindrome('yobananaboy'))
    self.assertTrue(check_palindrome('poop'))
    self.assertTrue(check_palindrome('madamimadam'))
    self.assertTrue(check_palindrome('tacocat'))

  def test_non_palindrome(self):
    result_1 = check_palindrome('matrix')
    self.assertFalse(result_1)
    self.assertFalse(check_palindrome('helloworld'))
    self.assertEqual(check_palindrome('sean'),False)

  def test_casing(self):
    self.assertTrue(check_palindrome('Tacocat'))
    self.assertTrue(check_palindrome('TacoCat'))
    self.assertTrue(check_palindrome('TACocat'))

  def test_uneven_amount_letters(self):
    self.assertTrue(check_palindrome('tacocat'))
    self.assertFalse(check_palindrome('boo'))

if __name__ == '__main__':
  main()