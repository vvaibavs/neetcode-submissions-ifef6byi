class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        group = defaultdict(list)

        for i in strs:
            alph = [0] * 26
            for j in i:
                alph[ord(j) - ord('a')] += 1
            group[tuple(alph)].append(i)
        
        return list(group.values())


                