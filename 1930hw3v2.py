def find_path_and_v_val(p, optimal_strategy, original_value_matrix):
    # get q value
    q = 1-p
    # start from second last row since we need values from the row below
    for r in range(len(original_value_matrix) - 2, -1, -1):
        for c in range(len(original_value_matrix[r])):
            # calcualte expected value
            print(str(r) + ", "+ str(c))
            expected_value = (
                q * original_value_matrix[r+1][c]) + (p * original_value_matrix[r+1][c+1])
            # see if we can do better
            best_value = max(original_value_matrix[r][c], expected_value)
            print(best_value)
            # we cannot do better so stop
            if best_value == original_value_matrix[r][c]:
                optimal_strategy[r][c] = str(1)
            else:
                optimal_strategy[r][c] = str(0)
            # update v value at this point to the best possible value
            original_value_matrix[r][c] = best_value

    print("v = ", original_value_matrix[0][0])
    for i in range(len(optimal_strategy)):
        print("n = ", i, " ", optimal_strategy[i])


def find_duck_walk_vals(n, change_fucntion):
    # find the initial values for the matrix by doing a duck walk
    duck_walk_res = []
    cur_value_row = [0]
    for _ in range(n+1):
        value_lst = []
        next_path = set()
        cur_value_row = sorted(cur_value_row)
        for val in cur_value_row:
            value_lst.append(change_fucntion(val))
            next_path.add(val + 1)
            next_path.add(val - 1)
        duck_walk_res.append(value_lst)
        cur_value_row = list(next_path)
    return duck_walk_res


def main():
    n = 10
    p = 0.4
    optimal_strategy = []
    # initilaize the optimal path 2d array
    for i in range(n+1):
        col_lst = []
        for _ in range(n+1):
            if i == n:
                col_lst.append(str(1))
            else:
                col_lst.append("*")
        optimal_strategy.append(col_lst)
    # find the initial duck walk values
    original_value_matrix = find_duck_walk_vals(n, square_value)
    print(optimal_strategy)
    find_path_and_v_val(p, optimal_strategy, original_value_matrix)


def return_value(val):
    return val


def square_value(val):
    return val**2


if __name__ == "__main__":
    main()
