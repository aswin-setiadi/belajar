import time


class KeyPad:
    """ """

    def __init__(self) -> None:
        self.vowels = {"A": None, "E": None, "I": None, "O": None, "U": None}
        self.combi_count: int = 0
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

    def solve(self):
        t1 = time.time()
        for key in self.matrix.keys():
            if key in self.vowels:
                self._traverse(key, 0, 1)
            else:
                self._traverse(key, 0, 0)
        t2 = time.time()
        print(t2 - t1)
        print(self.combi_count)
        return self.combi_count

    def _traverse(self, node: str, depth: int, vowel_count: int):
        depth += 1
        # input(f"node={node} cur_seq={cur_seq} #vowel={vowel_count}")
        if depth == 10:
            self.combi_count += 1
        else:
            for knight_path in self.matrix[node]:
                if knight_path in self.vowels:
                    # print(f"{knight_path} is vowel")
                    if vowel_count < 2:
                        self._traverse(knight_path, depth, vowel_count + 1)
                else:
                    self._traverse(knight_path, depth, vowel_count)


if __name__ == "__main__":
    KeyPad().solve()
