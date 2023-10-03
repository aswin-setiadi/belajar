from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.char_dict: dict[str, TrieNode] = defaultdict(TrieNode)
        self.isword = False


class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie = TrieNode()
        self.prefix = ""

        # build trie in reverse
        for w in words:
            w_ = w[::-1]
            cursor = self.trie
            for c in w_:
                cursor = cursor.char_dict[c]
            cursor.isword = True

    def query(self, letter: str):
        self.prefix += letter
        cursor = self.trie
        for c in reversed(self.prefix):
            if c in cursor.char_dict:
                cursor = cursor.char_dict[c]
                if cursor.isword:
                    return True
            else:
                return False


if __name__ == "__main__":
    # Your StreamChecker object will be instantiated and called as such:
    # obj = StreamChecker(words)
    # param_1 = obj.query(letter)
    words = ["cd", "f", "kl"]
    letters = [
        ["a"],
        ["b"],
        ["c"],
        ["d"],
        ["e"],
        ["f"],
        ["g"],
        ["h"],
        ["i"],
        ["j"],
        ["k"],
        ["l"],
    ]
    words = ["ab", "ba", "aaab", "abab", "baa"]
    letters = [
        ["a"],
        ["a"],
        ["a"],
        ["a"],
        ["a"],
        ["b"],
        ["a"],
        ["b"],
        ["a"],
        ["b"],
        ["b"],
        ["b"],
        ["a"],
        ["b"],
        ["a"],
        ["b"],
        ["b"],
        ["b"],
        ["b"],
        ["a"],
        ["b"],
        ["a"],
        ["b"],
        ["a"],
        ["a"],
        ["a"],
        ["b"],
        ["a"],
        ["a"],
        ["a"],
    ]
    sc = StreamChecker(words)
    for l in letters:
        param_1 = sc.query(l[0])
        print(param_1)
        # input("pause")
