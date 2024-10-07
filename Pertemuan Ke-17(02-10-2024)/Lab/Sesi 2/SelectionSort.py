def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

    return nums  # Mengembalikan list yang sudah disortir


# Masukkan angka-angka, sortir, dan cetak tanpa tanda kurung atau koma
sorted_nums = selection_sort(list(map(int, input().split())))
print(" ".join(map(str, sorted_nums)))
