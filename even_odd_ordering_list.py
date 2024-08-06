# Arrange list numbers in even and odd order with even numbers
# coming first in the list followed by odd ones.
def even_odd(nums):
    next_even, next_odd = 0, len(nums) - 1
    while next_even < next_odd:
        if nums[next_even] % 2 == 0:
            next_even += 1
        else:
            nums[next_even], nums[next_odd] = nums[next_odd], nums[next_even]
            next_odd -= 1

nums = [1, 2, 3, 4, 5]
even_odd(nums)
print(nums) # Output => [4, 2, 3, 5, 1]