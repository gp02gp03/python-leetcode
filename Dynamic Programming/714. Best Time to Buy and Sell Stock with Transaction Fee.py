'''
Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
'''
'''
cash => 第i天結束後,手中沒持有股票的最大收益 (由前一天賣出股票或是前一天持有股票但在當天賣出)
hold => 第i天結束後,手中還持有股票的最大收益 (由前一天持有股票或是前天沒有股票但在今天買入)
'''


def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash


print(maxProfit([1, 3, 2, 8, 4, 9], 2))
