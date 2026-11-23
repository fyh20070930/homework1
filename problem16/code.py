def reverseString(s):
    left = 0                 # 左指针，起始位置
    right = len(s) - 1       # 右指针，末尾位置
    while left < right:
        s[left], s[right] = s[right], s[left]  # 交换左右字符
        left += 1
        right -= 1
    return s

if __name__ == "__main__":
    arr = ["h","e","l","l","o"]
    print(f"输入：{arr}")
    reverseString(arr)
    print(f"反转后：{arr}")
