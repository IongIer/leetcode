def firstBadVersion(n) -> int:
    l = 0
    r = len(n) - 1
    while l <= r:
        mid = (l + r) // 2
        if n[mid]:
            r = mid
            bad = mid
        else:
            l = mid - 1
    return bad


print(firstBadVersion([0, 0, 0, 1, 1]))
