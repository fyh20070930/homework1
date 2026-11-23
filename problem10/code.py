def search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2  # 取中间位置
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # 目标更大，去右边找
        else:
            right = mid - 1 # 目标更小，去左边找
    return -1  # 没找到

if __name__ == "__main__":
    arr = [-1,0,3,5,9,12]
    t = 9
    print(f"数组：{arr}，目标={t}")
    print("下标：", search(arr,t))
