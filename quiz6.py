def std_weight(height, gender):
    if gender == "남자":
        male_bmi = round((height * height) * 22, 2) 
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, male_bmi))
    elif gender == "여자":
        female_bmi = round((height * height) * 21, 2)  
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, female_bmi))
    
std_weight(175 / 100 , "남자")