import unittest
from main import Solution, Builder
from global_vars import VALID_PIECES
from custom_exceptions import (
    DuplicateKeyException,
    InvalidKeyPadLayoutException,
    InvalidMaxDepthException,
    InvalidMaxVowelException,
)


class TestKeypad(unittest.TestCase):
    def test_sample_input(self):
        matrix: list[list[str | None]] = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
            [None, "1", "2", "3", None],
        ]
        self.assertEqual(
            Solution.solve(
                matrix=matrix, max_depth=10, max_vowel=2, move_type=VALID_PIECES[0]
            ),
            1_013_398,
        )

    def test_valid_matrix_knight(self):
        matrix1 = [["A", "B", "C"], ["D", "E", "F"]]
        matrix2 = [["A", "B", None], ["D", "E", "F"]]
        matrix3 = [[None, "B", None], ["D", "E", "F"]]
        self.assertEqual(
            Solution.solve(
                matrix=matrix1, max_depth=3, max_vowel=3, move_type=VALID_PIECES[0]
            ),
            4,
        )
        self.assertEqual(
            Solution.solve(
                matrix=matrix2, max_depth=3, max_vowel=3, move_type=VALID_PIECES[0]
            ),
            2,
        )
        self.assertEqual(
            Solution.solve(
                matrix=matrix3, max_depth=3, max_vowel=3, move_type=VALID_PIECES[0]
            ),
            0,
        )

    def test_invalid_matrix_knight(self):
        matrixes = []
        matrixes.append([[]])
        matrixes.append([["A"], ["B"]])
        matrixes.append([["A", "B"], ["C", "D"]])
        matrixes.append([["A", "B"], ["C", "D", "E"]])
        matrixes.append([["A", "B", "C"], ["D", "E", "F"], ["G", None]])
        for matrix in matrixes:
            with self.assertRaises(InvalidKeyPadLayoutException):
                Solution.solve(
                    matrix=matrix, max_depth=10, max_vowel=2, move_type=VALID_PIECES[0]
                )

    def test_duplicate_keys(self):
        matrix = [["A", "B", "C"], ["A", "E", "F"]]
        with self.assertRaises(DuplicateKeyException):
            Solution.solve(
                matrix=matrix, max_depth=10, max_vowel=2, move_type=VALID_PIECES[0]
            )

    def test_invalid_max_depth(self):
        matrix = [["A", "B", "C"], ["D", "E", "F"]]
        with self.assertRaises(InvalidMaxDepthException):
            Solution.solve(
                matrix=matrix, max_depth=-1, max_vowel=2, move_type=VALID_PIECES[0]
            )

    def test_invalid_max_vowel(self):
        matrix = [["A", "B", "C"], ["D", "E", "F"]]
        with self.assertRaises(InvalidMaxVowelException):
            Solution.solve(
                matrix=matrix, max_depth=10, max_vowel=-1, move_type=VALID_PIECES[0]
            )

    def test_rook_move(self):
        matrix = [["A", "B"], ["D", "E"], [None, None]]
        out_adj = Builder.build_adjacency_dict(matrix, "rook")
        exp_adj = {"A": ["B", "D"], "B": ["A", "E"], "D": ["E", "A"], "E": ["D", "B"]}
        self.assertEqual(out_adj, exp_adj)


if __name__ == "__main__":
    unittest.main()
