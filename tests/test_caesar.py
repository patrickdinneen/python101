import unittest
from cipher import caesar


class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(caesar.encrypt('the quick brown fox jumps over the lazy dog.', 23),
                         'qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.')

    def test_get_offset_character(self):
        self.assertEqual(caesar.get_offset_character('a', 1), 'b')
        self.assertEqual(caesar.get_offset_character('a', 2), 'c')
        self.assertEqual(caesar.get_offset_character('z', 1), 'a')
        self.assertEqual(caesar.get_offset_character('z', 2), 'b')


if __name__ == '__main__':
    unittest.main()
