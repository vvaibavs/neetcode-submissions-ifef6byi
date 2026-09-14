class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            alph = [0] * 26
            for l in s:
                alph[ord(l) - ord('a')] += 1
            hashmap[tuple(alph)].append(s)
        return list(hashmap.values())
            


                