def find_max(*nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(20, -6, 1, 9))
print(find_max(20, -6, 40, 1, 9))
