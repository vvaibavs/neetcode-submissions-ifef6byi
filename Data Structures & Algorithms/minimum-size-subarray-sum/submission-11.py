class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        first = 0
        second = 0
        sub = []
        total = nums[first]
        while second <= len(nums):
            if total < target:
                second += 1
                if second < len(nums): total += nums[second]
            elif total == target:
                if len(sub) > len(nums[first:second]) or len(sub) == 0:
                    sub = nums[first:second+1]
                first += 1
                second += 1
                total -= nums[first - 1]
                if second < len(nums): total += nums[second]
            elif total > target:
                if len(sub) > len(nums[first:second]) or len(sub) == 0:
                    sub = nums[first:second+1]
                first += 1
                total -= nums[first - 1]
        return len(sub)