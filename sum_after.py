from typing import List

def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    answer = []
    running_sum = (sum(x for x in nums if not x % 2))
    for q in queries:
        if nums[q[1]] % 2:
            nums[q[1]] += q[0]
            if not nums[q[1]] % 2:
                running_sum += nums[q[1]]
                answer.append(running_sum)
            else:
                answer.append(running_sum)
        else:
            if not ((nums[q[1]] + q[0]) % 2):
                nums[q[1]] += q[0]
                running_sum += q[0]
                answer.append(running_sum)
            else:
                running_sum -= nums[q[1]]
                nums[q[1]] += q[0]
                answer.append(running_sum)
    return answer

print(sumEvenAfterQueries([8,-10,10,-7,4,-2],
[[6,4],[-7,0],[-3,5],[6,1],[-8,1],[-10,2]]))