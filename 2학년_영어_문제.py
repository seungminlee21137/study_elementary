import csv
import random

# ==========================================
# 1. 2학년 영어 어휘 & 문장 데이터베이스
# ==========================================
vocab_db = [
    # [Animals - 동물]
    {"eng": "Cat", "kor": "고양이", "wrong": ["개", "돼지", "소"], "type": "word"},
    {"eng": "Dog", "kor": "강아지", "wrong": ["고양이", "새", "물고기"], "type": "word"},
    {"eng": "Pig", "kor": "돼지", "wrong": ["곰", "사자", "호랑이"], "type": "word"},
    {"eng": "Cow", "kor": "소", "wrong": ["말", "양", "염소"], "type": "word"},
    {"eng": "Lion", "kor": "사자", "wrong": ["호랑이", "원숭이", "기린"], "type": "word"},
    {"eng": "Tiger", "kor": "호랑이", "wrong": ["사자", "늑대", "여우"], "type": "word"},
    {"eng": "Monkey", "kor": "원숭이", "wrong": ["코끼리", "토끼", "다람쥐"], "type": "word"},
    {"eng": "Bird", "kor": "새", "wrong": ["물고기", "나비", "벌"], "type": "word"},
    {"eng": "Fish", "kor": "물고기", "wrong": ["새", "개구리", "거북이"], "type": "word"},
    {"eng": "Bear", "kor": "곰", "wrong": ["사슴", "말", "양"], "type": "word"},

    # [Colors - 색깔]
    {"eng": "Red", "kor": "빨간색", "wrong": ["파란색", "노란색", "초록색"], "type": "word"},
    {"eng": "Blue", "kor": "파란색", "wrong": ["빨간색", "검은색", "흰색"], "type": "word"},
    {"eng": "Yellow", "kor": "노란색", "wrong": ["보라색", "분홍색", "주황색"], "type": "word"},
    {"eng": "Green", "kor": "초록색", "wrong": ["빨간색", "갈색", "회색"], "type": "word"},
    {"eng": "Black", "kor": "검은색", "wrong": ["흰색", "빨간색", "파란색"], "type": "word"},
    {"eng": "White", "kor": "흰색", "wrong": ["검은색", "노란색", "초록색"], "type": "word"},
    
    # [Family - 가족]
    {"eng": "Mom", "kor": "엄마", "wrong": ["아빠", "할머니", "언니"], "type": "word"},
    {"eng": "Dad", "kor": "아빠", "wrong": ["엄마", "할아버지", "오빠"], "type": "word"},
    {"eng": "Brother", "kor": "남자 형제", "wrong": ["여자 형제", "엄마", "아빠"], "type": "word"},
    {"eng": "Sister", "kor": "여자 형제", "wrong": ["남자 형제", "할머니", "삼촌"], "type": "word"},
    {"eng": "Grandma", "kor": "할머니", "wrong": ["할아버지", "엄마", "이모"], "type": "word"},
    {"eng": "Grandpa", "kor": "할아버지", "wrong": ["할머니", "아빠", "삼촌"], "type": "word"},

    # [Body - 신체]
    {"eng": "Eye", "kor": "눈", "wrong": ["코", "입", "귀"], "type": "word"},
    {"eng": "Nose", "kor": "코", "wrong": ["눈", "입", "손"], "type": "word"},
    {"eng": "Mouth", "kor": "입", "wrong": ["귀", "머리", "발"], "type": "word"},
    {"eng": "Ear", "kor": "귀", "wrong": ["눈", "코", "입"], "type": "word"},
    {"eng": "Hand", "kor": "손", "wrong": ["발", "다리", "팔"], "type": "word"},
    {"eng": "Foot", "kor": "발", "wrong": ["손", "머리", "어깨"], "type": "word"},

    # [Sentences - 문장 & 회화]
    {"sent": "What is your ____?", "ans": "name", "wrong": ["game", "same", "lame"], "kor": "이름이 뭐니?"},
    {"sent": "How ____ you?", "ans": "are", "wrong": ["is", "am", "do"], "kor": "기분이 어때? / 안녕?"},
    {"sent": "I ____ happy.", "ans": "am", "wrong": ["is", "are", "be"], "kor": "나는 행복해."},
    {"sent": "Good ____.", "ans": "morning", "wrong": ["night", "bye", "hello"], "kor": "좋은 아침이야."},
    {"sent": "Nice to ____ you.", "ans": "meet", "wrong": ["meat", "feet", "see"], "kor": "만나서 반가워."},
    {"sent": "____ is a cat.", "ans": "It", "wrong": ["I", "You", "We"], "kor": "그것은 고양이야."},
    {"sent": "I like ____.", "ans": "pizza", "wrong": ["book", "desk", "pen"], "kor": "나는 피자를 좋아해."},
    {"sent": "See you ____.", "ans": "later", "wrong": ["water", "letter", "hater"], "kor": "나중에 봐."},
    {"sent": "Thank ____.", "ans": "you", "wrong": ["me", "he", "she"], "kor": "고마워."},
    {"sent": "Open the ____.", "ans": "door", "wrong": ["floor", "sky", "apple"], "kor": "문을 열어."}
]

