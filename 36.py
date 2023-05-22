class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # combinations=board[::]
        combinations= board[::]+[[i[j] for i in board] for j in range(len(board))]

        for i in range(3):
            for j in range(3):
                squre = list(map(lambda x: x[i * 3:(i + 1) * 3], board[j * 3:3 * (j + 1)]))
                arr = []
                for item in squre:
                    arr += item
                combinations.append(arr)
        print('s')
        for item in combinations:
            if len(set(item)) + item.count('.') != 10:
                return False
        return True

#%%
board = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
x=Solution
Solution.isValidSudoku(x,board)
#%%



#%%

x=[[i[j] for i in board] for j in range(len(board))]
#%%
aa=x[0]
#%%
aa.count('.')
#%%

#%%
xx=[[i[j] for i in board[0:2]] for j in range(3)]
#%%
xxx=list(map(lambda x: x[0:3],board[0:3]))
#%%



aa=['8', '3', '.', '6', '.', '.', '.', '9', '8']
len(set(aa)) + aa.count('.')
