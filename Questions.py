# import datetime
# from datetime import date
#
# months = [
#     {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11,
#      "dec": 12}]
# months_obj = 'jan'
#
# from datetime import date
#
# today_date = date.today()
# d2 = today_date.strftime("%m")
# print(d2)
# #
# def calculate_tenure(applicationid):
#     today_date = date.today()
#     d2 = today_date.strftime("%Y-%m-%d")
#     print(d2)
#     month_int = ''
#     for i in months[0].items():
#         if i[0] == months_obj:
#             month_int = i[1]
#     present_month = today_date.month
#     if present_month >= month_int:
#         tenure_date = date(today_date.year + 1, month_int, today_date.day)
#         tenure_date.strftime("%Y-%m-%d")
#         # dob = datetime.datetime.strptime( '%Y-%m-%d')
#         # now = today_date
#         # years = now.year - dob.year
#         months = today_date.month - tenure_date.month
#
# import calendar
#
#
# import calendar
# import datetime
#
#
# def get_month(month_str='Jan'):
#     if month_str:
#         c = {index for index, month in enumerate(calendar.month_abbr) if month == month_str}
#         return list(c)[0]
#
#
# get_month()
# #
# get_month()
#
# from datetime import date
#
# import datetime
# mydate = datetime.datetime.now()
# mydate.strftime("%B")
#
# today_date = date.today()
# c1 = date(2022, 11, 21)
# d2 = c1.strftime("%B")
# print(d2)
# def calculator(age):
#     age = (2022 - int(age))
#     print("You are " + str(age) + " years Old")
#
#
# calculator(input("Type your Birth Year: "))
# from datetime import date
#
# def calculate_age(born):
#     today = date.today()
#     c = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#     print(c)
#
#
#
#
# calculate_age(date(2000, 1, 29))
#
# Figure out your age
# import datetime
#
# currentDate = datetime.datetime.now()
#
# deadline = input('Plz enter your date of birth (mm/dd/yyyy) ')
# deadlineDate = datetime.datetime.strptime(deadline, '%Y/%m/%d')
# print(deadlineDate)
# daysLeft = deadlineDate - currentDate
# print(daysLeft)
#
# years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
# yearsInt = abs(int(years))
#
#  months = (years - yearsInt) * 12
# monthsInt = abs(int(months))
#
# print('You are {0:d} years, {1:d}  months'.format(yearsInt, monthsInt))
#
#
# import datetime
#
# currentDate = datetime.datetime.now()
#
# deadline = input('Plz enter your date of birth (mm/dd/yyyy) ')
# deadlineDate = datetime.datetime.strptime(deadline, '%m/%d/%Y')
# daysLeft = deadlineDate - currentDate
# years = ((daysLeft.total_seconds()) / (365 * 24 * 3600))
# yearsInt = int(years)
# months = (yearsInt - years) * 12
# monthsInt = int(months)
#
# days=(monthsInt-months)*(365/12)
# daysInt=int(days)
#
# hours = (days-daysInt)*24
# hoursInt=int(hours)
#
# minutes = (hours-hoursInt)*60
# minutesInt=int(minutes)
#
# seconds = (minutes-minutesInt)*60
# secondsInt =int(seconds)
#
# print('You are {0:d} years, {1:d}  months, '.format(yearsInt, monthsInt))
#
#
# c = datetime.datetime.now()
# print(c.day)
#
# import datetime
# from dateutil.rrule import rrule, MONTHLY
#
# strt_dt = datetime.date(2001, 1, 1)
# end_dt = datetime.date(2005, 6, 1)
#
# dates = [dt for dt in rrule(MONTHLY, dtstart=strt_dt, until=end_dt)]
#
# from datetime import datetime
# from dateutil import relativedelta
#
# date1 = datetime.strptime('2022-12-01', '%Y-%m-%d')
# date2 = datetime.strptime('2023-05-30', '%Y-%m-%d')
# r = relativedelta.relativedelta(date2, date1)
# z = r.months + (12 * r.years)
# print(z)
#
# a={'code': 200, 'msg': 'success', 'tenure': {}}
# print(a['code'])
# m = {'PAN': 1, 'Patta': 1, 'Aadhar': 2, 'Passbook': 1, 'Passport': 1, 'Voter ID': 2, 'Cheque Book': 1, 'Ration Card': 1,
#      'Applicant Photo': 1, 'Driving Licence': 2, 'Other Documents': 0, 'Account Statement': 1,
#      'Customer Declaration': 1}
# co_app_doc_cat = []
# co_applicant_docu_count = [(2, 'Aadhar', 'POA'), (1, 'Applicant Photo', 'Photo'), (1, 'PAN', 'POI')]
# co_app_doc_cat = []
# doc_coll = {}
# for co_appl in co_applicant_docu_count:
#     co_app_doc_cat.append(co_appl[2])
#     doc_coll.update({co_appl[1]: co_appl[0]})
#     if 'POA' and 'POI' in co_app_doc_cat:
#         for i in m.items():
#             # if co_appl[1] == i[0] and i[1] <= co_appl[0]:
#             #     print("DocPass")
#             if doc_coll.items() == m.items():
#                 print('bye')
# print(doc_coll)
# m_d = {'PAN': 1, 'Patta': 1, 'Aadhar': 2, 'Passbook': 1, 'Passport': 1, 'Voter ID': 2, 'Cheque Book': 1,
#        'Ration Card': 1,
#        'Applicant Photo': 1, 'Driving Licence': 2, 'Other Documents': 0, 'Account Statement': 1,
#        'Customer Declaration': 1}
# co_applicant_docu_count = [(3, 'Aadhar', 'POA'), (2, 'Applicant Photo', 'Photo'), (2, 'PAN', 'POI'), (1, 'Account Statement', 'Bank')]
# new = {}
# for i in co_applicant_docu_count:
#     new.update({i[1]: i[0]})
# shared_items = {k: m_d[k] for k in m_d if k in new and m_d[k] <= new[k]}
# if len(new) == len(shared_items):
#     print("pass")
# else:
#     print("upload required documents")
# print(shared_items)

