

class Solution:
	# @param A : tuple of strings
	# @return an integer
    def isValidSudoku(self,A):
        c = 0
        K = []
        for i in range(0,9):
            K.append(list(A[i]))
        for i in range(0,9):
            l = []
            for j in range(0,9):
                if(K[i][j] == '.'):
                    pass
                else:
                    if(int(K[i][j]) in l):
                        c = 1
                        break
                    else:
                        l.append(int(K[i][j]))
        if (c != 1):
            for i in range(0,9):
                l = []
                for j in range(0,9):
                    if(K[j][i] == '.'):
                        pass
                    else:
                        if(int(K[j][i]) in l):
                            c = 1
                            break
                        else:
                            l.append(int(K[j][i]))
        if (c != 1):
            for h in range(0,7,3):
                if(c == 1):
                    break
                for i in range(0,7,3):
                    if(c == 1):
                        break
                    l = []
                    for j in range(0,3):
                        if(c == 1):
                            break
                        for k in range(0,3):
                            if(K[h+j][k+i] == '.'):
                                pass
                            else:
                                if(int(K[h+j][i+k]) in l):
                                    c = 1
                                    break
                                else:
                                    l.append(int(K[h+j][i+k]))
        if(c == 1):
            return 0
        else:
             return 1
