class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        n, m = len(board), len(board[0])
        vis = {}

        view_list = []
        for i in range(m):
            if board[0][i] == 'O':
                view_list.append((0, i))
            
            if board[n-1][i] == 'O':
                view_list.append((n-1, i))
        
        for i in range(1, n-1):
            if board[i][0] == 'O':
                view_list.append((i, 0))
            if board[i][m-1] == 'O':
                view_list.append((i, m-1))
    
        while view_list:
            val = view_list.pop()
            i, j = val

            if val in vis: continue
            board[i][j] = 'T'
            vis[val] = True

            if i > 0 and board[i-1][j] == 'O':
                board[i-1][j] = 'T'
                view_list.append((i-1, j))
            if i < len(board)-1 and board[i+1][j] == 'O':
                board[i+1][j] == 'T'
                view_list.append((i+1, j))
            if j > 0 and board[i][j-1] == 'O':
                board[i][j-1] = 'T'
                view_list.append((i, j-1))
            if j < len(board[0]) - 1 and board[i][j+1] == 'O':
                board[i][j+1] = 'T'
                view_list.append((i, j+1))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        