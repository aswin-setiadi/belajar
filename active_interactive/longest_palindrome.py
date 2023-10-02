def SearchingChallenge(strParam: str):
    """
    loop (x, x+1 for even and ood) each char
      check if x is palindrome, if yes and longer than current result save
      expand x to left and right by 1 char if possible, repeat the check
      same for x+1
    x start with len 3 for odd, 4 for even, as 2 and below is invalid
    """
    # code goes here
    ans = ""
    s = strParam
    for i in range(len(s)):
        # odd
        l = i
        r = i + 2
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(ans):
                ans = s[l : r + 1]
            l -= 1
            r += 1

        # even
        l = i
        r = i + 1
        if r >= len(s):
            break
        if s[l] != s[r]:
            continue
        l -= 1
        r += 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(ans):
                ans = s[l : r + 1]
            l -= 1
            r += 1

    return ans if ans else "none"


# keep this function call here
print(SearchingChallenge("hellosannasmith"))

l = list("abcdefgh")
for i in range(2, len(l), 3):
    l[i] = "X"

l = "".join(l)
print(l)
