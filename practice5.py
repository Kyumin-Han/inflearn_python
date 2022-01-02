# 표준입출력

# 표준 출력
import sys
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요")

# print("Python", "Java", file=sys.stdout) # 일반적인 출력
# print("Python", "Java", file=sys.stderr) # err발생시의 출력

# 출력 form
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 1001):
#     print("대기번호 : " + str(num).zfill(3))

# 표준 입력
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다. ")

# 다양한 출력 포맷
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_<10}".format(500))
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))
print("{0:^<+30,}".format(10000000000000))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))