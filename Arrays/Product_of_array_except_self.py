n = int(input("Enter size of array: "))

nums = list(map(int, input("Enter numbers: ").split()))

answer = [1] * n

prefix = 1
for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]

print("Product Array:", *answer)