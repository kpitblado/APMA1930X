function [minCoins, coinSequence] = minCoins(coins, x)
    numCoins = length(coins);
    
    % Create an array to store the minimum number of coins needed for each value from 0 to x
    dp = inf(1, x + 1);
    dp(1) = 0;  % 0 coins needed to make a sum of 0
    
    % Create an array to store the selected coins for each value from 0 to x
    coinSelection = zeros(numCoins, x + 1);
    
    % Iterate through each coin denomination
    for coinIdx = 1:numCoins
        coin = coins(coinIdx);
        
        % Update the dp array and coinSelection for each value from coin to x
        for i = coin:x
            if dp(i - coin + 1) + 1 < dp(i + 1)
                dp(i + 1) = dp(i - coin + 1) + 1;
                coinSelection(coinIdx, i + 1) = coin;
            end
        end
    end
    
    % Initialize the coin sequence with zeros
    coinSequence = zeros(1, numCoins);
    
    % Trace back to find the coin sequence for x
    remaining = x;
    while remaining > 0
        coinIdx = find(coins == coinSelection(:, remaining + 1));
        coinSequence(coinIdx) = coinSequence(coinIdx) + 1;
        remaining = remaining - coins(coinIdx);
    end
    
    % The value in dp(x+1) will contain the minimum number of coins needed to make the sum x
    minCoins = dp(x + 1);
end




