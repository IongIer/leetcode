class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(arr, start, end):
            if end - start + 1 == 1:
                return arr
            middle = (start + end) // 2
            divide(arr, start, middle)
            divide(arr, middle + 1, end)
            conquer(arr, start, middle, end)
            return arr

        def conquer(arr, start, middle, end):
            left = arr[start : middle + 1]
            right = arr[middle + 1 : end + 1]
            i = 0
            j = 0
            k = start
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return divide(nums, 0, len(nums))
