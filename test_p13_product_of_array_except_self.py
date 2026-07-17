class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        # counting left through the array
        left_product = 1
        for i in range(n):
            # create the answer using the left_product from the previous loop or 1
            answer[i] = left_product
            # create a left product for the next loop so it can be put in the answer array
            left_product *= nums[i]

        # counting right through the array
        right_product = 1
        for i in range(n - 1, -1, -1):
            # create an answer multiplying from the right with the last right product or 1
            answer[i] *= right_product
            # cretae a right product multiplying the last one with a current nums[i] for the next loop
            right_product *= nums[i]

        return answer