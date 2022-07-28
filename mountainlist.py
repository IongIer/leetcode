from typing import List

#My very poor very slow solutin
def validMountainArray(arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    peak = max(arr)
    i = arr.index(peak)
    if peak == arr[-1] or peak == arr[0]:
        return False
    first = sorted(list(set(arr[: i + 1])))
    second = sorted(list(set(arr[i:])), reverse=True)
    return first == arr[: i + 1] and second == arr[i:]
