class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        freq = {}
        res = ""
        for i, n in enumerate(order):
            if n in s:
                hashmap[i] = n
        for i in s:
            if i not in hashmap.values():
                res += i
            else:
                freq[i] = freq.get(i, 0) + 1

        for v in hashmap.values():
            for i in range(freq[v]):
                res += v
            

        return res