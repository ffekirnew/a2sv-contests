from typing import List


class TrieNode:
    def __init__(self, is_end_of_word: int = 0, number: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word
        self.number = number


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, binary_representation: str, number: int) -> None:
        curr = self.root

        for i, char in enumerate(binary_representation):
            char_is_end_of_word = i == len(binary_representation) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(char_is_end_of_word, number)
            else:
                curr.children[char].is_end_of_word |= char_is_end_of_word
                curr.number = -1 if not char_is_end_of_word else number

            curr = curr.children[char]

    def search(self, binary_representation: str) -> bool:
        curr = self.root
        nemesis = self.root

        oposite = {'0':'1', '1':'0'}

        for i, char in enumerate(binary_representation):
            if oposite[char] in nemesis.children:
                nemesis = nemesis.children[oposite[char]]
            else:
                nemesis = nemesis.children[char]

            curr = curr.children[char]

        return curr.number ^ nemesis.number

    @classmethod
    def build_trie(cls, numbers: List[str]) -> "Trie":
        trie = cls()

        for number in numbers:
            binary_rep = binary_representation(number)
            trie.insert(binary_rep, number)

        return trie

def binary_representation(decimal: int, limit: int = 20) -> str:
    representation = bin(decimal)[2:]

    return ('0' * (limit - len(representation))) + representation



def solve():
    tests = int(input())
    for _ in range(tests):
       n = int(input())
       array = list(map(int, input().split()))

       trie = Trie.build_trie(array)

       print(max([ trie.search(binary_representation(number) for number in array) ]))


if __name__ == "__main__":
    solve()