class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for w in words:
            for n in words:
                if w != n and w in n and w not in answer:
                    answer.append(w)

        return answer