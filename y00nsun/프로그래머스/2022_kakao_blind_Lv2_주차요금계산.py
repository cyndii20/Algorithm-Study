# PROGRAMMERS
# 2022 KAKAO BLIND RECRUITMENT
# Lv.2 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

fees = [180, 5000, 10, 600]     # [기본시간, 기본요금, 시간당, 요금]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	

def solution(fees, records):
    parking = set()
    times = dict()
    answers = dict()

    for r in records:
        t, car, state = r.split(" ")
        if car not in times :
            times[car] = 0
                
        if state == "IN":
            parking.add(car)   
            times[car] -= int(t[:2]) * 60 + int(t[3:]) # (-)입차시간
        else :
            parking.remove(car)
            times[car] += int(t[:2]) * 60 + int(t[3:]) # (+)출차시간

    for car in parking:  # 출차 내역 없음
        times[car] += 23 * 60 + 59

    for car in times.keys():   
        if times[car] <= fees[0]:  # 기본 요금
            answers[car] = fees[1]
        else:
            answers[car] = fees[1] + math.ceil((times[car] - fees[0]) / fees[2]) * fees[3]
    
    answers = dict(sorted(answers.items()))
    answer = list(answers.values())
    
    return answer

print(solution(fees, records))
