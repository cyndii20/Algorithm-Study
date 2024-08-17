# PROGRAMMERS
# 2022 KAKAO BLIND RECRUITMENT
# Lv.1 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334


id_list = ["muzi", "frodo", "apeach", "neo"]    # 이용자의 ID
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"] # 각 이용자가 신고한 이용자의 ID 정보
k = 2   # 정지 기준이 되는 신고 횟수

def solution(id_list, report, k):
    answer = []
    report = set(report)    # 중복 제거
    
    answers = {x:0 for x in id_list }   # 이용자 : 결과 메일 수 
    reports = {x:[] for x in id_list }  # 이용자 : 자신을 신고한 이용자들

    for r in report:
        reporter, receiver = r.split(" ")
        reports[receiver].append(reporter)

    for id in reports.keys():
        if len(reports[id]) >= k :
            for reporters in reports[id]:
                answers[reporters] += 1

    answer = list(answers.values())
    return answer

print(solution(id_list, report, k))