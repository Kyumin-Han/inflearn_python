print(5)
print(-10)
# 실수값도 출력 가능
print(3.14)
print(1000)
# print 함수 안에서 자료형이 같을 경우 연산도 가능하다
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('string')
print("double quote")
# 같은 문자열을 반복하는 경우
print("ㅋ"*9)

# boolean True/False
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not(5 > 10))

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
# 이름이 바뀌는 경우 이름이 사용된 문장을 통째로 변경해야 한다
# 변수를 선언하고 그 변수를 사용해서 전체를 바꿀 필요 없이 해당 변수만 변경해 주면 된다

'''
여러
문장
주석
처리
'''

# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3
print(5%3) # 나머지 구하기
print(10%3)

print(5//3) # 몫 구하기
print(10//3)

print(10 > 3) # 비교 연산자
print(4 >= 7)

print(3 == 3) # 동등 연산자 boolean값 반환
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3) # 같지 않다
print(not (1 != 3))

# and or 연산자
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3) # 여러 항에 동시에 사용할 수 있다

# 숫자 함수
print(abs(-5)) # 절댓값
print(pow(4, 2)) # pow(x, y) x의 y제곱
print(max(5, 12)) # 인수 중 최댓값
print(min(5, 12)) # 인수 중 최솟값
print(round(3.14)) # 반올림
print(round(4.99))

# math 라이브러리 import 해서 사용
from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근 구하기

# random 라이브러리
from random import *

print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 1 이상 10 미만의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 값 생성
print(int(random() * 45) + 1) # 1 이상 45 이하의 값 생성

print(randrange(1, 46)) # 1 부터 45 이하의 값 생성
print(randrange(1, 46)) # 1 부터 45 이하의 값 생성
print(randrange(1, 46)) # 1 부터 45 이하의 값 생성
print(randrange(1, 46)) # 1 부터 45 이하의 값 생성
print(randrange(1, 46)) # 1 부터 45 이하의 값 생성
print(randrange(1, 46)) # 1 부터 45 이하의 값 생성

print(randint(1, 45)) # 1 부터 45 이하의 값 생성

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
# 여러줄의 문장 받기
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# slicing
# 문자열에서 필요한 정보만 가져오는 것
jumin = "980430-1234567"

print("성별 : " + jumin[7])
# 범위를 지정해서 시작 숫자 자리부터 끝 자리 직전까지 문자를 가져온다
print("생년 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 지정 위치 직전까지 문자를 가져온다
print("뒤 7자리 : " + jumin[7:]) # 시작 위치부터 끝까지 문자를 가져온다
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 뒤에서부터의 인덱스는 -1부터 시작한다

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # lower() 모든 문자를 소문자로
print(python.upper()) # upper() 모든 문자를 대문자로
print(python[0].isupper()) #isupper() 해당 문자가 대문자인지 boolean 값 리턴
print(len(python)) # len() 해당 문자열의 길이 출력
print(python.replace("Python", "Java")) # replace() 해당 문자를 찾아 대체

index = python.index("n") # 해당 글자가 있는 index를 알 수 있다
print(index)
index = python.index("n", index + 1) # 지정 위치 이후에 몇번째 자리에 있는지를 반환
print(index)

print(python.find("n")) # index와 같이 해당 글자의 위치 반환, 해당 글자가 문자열에 없을 경우에는 -1 반환
# print(python.index("Java")) -> 원하는 값이 없을 때는 오류가 난다

print(python.count("n")) # 문자열에서 해당 문자가 몇번 나왔는지 출력

# 문자열 포맷
print("a", "b")
# 방법 1
print("나는 %d살입니다" % 20) # %d 정수값을 대입한다
print("나는 %s을 좋아해요." % "파이썬") # %s 문자열을 대입한다
print("Apple은 %c로 시작해요." % "A") # %c 문자 1개를 대입한다
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러개의 값을 대입하고 싶을때는 괄호로 묶어서 순서대로 적어준다

# 방법 2
print("나는 {}살입니다.".format(20)) # {}에 format의 괄호에 있는 값이 대입된다
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# 중괄호안에 숫자를 넣으면 그 숫자 번째의 값이 괄호에 들어간다

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# 중괄호 안에 변수처럼 사용할 수 있다

# 방법 4(v.3.6 이상만 사용 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
print("백문이 불여일견 \n백견이 불여일타") # \n : 줄바꿈
print("저는 \"나도코딩\" 입니다") # \" : 큰 따옴표
print("C:\\Users\\4rbal\\Desktop\\inflearn\\python") # \\ : 문장내에서 역슬래시 한개
print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동
print("Redd\bApple") # \b : 백스페이스(한글자 삭제)
print("Red\tApple")

# 리스트 [] 배열

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

# 리스트 끝에 데이터 추가
subway.append("하하")
print(subway)

# 리스트 중간에 데이터 추가
subway.insert(1, "정형돈" )
print(subway)

# 리스트에서 데이터 제거(뒤에서부터)
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 데이터가 몇개가 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬하가
num_list = [5, 2, 4, 1, 3]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 리스트 비우기
# num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 딕셔너리
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 대괄호로 접근 했을 때는 키값이 없으면 그대로 프로그램을 종료시킨다

print(cabinet.get(5)) # get 함수를 이용해서 접근 했을때 키 값이 없으면 None을 출력하고 그대로 코드는 진행된다
print(cabinet.get(5, "사용가능"))
# get 함수를 통해 없는 값에 접근 할 때 None 값이 아닌 기본값을 설정해 줄 수 있다
print("hi")

# 딕셔너리 안에 키값이 있는지 확인하기
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
# string형 키 값도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 딕셔너리에 새 값을 넣기
print(cabinet)
cabinet["A-3"] = "김종국"
# 이미 있는 키 값일 경우 그 값은 업데이트된다
cabinet["C-20"] = "조세호"
# 새 키 값을 할당해 준 경우 해당 딕셔너리에 키와 값이 저장된다
print(cabinet)

# 딕셔너리에서 값을 빼기
del cabinet["A-3"]
print(cabinet)

# 키값만 출력
print(cabinet.keys())

# 밸류 값만 출력
print(cabinet.values())

# 키와 밸류의 쌍으로 출력
print(cabinet.items())

# 딕셔너리 지우기
cabinet.clear()
print(cabinet)

# 튜플
menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")
# 값을 추가하거나 삭제할 수 없다

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)

# set(집합)
# 중복이 안되고, 순서가 없는 것
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "박명수"])
# 교집합 구하기
print(java & python)
print(java.intersection(python))

# 합집합 구하기
print(java | python)
print(java.union(python))

# 차집합 구하기
print(java - python)
print(java.difference(python))

# set에 추가
python.add("김태호")
print(python)

# set에서 제거
java.remove("김태호")
print(java)

# 자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

