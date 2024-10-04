def bubble_sort(nums):
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                is_sorted = False

        i += 1

    return nums

sorted_nums = bubble_sort(list(map(int, input().split())))
print(" ".join(map(str, sorted_nums)))