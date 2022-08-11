END_SYMBOL = "*"

class Trie:
    def __init__(self):
        self.head = dict()

    def add(self, word: str):
        node = self.head
        for ch in word:
            if ch not in node:
                node[ch] = dict()
            node = node[ch]

        node[END_SYMBOL] = None

def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)

    result = set()
    for j in range(len(board)):
        for i in range(len(board[0])):
            explore(board, j, i, trie.head, "", result)

    return list(result)

def explore(board, row, column, trie_node, word, result):
    if board[row][column] not in trie_node:
        return

    curr_char = board[row][column]
    word = word + curr_char
    trie_node = trie_node[curr_char]
    if END_SYMBOL in trie_node:
        result.add(word)
        trie_node.pop(END_SYMBOL)
        if len(trie_node) == 0:
            return

    board[row][column] = END_SYMBOL
    
    for j, i in get_positions(board, row, column):
        explore(board, j, i, trie_node, word, result)

    if curr_char in trie_node and len(trie_node[curr_char]) == 0:
        trie_node.pop(curr_char)
    
    board[row][column] = curr_char

def get_positions(board, row, column):
    n, m = len(board), len(board[0])

    for j in range(row - 1, row + 2):
        for i in range(column - 1, column + 2):
            if j >= 0 and j < n and i >= 0 and i < m and board[j][i] != "@":
                yield [j, i]
