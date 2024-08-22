def solution(n, times):
    # if n <= len(times):
    #     result = times[n - 1]
    #     return result
    times.sort()
    start = 1
    end = times[-1] * n
    result = 0
    a = True
    while start <= end:
        possible_person = 0
        mid = (start + end) // 2
        for i in range(len(times)):
            possible_person += (mid // times[i])
            if possible_person >= n:
                result = mid
                end = mid - 1
                a = False
                break
        if not a:
            a = True
            continue
        else:
            start = mid + 1
    return result