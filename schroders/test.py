import unittest
from assign import KeyPad


class TestKeyPad(unittest.TestCase):
    def test_output(self):
        self.assertEqual(KeyPad().solve(), 1013398, "test msg")


if __name__ == "__main__":
    unittest.main()
