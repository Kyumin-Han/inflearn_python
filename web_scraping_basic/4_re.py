import re

# abcd, book, desk ...
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ....

p = re.compile("ca.e") 
# . : 하나의 문자를 의미 > care, cafe, case : ok caffe, caabe : NG
# ^ : 문자열의 시작을 의미 (지정된 문자열로 시작하는것)
# $ : 문자열의 끝을 의미 (지정된 문자열로 끝나는 것)

def print_match(m):    
    # print(m.group()) # 매치 되지 않으면 에러가 발생
    if m:
        print("m.group() :", m.group()) # 일치하는 문자열 반환
        print("m.string :", m.string) # 입력된 문자열 반환
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() :", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않았습니다.")

# m = p.match("careless") # 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 정규식 사용하기
# 1. r = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 리스트 형태로 반환

# 원하는 형태
# . : 하나의 문자를 의미 > care, cafe, case : ok caffe, caabe : NG
# ^ : 문자열의 시작을 의미 (지정된 문자열로 시작하는것)
# $ : 문자열의 끝을 의미 (지정된 문자열로 끝나는 것)

