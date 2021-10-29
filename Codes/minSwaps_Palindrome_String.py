def countSwap(str, n):
    str = list(str)
    count = 0
    ans = True

    for i in range(n//2):

        left = i
        right = n - left - 1

        while left < right:
            if str[left] == str[right]:
                break
            else:
                right = right - 1
        # if both pointer at same position, then we don't have sufficient no of swaps to make palindromic string
        if left == right:
            ans = False
            break
        else:
            for j in range(right, n-left-1):
                str[j], str[j+1] = str[j+1], str[j]
                count = count + 1
    if ans:
        return count
    else:
        return -1

str = "aabcb"
n = len(str)

ans1 = countSwap(str, n)
ans2 = countSwap(str[::-1], n)

print(max(ans1, ans2))
