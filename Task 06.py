def find_max(*nums):
    max_no = nums[0]
    for num in nums:
        if num > max_no:
            max_no = num
    print(max_no)

find_max(20, -6, 1, 9)
find_max(20, -6, 40, 1, 9)
