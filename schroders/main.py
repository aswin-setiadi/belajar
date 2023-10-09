from collections import Counter
import logging
import os
import sys

from custom_exceptions import (
    DuplicateKeyException,
    InvalidKeyPadLayoutException,
    InvalidMaxDepthException,
    InvalidMaxVowelException,
)
from global_vars import VALID_PIECES
from utils import timer

DEBUGGING = os.getenv("DEBUGGING")
if DEBUGGING == "1":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logger = logging.getLogger(__name__)


class Keypad:
    def __init__(
        self, adj_dict: dict[str, list[str]], max_depth: int, max_vowel: int
    ) -> None:
        """
        Subpath_accumulator will keep track of all the traversed valid 10 key combination given conditions:
        - current vowel count
        - current char/ location the subpath starts
        - depth
        """
        self.adj_dict = adj_dict
        self.vowels = {"A": None, "E": None, "I": None, "O": None, "U": None}
        self.max_vowels = max_vowel
        self.subpath_accumulator: dict[str, int] = {}
        self.max_depth = max_depth
        self.max_depth_tracker = self.max_depth - 1
        self.combi_count: int = 0
        self.naive_results: list[list[str]] = []

    @timer
    def solve(self):
        for key in self.adj_dict.keys():
            if key in self.vowels:
                self.combi_count += self._traverse(key, 0, 1)
            else:
                self.combi_count += self._traverse(key, 0, 0)
        logger.info(f"{self.combi_count:,}")
        return self.combi_count

    def _traverse(self, node: str, depth: int, vowel_count: int) -> int:
        depth += 1
        if depth == self.max_depth:
            return 1
        else:
            # now max vowel can be 2+ digit and node can be 2+ digit, put seperator
            k = f"{vowel_count}_{node}_{depth}"
            if k in self.subpath_accumulator:
                return self.subpath_accumulator[k]
            else:
                subpath_count: int = 0
                for knight_path in self.adj_dict[node]:
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

    @timer
    def naive_solve(self, use_depth: bool = False):
        for key in self.adj_dict.keys():
            key_count = 1 if key in self.vowels else 0
            if use_depth:
                self.naive_traverse_use_depth(key, 0, key_count)
            else:
                self.naive_traverse(key, [], key_count)

        if use_depth:
            logger.info(f"{self.combi_count:,}")
        else:
            logger.info(f"{len(self.naive_results):,}")

    def naive_traverse(self, node: str, seq: list[str], vowel_count: int):
        cur_seq: list[str] = seq.copy()
        cur_seq.append(node)
        if len(cur_seq) == self.max_depth:
            self.naive_results.append(cur_seq)
        else:
            for knight_path in self.adj_dict[node]:
                if knight_path in self.vowels:
                    if vowel_count < 2:
                        self.naive_traverse(knight_path, cur_seq, vowel_count + 1)
                else:
                    self.naive_traverse(knight_path, cur_seq, vowel_count)

    def naive_traverse_use_depth(self, node: str, cur_depth: int, vowel_count: int):
        cur_depth += 1
        if cur_depth == self.max_depth:
            self.combi_count += 1
        else:
            for knight_path in self.adj_dict[node]:
                if knight_path in self.vowels:
                    if vowel_count < 2:
                        self.naive_traverse_use_depth(
                            knight_path, cur_depth, vowel_count + 1
                        )
                else:
                    self.naive_traverse_use_depth(knight_path, cur_depth, vowel_count)


