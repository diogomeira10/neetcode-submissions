class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)

        products = []
        
        if zero_count:
            for num in nums:
                products.append(0) if num else products.append(product)
        else:
            for num in nums:
                products.append(product // num)

        return products