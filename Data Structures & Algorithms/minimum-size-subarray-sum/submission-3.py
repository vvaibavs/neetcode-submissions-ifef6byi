class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        first = 0
        second = 1
        sub = []
        while second <= len(nums):
            total = sum(nums[first:second])
            if total < target:
                second += 1
            elif total == target:
                if len(sub) > len(nums[first:second]) or len(sub) == 0:
                    sub = nums[first:second]
                first += 1
                second += 1
            elif total > target:
                if len(sub) > len(nums[first:second]) or len(sub) == 0:
                    sub = nums[first:second]
                first += 1
        print(sub)
        return len(sub)

        