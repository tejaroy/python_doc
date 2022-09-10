# def arithmethic_operator(a, b):
#     c = int(input('enter any one option[1.+,2.-,3.*,4./]:'))
#     d = [[0, 0], [0, 0]]
#     if c == 1:
#         for i in range(len(a)):
#             for j in range(len(b)):
#                 d[i][j] = a[i][j] + b[i][j]
#         print(d)
#     elif c == 2:
#         for i in range(len(a)):
#             for j in range(len(b)):
#                 d[i][j] = a[i][j] - b[i][j]
#         print(d)
#     elif c == 3:
#         for i in range(len(a)):
#             for j in range(len(b)):
#                 d[i][j] = a[i][j] * b[i][j]
#         print(d)
#     elif c == 4:
#         for i in range(len(a)):
#             for j in range(len(b)):
#                 d[i][j] = a[i][j] / b[i][j]
#         print(d)
#     else:
#         print('pls enter valid option')
#
#
# arithmethic_operator([[1, 2], [2, 1]], [[2, 1], [3, 5]])

# a = [[1, 2], [2, 1]]
# print(len(a))
# b = [[2, 1], [3, 5]]
# print(len(b))
# d = [[0, 0], [0, 0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         d[i][j] = a[i][j] + b[i][j]
# print(d)

# reverse-a-number
# a = [input('enter any value:')]
# print(int(a[0][::-1]))

#  check whether give number is armstrong number are not
# 153 ==> 1^3+5^3+3^3==>1+125+27-->153
# a = [input('enter any number:')]
# for i in a:
#     c = 0
#     for j in i:
#         d = (int(j)) * int(j) * int(j)
#         c = c + d
#     if str(c) == i:
#         print('It is armstrong number')
#     else:
#         print('Not armstrong number')


# check given number is prime number or not
# a = int(input('enter any number:'))
# if a % 2 != 0 or a == 2:
#     print('it is prime number')
# else:
#     print('not a prime number')


# Fibonacci Series
# first, second = 0, 1
# a = int(input('eneter any number:'))
# b = []
# for i in range(a):
#     if i <= 1:
#         res = i
#     else:
#         res = first + second
#         first = second
#         second = res
#     b.append(res)
# print(b)

# sort string in ascending order
# sort string in descending order
a = input('enter any string:')
c = ''
for i in sorted(a):
    c = c + i
print("asc:", c)
print('desc:', c[::-1])



