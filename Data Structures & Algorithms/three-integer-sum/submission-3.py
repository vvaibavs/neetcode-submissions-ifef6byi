class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    remainder = (nums[i] + nums[j]) * -1
                    if remainder in nums and nums.index(remainder) != i and nums.index(remainder) != j:
                        temp = [nums[i], nums[j], nums[nums.index(remainder)]]
                        temp.sort()
                        if temp not in answer:
                            answer.append(temp)
        return answer
