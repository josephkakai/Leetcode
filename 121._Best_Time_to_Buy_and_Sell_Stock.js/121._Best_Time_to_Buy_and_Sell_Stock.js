/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let Buy = prices[0];
    let maxProfit = 0;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < Buy) {
            Buy = prices[i];
        } else {
            let Profit = prices[i] - Buy
            if (Profit > maxProfit) {
                maxProfit = Profit;
            }
        }
    }  
    return maxProfit;
};