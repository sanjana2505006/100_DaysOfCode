def maximumProduct(nums):
    nums.sort()
    pdt1 = nums[-1] * nums[-2] * nums[-3]
    pdt2 = nums[0] * nums[-1] * nums[-2]
    return max(pdt1, pdt2)