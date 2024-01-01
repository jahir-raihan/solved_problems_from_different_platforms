class Solution:
    def snakesAndLadders(self, board):
        length = len(board)
        
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            
            if r % 2:
                c = length - 1 - c
            return r, c
        
        q = deque()
        visit = set()
        q.append([1, 0])
        
        while q:
            square, moves = q.popleft()
            for i in range(1,7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c]!= -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSqaure not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
              
         
        
