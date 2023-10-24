% Parameters
p = 0.4;
N = 10;

% Define the function f(x)
f = @(x) x^2;

% Create a matrix to store the optimal stopping strategy
matrix_size = N + 1;
strategy_matrix = zeros(matrix_size, matrix_size);

% Fill in the strategy matrix and compute the value of v
v = zeros(1, matrix_size);
for n = N : -1 : 1
    for state = -n : 2 : n
        % Calculate the expected value of f(S_tau) if we stop at time n and state S_n
        stop_value = f(state);
        % Calculate the expected value of f(S_tau) if we continue at time n and state S_n
        continue_value = p * v(n + state + 1) + (1 - p) * v(n - state + 1);

        if stop_value >= continue_value
            strategy_matrix(n + 1, state + n + 1) = 1;  % Stop
            v(n + 1) = stop_value;
        else
            strategy_matrix(n + 1, state + n + 1) = 0;  % Continue
            v(n + 1) = continue_value;
        end
    end
end

% Output the value of v
disp(['The value of v is: ' num2str(v(1))]);

% Output the optimal stopping strategy matrix
disp('Optimal stopping strategy:');
for n = 0 : N
    disp(['n = ' num2str(n) ' ' num2str(strategy_matrix(n + 1, :))]);
end