applicant_doc =[]
doc_result =[]
applicant_doc_count = [(2, 'Aadhar', 'POA'), (2, 'Applicant Photo', 'Photo'), (2, 'Voter ID', 'POI')]

manditory_master_doc = [{'document_name': 'Driving Licence', 'manditory_no_of_pages': 2, 'document_type': 'POI'},
                        {'document_name': 'Driving Licence', 'manditory_no_of_pages': 2, 'document_type': 'POA'},
                        {'document_name': 'Aadhar', 'manditory_no_of_pages': 2, 'document_type': 'POA'},
                        {'document_name': 'Aadhar', 'manditory_no_of_pages': 2, 'document_type': 'POI'},
                        {'document_name': 'Voter ID', 'manditory_no_of_pages': 2, 'document_type': 'POI'},
                        {'document_name': 'Voter ID', 'manditory_no_of_pages': 2, 'document_type': 'POA'},
                        {'document_name': 'PAN', 'manditory_no_of_pages': 1, 'document_type': 'POI'},
                        {'document_name': 'Applicant Photo', 'manditory_no_of_pages': 1, 'document_type': 'Photo'},
                        {'document_name': 'Patta', 'manditory_no_of_pages': 1, 'document_type': 'Land Records'},
                        {'document_name': 'Ration Card', 'manditory_no_of_pages': 1, 'document_type': 'POI'}, {
                            'document_name': 'Ration Card', 'manditory_no_of_pages': 1, 'document_type': 'POA'},
                        {'document_name': 'Account Statement', 'manditory_no_of_pages': 1, 'document_type': 'Bank Records'},
                        {'document_name': 'Passbook', 'manditory_no_of_pages': 1, 'document_type': 'Bank Records'},
                        {'document_name': 'Passport', 'manditory_no_of_pages': 1, 'document_type': 'POI'},
                        {'document_name': 'Passport', 'manditory_no_of_pages': 1, 'document_type': 'POA'},
                        {'document_name': 'Cheque Book', 'manditory_no_of_pages': 1, 'document_type': 'Bank Records'},
                        {'document_name': 'Other Documents', 'manditory_no_of_pages': 0, 'document_type': 'Other Documents'},
                        {'document_name': 'Customer Declaration', 'manditory_no_of_pages': 1, 'document_type': 'Mobile Number Change'}]
for applicant in applicant_doc_count:
    if applicant[2] == 'POA' or applicant[2] == 'POI':
        applicant_doc.append(applicant[2])
if 'POA' and 'POI' in applicant_doc:
    for applicants in applicant_doc_count:
        for k in manditory_master_doc:
            if k['document_type'] == applicants[2] and k['document_name'] == applicants[1] and k['manditory_no_of_pages'] <= applicants[0]:
                doc_result.append(k)
                break
print(doc_result)
