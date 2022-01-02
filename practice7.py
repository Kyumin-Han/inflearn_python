# pickle => 프로그램 상에서 사용하는 데이터를 파일 형태로 저장해주는 것

import pickle
# pickle로 데이터 내보내기
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장한다
# profile_file.close()

# pickle에서 데이터 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()