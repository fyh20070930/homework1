def maxSubArray(nums):
    cur_sum = nums[0]   # 当前子数组和
    max_sum = nums[0]   # 全局最大和
    for x in nums[1:]:
        # 选：接上前面，或者重新以x开头
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"输入数组：{arr}")
    print(f"最大子数组和：{maxSubArray(arr)}")
