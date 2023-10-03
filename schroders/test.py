import unittest
from main import Keypad


class TestKeypad(unittest.TestCase):
    def test_output(self):
        self.assertEqual(Keypad().solve(), 1013398)


if __name__ == "__main__":
    unittest.main()
