def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # 存放当前窗口内的字符
    left = 0  # 窗口左边界
    max_len = 0  # 记录最长长度
    for right in range(len(s)):
        # 当前字符已经在窗口内，持续收缩左边界
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        # 更新最大长度
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    st = "abcabcbb"
    print(f"输入字符串：{st}")
    print(f"输出：{lengthOfLongestSubstring(st)}")
