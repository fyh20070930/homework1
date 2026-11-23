def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            # 题目下标从1开始
            return [left + 1, right + 1]
        elif total < target:
            left += 1  # 和太小，左指针右移
        else:
            right -= 1 # 和太大，右指针左移
    return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    t = 9
    print(f"数组：{nums}, target={t}")
    print(twoSum(nums, t))
