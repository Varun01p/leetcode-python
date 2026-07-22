def move_zeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


# Test Cases
nums1 = [0, 1, 0, 3, 12]
print(move_zeroes(nums1))

nums2 = [0]
print(move_zeroes(nums2))

nums3 = [1, 2, 3]
print(move_zeroes(nums3))