month = int(input())

thirty = 30
thirty_one = 31

months = [i for i in range(1, 13)]

days = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_day = { k:v for k, v in zip(months, days) }

try:
    for i in range(month_day[month]):
        text_file = open("{}월.txt".format(month), "a", encoding="utf8")
        text_file.write("%2d-%2d\n" % (month, i+1))
    text_file.close()
except Exception as err:
    print(err)

# for i in range(1, 51):
#     report_file = open("{}주차.txt".format(i), "w", encoding="utf8")
#     report_file.write("- {} 주차 주간보고 -".format(i))
#     report_file.write("\n부서 : ")
#     report_file.write("\n이름 : ")
#     report_file.write("\n업무 요약 : ")
# report_file.close()
