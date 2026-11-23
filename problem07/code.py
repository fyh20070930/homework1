def longestPalindrome(s: str) -> str:
    # 向外扩散函数
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    res = ""
    for i in range(len(s)):
        s1 = expand(i, i)      # 奇数长度回文，中心i
        s2 = expand(i, i+1)    # 偶数长度回文，中心i,i+1
        # 保留更长的回文串
        if len(s1) > len(res):
            res = s1
        if len(s2) > len(res):
            res = s2
    return res

if __name__ == "__main__":
    st = "babad"
    print(f"输入字符串：{st}")
    print(f"输出：{longestPalindrome(st)}")
