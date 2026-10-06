class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        for n in range(len(nums)):
            remainder = {}
            target = -(nums[n])
            for i in range(len(nums)):
                if i!=n:
                    if target - nums[i] not in remainder:
                        remainder[nums[i]] = i
                    else:
                        temp = sorted([nums[n], target-nums[i], nums[i]])
                        if temp not in res:
                            res.append(temp)
        return res
