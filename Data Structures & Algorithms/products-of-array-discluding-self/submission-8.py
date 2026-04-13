class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = []
        suffixProd = []

        for i in range(len(nums)):
            temp = 1
            if(i < len(nums) - 1):
                for j in range(i+1, len(nums)):
                    temp *= nums[j]
            else:
                temp = 1
            suffixProd.append(temp)

        for i in range(len(nums)):
            temp = 1
            if(i > 0):
                for j in range(i-1, -1, -1):
                    temp*=nums[j]
            else:
                temp = 1
            prefixProd.append(temp)
        
        print(prefixProd)
        print(suffixProd)
        
        res = []
        for i in range(len(prefixProd)):
            res.append(prefixProd[i] * suffixProd[i])

        return res