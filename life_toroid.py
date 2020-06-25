import copy


def actual_row(row_no, rows):
    return row_no % rows


def actual_col(col_no, cols):
    return col_no % cols


def neighbour_sum(arr, i, j, rows, cols):
    s = 0
    for l in range(-1, 2):
        for k in range(-1, 2):
            s += int(arr[actual_row(i + k, rows)][actual_col(j + l, cols)])
    return s - int(arr[i][j])


def replace_in_str(s, place, replacement):
    if place == 0:
        return replacement + s[1:]
    elif place == len(s) - 1:
        return s[:-1] + replacement
    return s[:place] + replacement + s[place + 1:]


def update(prev, rows, cols):
    new = copy.copy(prev)
    for i in range(rows):
        for j in range(cols):
            if neighbour_sum(prev, i, j, rows, cols) == 3 and prev[i][j] == '0':
                new[i] = replace_in_str(new[i], j, '1')
            if prev[i][j] == '1' and not (2 <= neighbour_sum(prev, i, j, rows, cols) <= 3):
                new[i] = replace_in_str(new[i], j, '0')
    return new


def final(input_arr, rows, cols, iterations):
    prev = input_arr
    for i in range(iterations):
        prev = update(prev, rows, cols)
    return prev


def print_pattern(arr):
    for i in range(len(arr)):
        print(arr[i])


A = ['0' * 10, '0' * 3 + '11' + '0' * 5, '0' * 4 + '1' + '0' * 5, '0' * 10, '0' * 10, '0' * 3 + '11' + '0' * 5,
     '0011' + '0' * 6, '0' * 5 + '10000', '00001' + '0' * 5, '0' * 10]
print_pattern(A)
print('')
print_pattern(final(A, 10, 10, 1))
