# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입급이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

# def withdraw(balance, money):
#     if balance < money:
#         print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
#         return balance
#     else:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# 기본 값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}세\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age = 17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}세\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")
# profile("조세호", main_lang="자바")

# 키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# 가변 인자
# 받는 인자가 갯수보다 적거나 더 많이 받아야 할때 사용한다
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수와 전역변수
# 지역변수 : 함수에서만 사용 가능한 변수
# 전역변수 : 프로그램 전체에서 사용 가능한 변수

gun = 10

def checkpoint(soldiers):
    global gun # 전역 범위에 있는 gun을 사용한다
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

# global 키워드를 이용해서 전역변수를 사용하면 코드 관리를 하기 어려워지기 때문에
# 인자로 전달받아서 사용하고 return으로 다시 전역 범위로 전달해 준다
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {}".format(gun))