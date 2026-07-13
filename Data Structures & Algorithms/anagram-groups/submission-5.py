class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        res = []
        for s in strs:
            alph = [0] * 26
            for i in range(len(s)):
                alph[ord(s[i]) - ord('a')] += 1
            temp[tuple(alph)].append(s)

        return list(temp.values())
            