# ==========================================
# 2. 문제 생성 로직 (4가지 유형)
# ==========================================
def generate_english_questions(target_count=2000):
    questions = []
    
    # 단어(Word) 리스트와 문장(Sentence) 리스트 분리
    word_items = [item for item in vocab_db if "type" in item]
    sent_items = [item for item in vocab_db if "sent" in item]

    while len(questions) < target_count:
        # 유형 랜덤 선택 (1: 영->한, 2: 한->영, 3: 문장 빈칸, 4: 철자 고르기)
        q_type = random.randint(1, 4)
        
        # ----------------------------------
        # Type 1: 영어 단어 -> 한글 뜻 (Apple 뜻은?)
        # ----------------------------------
        if q_type == 1:
            item = random.choice(word_items)
            
            # 오답 생성: DB에 있는 다른 단어의 뜻을 가져옴
            other_kors = [w['kor'] for w in word_items if w['kor'] != item['kor']]
            distractors = random.sample(other_kors, 3)
            
            questions.append({
                "q": f"다음 영어 단어의 뜻은 무엇일까요? '{item['eng']}'",
                "a": item['kor'],
                "w1": distractors[0],
                "w2": distractors[1],
                "w3": distractors[2]
            })

        # ----------------------------------
        # Type 2: 한글 뜻 -> 영어 단어 ('사과'는 영어로?)
        # ----------------------------------
        elif q_type == 2:
            item = random.choice(word_items)
            
            # 오답 생성: DB에 있는 다른 영어 단어를 가져옴
            other_engs = [w['eng'] for w in word_items if w['eng'] != item['eng']]
            distractors = random.sample(other_engs, 3)
            
            questions.append({
                "q": f"'{item['kor']}'(은)는 영어로 무엇일까요?",
                "a": item['eng'],
                "w1": distractors[0],
                "w2": distractors[1],
                "w3": distractors[2]
            })

        # ----------------------------------
        # Type 3: 문장 빈칸 채우기 (회화)
        # ----------------------------------
        elif q_type == 3:
            item = random.choice(sent_items)
            wrongs = item['wrong']
            random.shuffle(wrongs)
            
            questions.append({
                "q": f"빈칸에 알맞은 말은? '{item['sent']}' ({item['kor']})",
                "a": item['ans'],
                "w1": wrongs[0],
                "w2": wrongs[1],
                "w3": wrongs[2]
            })

        # ----------------------------------
        # Type 4: 올바른 철자 찾기 (Spelling)
        # ----------------------------------
        elif q_type == 4:
            item = random.choice(word_items)
            word = item['eng']
            
            # 간단한 철자 오답 만들기 (철자 하나 바꾸거나 빼기)
            # 예: Lion -> Loin, Lon, Laon
            wrong_spellings = []
            if len(word) > 2:
                w1 = word[:-1]  # 끝글자 뺌
                w2 = word[0] + word[2:] + word[1] if len(word)>2 else word+"s" # 순서 바꿈
                w3 = word + "e" # 뒤에 e 붙임
                wrong_spellings = [w1, w2, w3]
            else:
                wrong_spellings = [word+"s", "a"+word, word+"e"]
            
            questions.append({
                "q": f"'{item['kor']}'의 올바른 영어 철자는?",
                "a": word,
                "w1": wrong_spellings[0],
                "w2": wrong_spellings[1],
                "w3": wrong_spellings[2]
            })

    return questions[:target_count]

# ==========================================
# 3. CSV 파일 저장
# ==========================================
final_data = generate_english_questions(2000)
filename = "2학년_영어_문제은행.csv"

with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    # 헤더 작성 (웹 프로그램 호환)
    writer.writerow(["id", "grade", "subject", "q", "a", "w1", "w2", "w3"])
    
    for idx, item in enumerate(final_data, 1):
        row = [
            4000 + idx,       # 영어는 ID 4000번대부터 시작
            "2",              # grade
            "english",        # subject (영어)
            item["q"],        # q
            item["a"],        # a
            item["w1"],       # w1
            item["w2"],       # w2
            item["w3"]        # w3
        ]
        writer.writerow(row)

print(f"=========================================")
print(f"'{filename}' 파일이 생성되었습니다!")
print(f"총 {len(final_data)}개의 영어 문제가 저장되었습니다.")
print(f"=========================================")