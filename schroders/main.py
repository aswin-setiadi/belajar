import logging
import os
import sys
import time
from typing import Optional

from custom_exceptions import InvalidKeyPadLayoutException

DEBUGGING = os.getenv("DEBUGGING")
if DEBUGGING == "1":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logger = logging.getLogger(__name__)

class Keypad:
    def __init__(
        self,
        matrix: list[list[str | None]],
        max_depth: int,
        max_vowel: int,
    ) -> None:
        """
        Subpath_count will keep track of all the traversed valid 10 key combination given conditions:
        - current vowel count
        - current char (vowel or not)
        - depth
        """
        if len(matrix) <= 1:
            raise InvalidKeyPadLayoutException
        dim = len(matrix) * len(matrix[0])
        if dim < 6:
            raise InvalidKeyPadLayoutException
        self.matrix = self._build_adjacency_list(matrix)
        self.vowels = {"A": None, "E": None, "I": None, "O": None, "U": None}
        self.max_vowels = max_vowel
        self.subpath_accumulator: dict[str, int] = {}
        self.max_depth = max_depth
        self.max_depth_tracker = self.max_depth - 1

        self.combi_count: int = 0

    def solve(self):
        t1 = time.time()
        for key in self.matrix.keys():
            if key in self.vowels:
                self.combi_count += self._traverse(key, 0, 1)
            else:
                self.combi_count += self._traverse(key, 0, 0)
        t2 = time.time()
        logger.debug(t2 - t1)
        logger.debug(len(self.subpath_accumulator))
        logger.info(self.combi_count)
        return self.combi_count

    def _traverse(self, node: str, depth: int, vowel_count: int) -> int:
        depth += 1
        if depth == self.max_depth:
            return 1
        else:
            k = f"{vowel_count}{node}{depth}"
            if k in self.subpath_accumulator:
                return self.subpath_accumulator[k]
            else:
                subpath_count: int = 0
                for knight_path in self.matrix[node]:
                    if knight_path in self.vowels:
                        if vowel_count < self.max_vowels:
                            subpath_count += self._traverse(
                                knight_path, depth, vowel_count + 1
                            )

                    else:
                        subpath_count += self._traverse(knight_path, depth, vowel_count)
                if 2 <= depth and depth <= self.max_depth_tracker:
                    self.subpath_accumulator[k] = subpath_count
            return subpath_count

    @staticmethod
    def _build_adjacency_list(
        m: list[list[str | None]],
    ) -> dict[str, list[str]]:
        adj_dict: dict[str, list[Optional[str]]] = {}
        max_row_index = len(m)
        max_col_index = len(m[0])
        for row in range(len(m)):
            for col in range(len(m[row])):
                key = m[row][col]
                if key != None:
                    adj_dict[key] = []
                    if row >= 2:
                        if col >= 1:
                            Keypad._append_target(adj_dict[key], m[row - 2][col - 1])
                        if col < max_col_index - 1:
                            Keypad._append_target(adj_dict[key], m[row - 2][col + 1])
                    if row >= 1:
                        if col >= 2:
                            Keypad._append_target(adj_dict[key], m[row - 1][col - 2])
                        if col < max_col_index - 2:
                            Keypad._append_target(adj_dict[key], m[row - 1][col + 2])
                    if row < max_row_index - 2:
                        if col >= 1:
                            Keypad._append_target(adj_dict[key], m[row + 2][col - 1])
                        if col < max_col_index - 1:
                            Keypad._append_target(adj_dict[key], m[row + 2][col + 1])
                    if row < max_row_index - 1:
                        if col >= 2:
                            Keypad._append_target(adj_dict[key], m[row + 1][col - 2])
                        if col < max_col_index - 2:
                            Keypad._append_target(adj_dict[key], m[row + 1][col + 2])
        return adj_dict

    @staticmethod
    def _append_target(l: list[Optional[str]], t: str | None):
        if t != None:
            l.append(t)


def main():
    matrix: list[list[str | None]] = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        [None, "1", "2", "3", None],
    ]
    Keypad(matrix=matrix, max_depth=10, max_vowel=2).solve()


if __name__ == "__main__":
    main()
