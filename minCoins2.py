def min_coins(denominations, target_value):
    # Initialize an array to store the minimum number of denominations needed for each value from 0 to target_value
    min_coins_array = [float('inf')] * (target_value + 1)
    min_coins_array[0] = 0  # 0 coins needed to make a sum of 0
    
    # Initialize an array to store the selected coins for each value from 0 to target_value
    coin_selection = [-1] * (target_value + 1)
    
    # Iterate through each coin denomination
    for coin in denominations:
        # Update the min_coins_array array and coin_selection for each value from coin to target_value
        for i in range(coin, target_value + 1):
            # Apply dynamic programming to find the minimum number of coins needed
            if min_coins_array[i - coin] + 1 < min_coins_array[i]:
                coin_selection[i] = coin
            min_coins_array[i] = min(min_coins_array[i - coin] + 1,min_coins_array[i])    
    
    # Initialize the coin sequence with zeros
    coin_sequence = [0] * len(denominations)
    
    # Trace back to find the coin sequence for target_value
    remaining = target_value
    while remaining > 0:
        coin = coin_selection[remaining]
        coin_index = denominations.index(coin)
        coin_sequence[coin_index] += 1
        remaining -= coin
    
    # Return the minimum number of coins needed and which coins are used
    return min_coins_array[target_value], coin_sequence

# Test cases
coins1 = [1, 6, 10]
x1 = 13
result1 = min_coins(coins1, x1)
print("Minimum number of coins needed:", result1[0])
print("Coin sequence:", result1[1])

# Test Case 1:
# Minimum number of coins needed: 3
# Coin sequence: [1, 2, 0]

coins2 = [1, 1930, 2023]
x2 = 1000000
result2 = min_coins(coins2, x2)
print("Minimum number of coins needed:", result2[0])
print("Coin sequence:", result2[1])

# Test Case 2:
# Minimum number of coins needed: 505
# Coin sequence: [10, 15, 480]