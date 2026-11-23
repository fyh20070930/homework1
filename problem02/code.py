def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        # 遇到重复字符，左指针右移，移除集合里的字符
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s1 = "abcabcbb"
    print(f"输入字符串：{s1}")
    print(f"最长无重复子串长度：{lengthOfLongestSubstring(s1)}")

    s2 = "bbbbb"
    print(f"输入字符串：{s2}")
    print(f"最长无重复子串长度：{lengthOfLongestSubstring(s2)}")

    s3 = "pwwkew"
    print(f"输入字符串：{s3}")
    print(f"最长无重复子串长度：{lengthOfLongestSubstring(s3)}")
