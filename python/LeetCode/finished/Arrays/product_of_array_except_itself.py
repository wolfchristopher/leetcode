
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize the output array with 1s. example n = 4, output = [1, 1, 1, 1]

        """
        We start with left = 1. This will be used to store the cumulative product of the elements to the left of the 
        current index i. We initialize left to 1 because we need a neutral starting value for multiplication. In other 
        words, before we start multiplying, we want the product to be 1 so that it doesn’t affect the result. 
        """
        # First pass: compute the product of elements to the left of each index.
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # Second pass: compute the product of elements to the right of each index.
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output