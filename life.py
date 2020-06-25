import copy


def neighbour_sum(arr, i, j, rows, cols):
    s = 0
    for l in range(-1, 2):
        for k in range(-1, 2):
            if 0 <= i + k < rows and 0 <= j + l < cols:
                s += int(arr[i + k][j + l])
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
            if prev[i][j] == '1' and (0 <= neighbour_sum(prev, i, j, rows, cols) <= 1  or 4 <= neighbour_sum(prev, i, j, rows, cols) <= 8):
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
B = ['000', '111', '000']

#print_pattern(final(B, 3, 3, 1))
print_pattern(A)
print('')
print_pattern(final(A, 10, 10, 5))