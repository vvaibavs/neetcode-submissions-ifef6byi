class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            alph = [0] * 26
            for i in s:
                alph[ord(i) - ord('a')] += 1
            hashmap[tuple(alph)].append(s)
        return list(hashmap.values())

        
            


                