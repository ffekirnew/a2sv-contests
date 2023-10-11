class TrieNode:
    def __init__(self, is_end_of_word: int = 0, words_node_is_part_of: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word
        self.words_node_is_part_of = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            char_is_end_of_word = i == len(word) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(char_is_end_of_word, 1)
            else:
                curr.children[char].is_end_of_word |= char_is_end_of_word
                curr.children[char].words_node_is_part_of += 1

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            if (
                char not in curr.children
                or curr.children[char].words_node_is_part_of == 1
            ):
                return i

            curr = curr.children[char]

        return i + 1


class SlackBot:
    def trie_solution(self):
        trie = Trie()

        num_strings = int(input())
        strings = []

        for _ in range(num_strings):
            strings.append(input())
            trie.insert(strings[-1])

        for word in strings:
            print(trie.search(word))

    def solve(self):
        num_strings = int(input())
        strings = []

        for _ in range(num_strings):
            strings.append(input())

        for i in range(num_strings):
            max_similarity = 0
            for j in range(num_strings):
                if i == j:
                    continue

                string_i, string_j = strings[i], strings[j]
                similarity = 0

                for k in range(min(len(string_i), len(string_j))):
                    if string_i[k] != string_j[k]:
                        break
                    similarity += 1

                max_similarity = max(max_similarity, similarity)

            print(max_similarity)


if __name__ == "__main__":
    slack_bot = SlackBot()
    slack_bot.trie_solution()
