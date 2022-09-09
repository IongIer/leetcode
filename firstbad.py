# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        bad_version = set()
        mid = (n + 1) // 2
        while mid >= 1 and mid <= n:
            if isBadVersion(mid):
                if mid not in bad_version:
                    bad_version.add(mid)
                    n = mid
                    mid = (mid + 1) // 2
                else:
                    return mid
            else:
                mid = (mid + n + 1) // 2
