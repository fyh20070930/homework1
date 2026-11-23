def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    nums1 = [2,7,11,15]
    t1 = 9
    res1 = twoSum(nums1, t1)
    print(f"输入数组：{nums1}，target={t1}")
    print(f"结果下标（从1开始）：{res1}")

    nums2 = [2,3,4]
    t2 = 6
    res2 = twoSum(nums2, t2)
    print(f"输入数组：{nums2}，target={t2}")
    print(f"结果下标（从1开始）：{res2}")
