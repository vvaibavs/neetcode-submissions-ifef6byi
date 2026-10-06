class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortednums = sorted(nums)

        for i in range(len(sortednums)):
            j = i+1
            k = len(sortednums) - 1
            target = sortednums[i] * -1
            
            while j < k:
                if j == i:
                    j+=1
                elif k == i:
                    k-=1
                else:
                    if sortednums[j] + sortednums[k] + sortednums[i] > 0:
                        k-=1
                    elif sortednums[j] + sortednums[k] + sortednums[i] < 0:
                        j+=1
                    elif sortednums[j] + sortednums[k] + sortednums[i] == 0:
                        s = sorted([sortednums[i], sortednums[j], sortednums[k]])
                        if s not in res:
                            res.append(s)
                        j+=1
                        k-=1

        return res
