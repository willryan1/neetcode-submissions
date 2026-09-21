class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(c_i, c_j, used, c_word):
            if c_word == word:
                return True
            if c_i >= len(board):
                return False
            if c_j >= len(board[0]):
                return False
            if c_i < 0: return False
            if c_j < 0: return False
            if (c_i, c_j) in used:
                return False
            # x, y, used set, and current word so far
            if board[c_i][c_j] != word[len(c_word)]:
                return False
            if len(c_word) > len(word):
                return False

            used.add((c_i, c_j))
            curr = c_word + board[c_i][c_j]
            a = search(c_i + 1, c_j, used, curr)
            b = search(c_i, c_j + 1, used, curr)
            c = search(c_i - 1, c_j, used, curr)
            d = search(c_i, c_j - 1, used, curr)
            used.remove((c_i, c_j))

            return a or b or c or d
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i, j, set(), ""):
                    return True
        return False
            
            