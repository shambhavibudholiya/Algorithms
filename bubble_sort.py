def sort(nums):
    for i in  range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                temp = nums[j]
                nums [j] = nums[j+1]
                nums[j+1] = temp

nums = [3,6,1,2,3,4,6,7,6,4,7,9,9,6]
sort(nums)
print(nums)