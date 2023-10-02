from collections import defaultdict
from queue import Queue


def ArrayChallenge(strArr: list[str]):  # not working
    # code goes here
    class TrieNode:
        def __init__(self):
            self.char: dict[str, "TrieNode"] = defaultdict(TrieNode)
            self.is_word = False

    # all word != chars
    chars = strArr[0]
    words = strArr[1].split(",")
    trie = TrieNode()
    for word in words:
        node = trie
        for c in word:
            node = node.char[c]
        node.is_word = True
    print(trie.char.keys())
    print(trie.char["b"].char.keys())
    print(trie.char["b"].char["a"].char.keys())
    print(trie.char["b"].char["a"].char["l"].char.keys())
    print(trie.char["b"].char["a"].char["l"].char["l"].char.keys())
    print(trie.char)
    if trie.char:
        print(True)
    else:
        print(False)
    print(trie.char["b"].char["a"].char["l"].char["l"].char)
    if trie.char["b"].char["a"].char["l"].char["l"].char:
        print(True)
    else:
        print(False)
    ans = []
    tmp = []
    cursor = trie
    for c in chars:
        if c not in cursor.char:
            # print(ans)
            # print(tmp)
            return "not possible"
        # print(f"{c} {cursor.char.keys()}")
        tmp.append(c)
        cursor = cursor.char[c]
        if cursor.is_word:
            ans.append("".join(tmp))
            tmp = []
            cursor = trie

    return ",".join(ans)


def ArrayChallenge2(strArr: list[str]):
    chars = strArr[0]
    words = strArr[1].split(",")  # can use dict/ hashmap for faster search
    w1 = ""
    w2 = ""
    print(chars)
    print(words)
    for w1len in range(1, len(chars)):
        print(f"{chars[:w1len]}")
        if chars[:w1len] not in words:
            continue
        # w1 in words
        if chars[w1len:] in words:
            # w2 found
            w1 = chars[:w1len]
            w2 = chars[w1len:]
            break

    if not w1:
        return "not possible"
    else:
        return f"{w1},{w2}"


# keep this function call here
# print(ArrayChallenge(["baseball", "base,ball"]))
print(ArrayChallenge2(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))
