from random import *

count = 0
for i in range(1, 51):
    drive_time = randint(5, 50)
    if 5 <= drive_time and drive_time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, drive_time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, drive_time))

print("총 탑승 승객 : {}분".format(count))