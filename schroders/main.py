import logging
import sys
import time


from global_vars import DEBUGGING

if DEBUGGING:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Keypad:
    """ """

    def __init__(self, max_depth: int = 10) -> None:
        """
        Subpath_count will keep track of all the traversed valid 10 key combination given conditions:
        - current vowel count
        - current char (vowel or not)
        - depth
        """
        self.vowels = {"A": None, "E": None, "I": None, "O": None, "U": None}
        self.subpath_accumulator: dict[str, int] = {}
        self.matrix: dict[str, list[str]] = {}
        self.matrix["A"] = ["H", "L"]
        self.matrix["B"] = ["I", "K", "M"]
        self.matrix["C"] = ["F", "J", "L", "N"]
        self.matrix["D"] = ["G", "M", "O"]
        self.matrix["E"] = ["H", "N"]
        self.matrix["F"] = ["C", "M", "1"]
        self.matrix["G"] = ["D", "N", "2"]
        self.matrix["H"] = ["A", "E", "K", "O", "1", "3"]
        self.matrix["I"] = ["B", "L", "2"]
        self.matrix["J"] = ["C", "M", "3"]
        self.matrix["K"] = ["B", "H", "2"]
        self.matrix["L"] = ["A", "C", "I", "3"]
        self.matrix["M"] = ["B", "D", "F", "J"]
        self.matrix["N"] = ["C", "E", "G", "1"]
        self.matrix["O"] = ["D", "H", "2"]
        self.matrix["1"] = ["F", "H", "N"]
        self.matrix["2"] = ["G", "I", "K", "O"]
        self.matrix["3"] = ["H", "J", "L"]
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
        logging.debug(t2 - t1)
        logging.debug(len(self.subpath_accumulator))
        logging.info(self.combi_count)
        return self.combi_count

    def _traverse(self, node: str, depth: int, vowel_count: int) -> int:
        depth += 1
        # input(f"node={node} cur_seq={cur_seq} #vowel={vowel_count}")
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
                        # print(f"{knight_path} is vowel")
                        if vowel_count < 2:
                            subpath_count += self._traverse(
                                knight_path, depth, vowel_count + 1
                            )

                    else:
                        subpath_count += self._traverse(knight_path, depth, vowel_count)
                if 2 <= depth and self.max_depth_tracker >= depth:
                    self.subpath_accumulator[k] = subpath_count
            return subpath_count


if __name__ == "__main__":
    Keypad(max_depth=10).solve()
