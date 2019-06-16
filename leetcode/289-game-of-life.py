class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        #print board
        
        # 0 -> 0: 0
        # 1 -> 0: 3
        # 0 -> 1: 2
        # 1 -> 1: 1

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                
                liveCount = 0
                deadCount = 0
                
                for m in range(max(i-1, 0), min(i+2, len(board))):
                    for n in range(max(j-1, 0), min(j+2, len(board[i]))):
                        if m == i and n == j:
                            continue
                        v = board[m][n]
                        if v == 0 or v == 2:
                            deadCount += 1
                        else:
                            liveCount += 1
                
                if board[i][j] == 1:
                    if liveCount < 2:
                        board[i][j] = 3
                    elif liveCount <= 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
                elif liveCount == 3:
                    board[i][j] = 2

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
                    
        #print board
