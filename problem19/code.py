def maxProfit(prices):
    min_price = prices[0]  # 记录历史最低价格
    max_profit = 0
    for p in prices[1:]:
        if p < min_price:
            min_price = p
        else:
            profit = p - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

if __name__ == "__main__":
    price_list = [7,1,5,3,6,4]
    print(f"价格序列：{price_list}")
    print(f"最大利润：{maxProfit(price_list)}")
