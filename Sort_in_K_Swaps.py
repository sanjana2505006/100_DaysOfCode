def bubbleSort(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                count += 1

    return count <= k