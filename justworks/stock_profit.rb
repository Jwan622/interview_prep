## get the max profit for the day. This is a good example of the greedy algorithm.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]   #max price should be 6
# stock_prices_yesterday = [14,12,8,2]   # max price should be -2

def get_max_profit(stock_prices_yesterday)
  min_price = stock_prices_yesterday[0]   # starting price
  max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]   # starting profit

  if stock_prices_yesterday.length < 2
    throw IndexError, "Stock prices need to contain at least 2 prices."
  end

  stock_prices_yesterday[1..-1].each do |current_price|
    potential_profit = current_price - min_price

    max_profit = [potential_profit, max_profit].max

    min_price = [min_price, current_price].min
  end
  max_profit
end

p get_max_profit(stock_prices_yesterday)

#
# =begin
# stock_prices = [70,23,100,34,12,55,8,90,66,2,56,65]
# In the array above, the prices above are in time-sequential order. Write a method that will
# find the highest possible profit, you don't need the indices or actual prices...just have the method
# return the highest possible profit. What is profit? Well it's buy - sell.
# Note that if you were to pick two numbers to buy and sell, the buy needs to come first.
# For example, you can buy 12 and sell 55 for a profit of +43 but you cannot buy 23 and sell 70 since
# that is moving backwards in time. You also cannot buy 2 and sell 100 since that is also moving backwards in
# time. Find the n^2 solution and the n solution.
# =end
# gem 'pry'
#
# # N^2 solution
# stock_prices = [70,23,100,34,12,55,8,90,66,2,56,65]
# x = stock_prices.flat_map.with_index do |buy,i|    # we need the flat map because the inner array returns an array of hashes. You should use flat_map instead of map if you have an inner map
#   stock_prices[(i+1)..-1].map do |sell|
#     {:buy => buy, :sell => sell, :profit => sell - buy}   # so the inner map returns an array of hashes.
#   end
# end
#
# y= x.max_by { |h| h[:profit] }
# puts y
#
# # N solution by Horace
# def profit(spread)
#   -spread.reduce(:-)
# end
#
# def best_profit(prices)
#   buy,sell,*prices = prices
#   best_spread = [buy,sell]
#   prices.each do |p|
#     if p < buy
#       buy = p
#     elsif profit([buy, p]) > profit(best_spread)
#       best_spread = [buy, p]
#     end
#   end
#   profit(best_spread)
# end
#
# best_profit([70,23,34,12,55,8,90,66,56,65])
#
# # My N solution
# class StockPrices
#   attr_reader :stock_prices
#
#   def initialize(stock_prices)
#     @stock_prices = stock_prices
#   end
#
#   def calc
#     current_buy = stock_prices[0]
#     max_profit = 0
#     stock_prices.each_with_index do |sell_price, index|
#       if sell_price < current_buy
#         current_buy = sell_price
#       elsif sell_price - current_buy > max_profit
#         max_profit = sell_price - current_buy
#       end
#     end
#     return max_profit
#   end
# end
# s = StockPrices.new([70,23,34,12,55,8,90,66,56,65])
# puts "The max profit of the array using this calc method is #{s.calc}"
#
# =begin
# I think the trick here is figuring out the best possible solution step by step.
# Start by thinking if there's an n solution
# you got the n^2 solution but is there an n solution?
# Iterate and think:
# 1. Well start with the first number. Then take the second number, what's the profit. It's
# the sell number (the second one) - the buy number (the first one). Iterate through the remainder of the array
# if that new number is < the buy, then update the buy to the new number since the lower of the two numbers will
# yield the highest profit with the remainder of the array. the iteration of the remainder if the array represents the
# sell number.
# =end
