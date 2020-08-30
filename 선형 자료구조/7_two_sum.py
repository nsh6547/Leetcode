nums= [2, 7, 11, 15]
target = 9

left, right =0, len(nums)-1
while  left !=right:
    if nums[left] + nums[right] < target:
        left += 1

    elif nums[left] +nums[right] > target:
        right -=1

    else:
        print([left, right])

# 풀이 4
# nums_map={}
#
# for i,num in enumerate(nums):
#     if target - num in nums_map:
#         print( [nums_map[target-num], i])
#     nums_map[num]=i

# 풀이 3
# for i,num in enumerate(nums):
#     nums_map[num]=i
#
# for i, num in enumerate(nums):
#     if target - num in nums_map and i != nums_map[target- num]:
#         print([nums.index(num), nums_map[target - num]])
# 풀이2
# for i,n in enumerate(nums):
#     print(i,n)
#     complement = target - n
#     if complement in nums[i+1:]:
#         print([nums.index(n), nums[i+1:].index(complement)+ (i+1)])

# 풀이1
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] ==target:
#             print([i,j])

