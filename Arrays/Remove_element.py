def remove_element(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k, nums[:k]


# Test Case 1
nums = [3, 2, 2, 3]
k, arr = remove_element(nums, 3)
print("Remaining Count:", k)
print("Modified Array:", arr)

# Test Case 2
nums = [0,1,2,2,3,0,4,2]
k, arr = remove_element(nums, 2)
print("Remaining Count:", k)
print("Modified Array:", arr)