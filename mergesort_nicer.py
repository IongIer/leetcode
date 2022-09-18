from typing import List


def sort_array(nums: List[int]) -> List[int]:
    def mergesort(arr):
        len_arr = len(arr)
        if len_arr <= 1:
            return arr
        left_half = mergesort(arr[: len_arr // 2])
        right_half = mergesort(arr[len_arr // 2 :])
        return merge(left_half, right_half)

    def merge(left_half, right_half):
        len_left_half = len(left_half)
        len_right_half = len(right_half)
        sol = []
        i = 0
        j = 0
        while i < len_left_half and j < len_right_half:
            if left_half[i] <= right_half[j]:
                sol.append(left_half[i])
                i += 1
            else:
                sol.append(right_half[j])
                j += 1
        return sol + (right_half[j:] if i == len_left_half else left_half[i:])

    return mergesort(nums)
