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

    def query(self, letter: str) -> bool:
        self.prefix += letter
        index = len(self.prefix) - 1
        print(self.prefix)
        # print(index)
        # print(self.trie.char_dict.keys())
        cursor = self.trie
        while True:
            if index >= 0:
                if self.prefix[index] in cursor.char_dict:
                    cursor = cursor.char_dict[self.prefix[index]]
                    if cursor.isword:
                        print(self.prefix[index:])
                        return True
                    index -= 1
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
    sc = StreamChecker(words)
    for l in letters:
        param_1 = sc.query(l[0])
        print(param_1)
        # input("pause")
