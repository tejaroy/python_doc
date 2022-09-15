# # # def arithmethic_operator(a, b):
# # #     c = int(input('enter any one option[1.+,2.-,3.*,4./]:'))
# # #     d = [[0, 0], [0, 0]]
# # #     if c == 1:
# # #         for i in range(len(a)):
# # #             for j in range(len(b)):
# # #                 d[i][j] = a[i][j] + b[i][j]
# # #         print(d)
# # #     elif c == 2:
# # #         for i in range(len(a)):
# # #             for j in range(len(b)):
# # #                 d[i][j] = a[i][j] - b[i][j]
# # #         print(d)
# # #     elif c == 3:
# # #         for i in range(len(a)):
# # #             for j in range(len(b)):
# # #                 d[i][j] = a[i][j] * b[i][j]
# # #         print(d)
# # #     elif c == 4:
# # #         for i in range(len(a)):
# # #             for j in range(len(b)):
# # #                 d[i][j] = a[i][j] / b[i][j]
# # #         print(d)
# # #     else:
# # #         print('pls enter valid option')
# # #
# # #
# # # arithmethic_operator([[1, 2], [2, 1]], [[2, 1], [3, 5]])
# #
# # # a = [[1, 2], [2, 1]]
# # # print(len(a))
# # # b = [[2, 1], [3, 5]]
# # # print(len(b))
# # # d = [[0, 0], [0, 0]]
# # # for i in range(len(a)):
# # #     for j in range(len(b)):
# # #         d[i][j] = a[i][j] + b[i][j]
# # # print(d)
# #
# # # reverse-a-number
# # # a = [input('enter any value:')]
# # # print(int(a[0][::-1]))
# #
# # #  check whether give number is armstrong number are not
# # # 153 ==> 1^3+5^3+3^3==>1+125+27-->153
# # # a = [input('enter any number:')]
# # # for i in a:
# # #     c = 0
# # #     for j in i:
# # #         d = (int(j)) * int(j) * int(j)
# # #         c = c + d
# # #     if str(c) == i:
# # #         print('It is armstrong number')
# # #     else:
# # #         print('Not armstrong number')
# #
# #
# # # check given number is prime number or not
# # # a = int(input('enter any number:'))
# # # if a % 2 != 0 or a == 2:
# # #     print('it is prime number')
# # # else:
# # #     print('not a prime number')
# #
# #
# # # Fibonacci Series
# # # first, second = 0, 1
# # # a = int(input('eneter any number:'))
# # # b = []
# # # for i in range(a):
# # #     if i <= 1:
# # #         res = i
# # #     else:
# # #         res = first + second
# # #         first = second
# # #         second = res
# # #     b.append(res)
# # # print(b)
# #
# # # sort string in ascending order
# # # sort string in descending order
# # a = input('enter any string:')
# # c = ''
# # for i in sorted(a):
# #     c = c + i
# # print("asc:", c)
# # print('desc:', c[::-1])
#
#
# center_list = [12, 23, 45, 56]
# branch_list = [432, 4321, 213]
# for i in a :
#     for j in b:
#         print(i)
#         i=7
#         j=21
#         if i not in a and j not in b:
#             a.append(i)
#             b.append(j)
#         else:
#             print('no')
# print(a)
# print(b)
# from datetime import date, datetime
#
# # age calculate
# # Python3 code to calculate age in years
#
# from datetime import date
#
#
# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year - (
#             (today.month, today.day) < (birthDate.month, birthDate.day))
#     return age
#
#
# # Driver code
# print(calculateAge(date(2000, 1, 29)), "years")
import datetime
# from datetime import date
#
#
# # def calculate_age(deadlineDate, till_date=None, exist_age=-1):
# #     print('deadlineDate', deadlineDate, 'till_date', till_date)
# #     if till_date:
# #         till_date = till_date.date()
# #         if type(till_date) == datetime.date:
# #             currentDate = datetime.datetime.combine(till_date, datetime.datetime.min.time())
# #         else:
# #             currentDate = till_date
# #     else:
# #         currentDate = datetime.datetime.now()
# #     try:
# #         daysLeft = deadlineDate - currentDate
# #         years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
# #         yearsInt = int(years)
# #
# #         months = (years - yearsInt) * 12
# #         monthsInt = int(months)
# #
# #         days = (months - monthsInt) * (365.242 / 12)
# #         daysInt = int(days)
# #
# #         hours = (days - daysInt) * 24
# #         hoursInt = int(hours)
# #
# #         minutes = (hours - hoursInt) * 60
# #         minutesInt = int(minutes)
# #
# #         seconds = (minutes - minutesInt) * 60
# #         secondsInt = int(seconds)
# #         if abs(monthsInt) > 0 or abs(daysInt) > 0:
# #             age = abs(yearsInt) + 1
# #     except Exception as e:
# #         print(e)
# #         print('Error while calculating age')
# #         age = exist_age
# #
# #     print(age)
#
# def calculate_age_old(born, till_date=None, exist_age=-1):
#     if till_date:
#         today = till_date
#     else:
#         today = date.today()
#     try:
#         age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#         daysLeft = today.year - born.year
#         yearsInt = int(daysLeft)
#         print('years', yearsInt)
#
#         months = (age - yearsInt) * 12
#         monthsInt = int(months)
#         print('months', monthsInt)
#
#         days = (months - monthsInt) * (365.242 / 12)
#         daysInt = int(days)
#         print('days', daysInt)
#     except Exception as e:
#         print(e)
#         age = exist_age
#     print(str(age))
#
#
# calculate_age_old(date(2000, 1, 29))

import datetime
from datetime import date


def ageCalculator(year, month, dat):
    today = date.today()
    dob = datetime.date(year, month, dat)
    # calculate year
    years = ((today - dob).total_seconds() / (365.242 * 24 * 3600))
    yearsInt = int(years)

    # calculate month
    months = (years - yearsInt) * 12
    monthsInt = int(months)

    # calculate day
    days = (months - monthsInt) * (365.242 / 12)
    daysInt = int(days)
    partner = input('enter your product:-')
    try:
        if partner == 'DCB':
            if monthsInt >= 6 and daysInt >= 1:
                print(yearsInt + 1)
                monthsInt, daysInt = 0, 0
                print('You are {0} years, {1} months, {2} days old.'.format(yearsInt+1, monthsInt, daysInt))

            else:
                print('You are {0} years, {1} months, {2} days old.'.format(yearsInt, monthsInt, daysInt))
        else:
            if partner == 'Samunathi' or 'Agriwise' or 'DER':
                if monthsInt >= 12 and daysInt >= 1:
                    monthsInt, daysInt = 0, 0
                    print('You are {0} years, {1} months, {2} days old.'.format(yearsInt+1, monthsInt, daysInt))
                else:
                    print('You are {0} years, {1} months, {2} days old.'.format(yearsInt, monthsInt, daysInt))
    except Exception as e:
        print(e)


ageCalculator(2000, 1, 29)
