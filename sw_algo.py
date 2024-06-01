class Node:
    def __init__(self):
        self.score = 0
        self.pointer = None

class SmithWaterman:
    def __init__(self, seq1, seq2, match=2, mismatch=-1, gap=-1):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

        self.matrix = [[Node() for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    def calculate_scores(self):

        for i in range(1, len(self.seq1)+1):
            for j in range(1, len(self.seq2)+1):

                if self.seq1[i-1] == self.seq2[j-1]:
                    match_score = self.matrix[i-1][j-1].score + self.match
                else:
                    match_score = self.matrix[i-1][j-1].score + self.mismatch

                delete_score = self.matrix[i-1][j].score + self.gap
                insert_score = self.matrix[i][j-1].score + self.gap

                self.matrix[i][j].score = max(0, match_score, delete_score, insert_score)

                if self.matrix[i][j].score == match_score:
                    self.matrix[i][j].pointer = self.matrix[i-1][j-1]
                elif self.matrix[i][j].score == delete_score:
                    self.matrix[i][j].pointer = self.matrix[i-1][j]
                elif self.matrix[i][j].score == insert_score:
                    self.matrix[i][j].pointer = self.matrix[i][j-1]




    def traceback(self):

        max_score = 0
        max_pos = (0,0)

        for i in range(len(self.seq1)+1):
            for j in range(len(self.seq2)+1):
                if self.matrix[i][j].score > max_score:
                    max_score = self.matrix[i][j].score
                    max_pos = (i,j)

        align1 = ""
        align2 = ""
        i, j = max_pos

        while self.matrix[i][j].score > 0:
            if self.matrix[i][j].pointer == self.matrix[i-1][j-1]:
                align1 += self.seq1[i-1]
                align2 += self.seq2[j-1]
                i -= 1
                j -= 1
            elif self.matrix[i][j].pointer == self.matrix[i][j-1]:
                align1 += "-"
                align2 += self.seq2[j-1]
                j -= 1
            elif self.matrix[i][j].pointer == self.matrix[i-1][j]:
                align1 += self.seq1[i-1]
                align2 += "-"
                i -= 1

        return align1[::-1], align2[::-1], max_score

    def align(self):
        self.calculate_scores()
        return self.traceback()

sw = SmithWaterman('AATCGTAT', 'GCCCTAGG')
align1, align2, score = sw.align()

print(f'Alignment Score: {score}')
print(f'Alignment 1: {align1}')
print(f'Alignment 2: {align2}')
