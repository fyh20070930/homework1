def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    # 从第3阶循环到n
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    return b

if __name__ == "__main__":
    n = 3
    print(f"n={n}，方法数：{climbStairs(n)}")
