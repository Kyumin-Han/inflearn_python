for i in range(1, 51):
    report_file = open("{}주차.txt".format(i), "w", encoding="utf8")
    report_file.write("- {} 주차 주간보고 -".format(i))
    report_file.write("\n부서 : ")
    report_file.write("\n이름 : ")
    report_file.write("\n업무 요약 : ")
report_file.close()
