# 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
for waiting_no in range(1, 6): # range(5) 0~4까지의 범위, range(1, 6) 1~5까지의 범위
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "그루트"]

for customer in starbucks:
    print("{}, 커피가 준비되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기되었습니다.")

# 무한루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# 조건이 만족할때까지 루프를 돈다
customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# continue/break
absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한줄 for문
students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)

# 문자열을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)

# 문자열을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)