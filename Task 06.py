def find_max(*nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    print(max_num)

find_max(20, -6, 1, 9)
find_max(20, -6, 40, 1, 9)
