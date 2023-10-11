class TrieNode:
    def __init__(self, is_end_of_word: int = 0, word_index: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            char_is_end_of_word = i == len(word) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(char_is_end_of_word)
            else:
                curr.children[char].is_end_of_word |= char_is_end_of_word

            curr = curr.children[char]

    def search(self) -> bool:
        curr = self.root
        count = 0

        while curr and curr.children:
            if len(curr.children.keys()) > 1:
                break

            count += 1
            curr = list(curr.children.values())[0]

        return count


def solve():
    word1 = input()[::-1]
    word2 = input()[::-1]

    trie = Trie()
    trie.insert(word1)
    trie.insert(word2)

    similarity = trie.search()
    sum_of_lengths = sum([len(word1), len(word2)])
    if similarity > len(word1) or similarity > len(word2):
        print(sum_of_lengths - 2 * min([len(word1), len(word2)]))
    else:
        print(sum_of_lengths - 2 * similarity)


if __name__ == "__main__":
    solve()
