def arithmethic_operator(a, b):
    c = int(input('enter any one option[1.+,2.-,3.*,4./]:'))
    d = [[0, 0], [0, 0]]
    if c == 1:
        for i in range(len(a)):
            for j in range(len(b)):
                d[i][j] = a[i][j] + b[i][j]
        print(d)
    elif c == 2:
        for i in range(len(a)):
            for j in range(len(b)):
                d[i][j] = a[i][j] - b[i][j]
        print(d)
    elif c == 3:
        for i in range(len(a)):
            for j in range(len(b)):
                d[i][j] = a[i][j] * b[i][j]
        print(d)
    elif c == 4:
        for i in range(len(a)):
            for j in range(len(b)):
                d[i][j] = a[i][j] / b[i][j]
        print(d)
    else:
        print('pls enter valid option')
arithmethic_operator([[1, 2], [2, 1]], [[2, 1], [3, 5]])

# a = [[1, 2], [2, 1]]
# print(len(a))
# b = [[2, 1], [3, 5]]
# print(len(b))
# d = [[0, 0], [0, 0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         d[i][j] = a[i][j] + b[i][j]
# print(d)
