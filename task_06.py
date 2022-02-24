def find_maximum_number(*nums):
    max_number = nums[0]
    for num in nums:
        if num > max_number:
            max_number = num
    return max_number

print(find_maximum_number(20, -6, 1, 9))
print(find_maximum_number(20, -6, 40, 1, 9))
