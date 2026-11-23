def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        if area > max_water:
            max_water = area
        # 移动更小的挡板
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

if __name__ == "__main__":
    h1 = [1,8,6,2,5,4,8,3,7]
    print(f"输入数组：{h1}")
    print(f"最大盛水量：{maxArea(h1)}")

    h2 = [1,1]
    print(f"输入数组：{h2}")
    print(f"最大盛水量：{maxArea(h2)}")