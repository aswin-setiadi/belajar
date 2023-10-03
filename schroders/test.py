import unittest
from main import Keypad


class TestKeypad(unittest.TestCase):
    def test_sample_input(self):
        matrix: list[list[str | None]] = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
            [None, "1", "2", "3", None],
        ]
        self.assertEqual(
            Keypad(matrix=matrix, max_depth=10, max_vowel=2).solve(), 1013398
        )


if __name__ == "__main__":
    unittest.main()