class Builder:
    move_type = VALID_PIECES

    @classmethod
    def build_adjacency_list(
        cls, m: list[list[str | None]], piece_name: str
    ) -> dict[str, list[str]]:
        if piece_name not in Builder.move_type:
            raise Exception

        adj_dict: dict[str, list[str]] = {}
        max_row_index = len(m)
        max_col_index = len(m[0])
        if piece_name == VALID_PIECES[0]:
            for row in range(len(m)):
                for col in range(len(m[row])):
                    key = m[row][col]
                    if key != None:
                        adj_dict[key] = []
                        if row >= 2:
                            if col >= 1:
                                Builder._append_target(
                                    adj_dict[key], m[row - 2][col - 1]
                                )
                            if col < max_col_index - 1:
                                Builder._append_target(
                                    adj_dict[key], m[row - 2][col + 1]
                                )
                        if row >= 1:
                            if col >= 2:
                                Builder._append_target(
                                    adj_dict[key], m[row - 1][col - 2]
                                )
                            if col < max_col_index - 2:
                                Builder._append_target(
                                    adj_dict[key], m[row - 1][col + 2]
                                )
                        if row < max_row_index - 2:
                            if col >= 1:
                                Builder._append_target(
                                    adj_dict[key], m[row + 2][col - 1]
                                )
                            if col < max_col_index - 1:
                                Builder._append_target(
                                    adj_dict[key], m[row + 2][col + 1]
                                )
                        if row < max_row_index - 1:
                            if col >= 2:
                                Builder._append_target(
                                    adj_dict[key], m[row + 1][col - 2]
                                )
                            if col < max_col_index - 2:
                                Builder._append_target(
                                    adj_dict[key], m[row + 1][col + 2]
                                )

        if piece_name == VALID_PIECES[1]:
            for row in range(len(m)):
                for col in range(len(m[row])):
                    key = m[row][col]
                    if key is None:
                        continue
                    else:
                        if key not in adj_dict:
                            adj_dict[key] = []
                        possible_horizontal = m[row]
                        possible_vertical = [v[col] for v in m]
                        for cell in possible_horizontal:
                            if cell != key and cell is not None:
                                adj_dict[key].append(cell)
                        for cell in possible_vertical:
                            if cell != key and cell is not None:
                                adj_dict[key].append(cell)

        if piece_name == VALID_PIECES[2]:
            for row in range(len(m)):
                for col in range(len(m[row])):
                    key = m[row][col]
                    if key is None:
                        continue
                    else:
                        if key not in adj_dict:
                            adj_dict[key] = []
                        for row2 in range(len(m)):
                            if row2 != row:
                                col_diff = abs(row2 - row)
                                new_col = col - col_diff
                                new_col2 = col + col_diff
                                if new_col >= 0:
                                    target = m[row2][new_col]
                                    if target is not None:
                                        adj_dict[key].append(target)
                                if new_col2 < max_col_index:
                                    target = m[row2][new_col2]
                                    if target is not None:
                                        adj_dict[key].append(target)
        return adj_dict

    @staticmethod
    def _append_target(l: list[str], t: str | None):
        if t != None:
            l.append(t)


class Solution:
    @staticmethod
    def solve(
        matrix: list[list[str | None]],
        max_depth: int,
        max_vowel: int,
    ) -> int:
        if len(matrix) <= 1 or len(matrix[0]) <= 1:
            raise InvalidKeyPadLayoutException
        # check all rows have same column length
        _ = len(matrix[0])
        for row in matrix[1:]:
            if len(row) != _:
                raise InvalidKeyPadLayoutException
        _ = len(matrix) * len(matrix[0])
        if _ < 6:
            raise InvalidKeyPadLayoutException

        tmp_list = [v for sublist in matrix for v in sublist if v is not None]
        _ = [k for k, v in Counter(tmp_list).items() if v > 1]
        if _:
            raise DuplicateKeyException

        if max_depth < 0:
            raise InvalidMaxDepthException
        if max_vowel < 0:
            raise InvalidMaxVowelException

        if DEBUGGING:
            Keypad(
                matrix=matrix, max_depth=max_depth, max_vowel=max_vowel
            ).naive_solve()
            Keypad(matrix=matrix, max_depth=max_depth, max_vowel=max_vowel).naive_solve(
                use_depth=True
            )
        return Keypad(matrix=matrix, max_depth=max_depth, max_vowel=max_vowel).solve()


def main():
    matrix: list[list[str | None]] = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        [None, "1", "2", "3", None],
    ]
    Solution.solve(matrix=matrix, max_depth=10, max_vowel=2)


if __name__ == "__main__":
    main()
