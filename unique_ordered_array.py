# Remove duplicates from an increasingly ordered list with unique numbers present in increasing order in the start of the list.
# Replacement should be in place.
# Return number of unique numbers.
def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

nums = [1, 1, 2, 3, 3, 4, 4, 5]
print(removeDuplicates(nums))
print(nums)

# Output
# 5
# [1, 2, 3, 4, 5, 4, 4, 5]