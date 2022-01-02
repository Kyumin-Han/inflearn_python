site = "http://github.com"

word = site.replace("http://", "")

word = word[:word.index(".")]

password = word[:3] + str(len(word)) + str(word.count("e")) + "!"

print(f"{site}의 비밀번호는 {password}입니다.")