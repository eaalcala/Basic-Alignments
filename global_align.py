class Node():
    def __init__(self):
        self.score = 0
        self.pointer = None


class GlobalAlignment():

    def __init__(self, seq1, seq2, match=1, mismatch=-1, gap=-2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.matrix = [[Node() for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    
    def calculate_scores(self):
        
        for i in range(1, len(self.seq1) + 1):
            self.matrix[i][0].score = self.matrix[i-1][0].score + self.gap
            self.matrix[i][0].pointer = self.matrix[i-1][0]
            
        for j in range(1, len(self.seq2) + 1):
            self.matrix[0][j].score = self.matrix[0][j-1].score + self.gap
            self.matrix[0][j].pointer = self.matrix[0][j-1]


        # for i in range(len(self.matrix)):
        #     for j in range(len(self.matrix[0])):
        #         print(self.matrix[i][j].score, end=" ")
        #     print()

        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                curr_match = self.match
                if self.seq1[i-1] != self.seq2[j-1]:
                    curr_match = self.mismatch
                
                self.matrix[i][j].score = max(self.matrix[i-1][j].score + self.gap, self.matrix[i][j-1].score + self.gap, self.matrix[i-1][j-1].score + curr_match)

                # "d", "h", "v"
                if self.matrix[i][j].score == self.matrix[i-1][j-1].score + curr_match:
                    self.matrix[i][j].pointer = self.matrix[i-1][j-1]
                elif self.matrix[i][j].score == self.matrix[i][j-1].score + self.gap:
                    self.matrix[i][j].pointer = self.matrix[i][j-1]
                elif self.matrix[i][j].score == self.matrix[i-1][j].score + self.gap:
                    self.matrix[i][j].pointer = self.matrix[i-1][j]
                
        # for i in range(len(self.matrix)):
        #     for j in range(len(self.matrix[0])):
        #         print(self.matrix[i][j].score, end=" ")
        #     print()
        res1, res2 = self.backtracking()
        print(self.matrix[i][j].score)
        print(res1)
        print(res2)
        return [self.matrix[i][j].score, res1, res2]
        
    
    def backtracking(self):
        i = len(self.seq1)
        j = len(self.seq2)
        res1 = ""
        res2 = ""
        while i + j != 0:
            if self.matrix[i][j].pointer == self.matrix[i-1][j-1]:
                res1 += self.seq1[i-1]
                res2 += self.seq2[j-1]
                i -= 1
                j -= 1
            elif self.matrix[i][j].pointer == self.matrix[i-1][j]:
                res1 += self.seq1[i-1]
                res2 += "-"
                i -= 1
            elif self.matrix[i][j].pointer == self.matrix[i][j-1]:
                res1 += "-"
                res2 += self.seq2[j-1]
                j -= 1
        res1 = res1[::-1]
        res2 = res2[::-1]
        return [res1, res2]



# 3 1 2
# G
# ACATACGATG


dum = GlobalAlignment("G", "ACATACGATG", match=3, mismatch=-1, gap=-2)

dum.calculate_scores()
        