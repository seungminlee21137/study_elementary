import csv
import random

def generate_math_questions(target_count=2000):
    questions = []
    
    while len(questions) < target_count:
        case_type = random.randint(1, 4)
        num1, num2 = 0, 0
        operator = ""
        
        # ----------------------------------
        # Case 1: 2자리 - 1자리 (예: 23 - 5)
        # ----------------------------------
        if case_type == 1:
            num1 = random.randint(10, 99)
            num2 = random.randint(1, 9)
            operator = "-"
            if num1 < num2: num1, num2 = num2, num1

        # ----------------------------------
        # Case 2: 2자리 + 1자리 (예: 45 + 7)
        # ----------------------------------
        elif case_type == 2:
            num1 = random.randint(10, 99)
            num2 = random.randint(1, 9)
            operator = "+"

        # ----------------------------------
        # Case 3: 2자리 - 2자리 (예: 81 - 40)
        # ----------------------------------
        elif case_type == 3:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            operator = "-"
            # 뺄셈은 큰 수에서 작은 수를 빼도록 정렬
            if num1 < num2: num1, num2 = num2, num1

        # ----------------------------------
        # Case 4: 2자리 + 2자리 (예: 34 + 25)
        # ----------------------------------
        elif case_type == 4:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            operator = "+"

        # ----------------------------------
        # [정답 계산 및 검산]
        # ----------------------------------
        if operator == "+":
            answer = num1 + num2
        else:
            answer = num1 - num2
            
        # 질문 텍스트 생성
        q_text = f"{num1} {operator} {num2} = ?"

        # ★ 안전장치: 파이썬 eval 함수로 질문 텍스트를 실제 계산해서 검증
        # 문자열 "81 - 40"을 계산기에 넣어 41이 나오는지 확인
        calc_check = eval(f"{num1} {operator} {num2}")
        if calc_check != answer:
            print(f"오류 발견! 폐기: {q_text} (계산값:{calc_check} != 변수값:{answer})")
            continue # 이 문제는 버리고 다시 생성

        # ----------------------------------
        # [오답 보기 생성] (정답과 겹치지 않게)
        # ----------------------------------
        wrong_set = set()
        
        while len(wrong_set) < 3:
            # 오답 패턴: 정답에서 -10, +10, -1, +1, 랜덤오차
            offset = random.choice([-10, 10, -1, 1, random.randint(-5, 5)])
            wrong_val = answer + offset
            
            # 오답 조건: 
            # 1. 정답과 달라야 함
            # 2. 결과가 0보다 커야 함 (초등 2학년 수준)
            # 3. 이미 뽑은 오답과 겹치면 안 됨 (set이 처리)
            if wrong_val != answer and wrong_val >= 0:
                wrong_set.add(wrong_val)
        
        wrongs = list(wrong_set)
        random.shuffle(wrongs)

        # 문제 저장
        questions.append({
            "q": q_text,
            "a": str(answer),
            "w1": str(wrongs[0]),
            "w2": str(wrongs[1]),
            "w3": str(wrongs[2])
        })

    return questions[:target_count]

# ==========================================
# 파일 저장
# ==========================================
final_data = generate_math_questions(2000)
filename = "2학년_수학_문제은행.csv"

with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "grade", "subject", "q", "a", "w1", "w2", "w3"])
    
    for idx, item in enumerate(final_data, 1):
        writer.writerow([
            3000 + idx, "2", "math",
            item["q"], item["a"], 
            item["w1"], item["w2"], item["w3"]
        ])

print(f"=========================================")
print(f"'{filename}' 생성 완료!")
print(f"검산 기능을 통과한 무결점 수학 문제 {len(final_data)}개")
print(f"=========================================")