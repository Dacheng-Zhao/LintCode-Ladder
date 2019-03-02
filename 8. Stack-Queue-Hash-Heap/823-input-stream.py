class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        # Write your code here
        A = []
        for ele in inputA:
            if ele == '<' and len(A) == 0:
                continue
            elif ele == '<' and len(A) > 0:
                A.pop()
            else:
                A.append(ele)
        B = []
        for ele in inputB:
            if ele == '<' and len(B) == 0:
                continue
            elif ele == '<' and len(B) > 0:
                B.pop()
            else:
                B.append(ele)
        if A == B:
            return 'YES'
        else:
            return 'NO'
