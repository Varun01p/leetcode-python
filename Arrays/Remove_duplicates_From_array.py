def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k, nums[:k]


# Test Cases
nums1 = [1, 1, 2]
k, arr = remove_duplicates(nums1)
print("Unique Count:", k)
print("Modified Array:", arr)

nums2 = [0,0,1,1,1,2,2,3,3,4]
k, arr = remove_duplicates(nums2)
print("Unique Count:", k)
print("Modified Array:", arr)