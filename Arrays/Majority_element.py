def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Test Cases
nums1 = [3, 2, 3]
print("Majority Element:", majority_element(nums1))

nums2 = [2, 2, 1, 1, 1, 2, 2]
print("Majority Element:", majority_element(nums2))