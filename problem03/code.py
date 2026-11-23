def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    res = ""
    for i in range(len(s)):
        s1 = expand(i, i)
        s2 = expand(i, i+1)
        if len(s1) > len(res):
            res = s1
        if len(s2) > len(res):
            res = s2
    return res

if __name__ == "__main__":
    s1 = "babad"
    print(f"输入字符串：{s1}")
    print(f"最长回文子串：{longestPalindrome(s1)}")

    s2 = "cbbd"
    print(f"输入字符串：{s2}")
    print(f"最长回文子串：{longestPalindrome(s2)}")
