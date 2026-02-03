import csv
import random

# ==========================================
# 6학년 영어 핵심 문법 및 어휘 데이터베이스
# ==========================================
# 주제: 과거형, 길찾기, 장래희망, 날짜, 비교급, 미래형, 전화, 이유묻기
quiz_db = [
    # 1. 과거형 (Past Tense)
    {"q": "다음 빈칸에 알맞은 말은? \"What ____ you do yesterday?\"", "a": "did", "w": ["do", "will", "are"]},
    {"q": "다음 우리말을 영어로 바르게 옮긴 것은? \"나는 공원에 갔어.\"", "a": "I went to the park.", "w": ["I go to the park.", "I will go to the park.", "I am going to the park."]},
    {"q": "다음 대화의 빈칸에 알맞은 말은? A: How was your weekend? B: It ____ great.", "a": "was", "w": ["is", "are", "were"]},
    {"q": "다음 중 과거형 동사가 *잘못* 짝지어진 것은?", "a": "go - goed", "w": ["eat - ate", "see - saw", "play - played"]},
    {"q": "다음 빈칸에 알맞은 말은? \"I ____ my grandmother last Sunday.\"", "a": "visited", "w": ["visit", "visiting", "will visit"]},

    # 2. 길 찾기 (Directions)
    {"q": "다음 빈칸에 알맞은 말은? \"Where ____ the post office?\"", "a": "is", "w": ["are", "do", "does"]},
    {"q": "다음 대화의 응답으로 알맞은 것은? A: Where is the bank? B: ______", "a": "Go straight and turn left.", "w": ["I am happy.", "It is 5 o'clock.", "I like apples."]},
    {"q": "다음 단어의 뜻으로 알맞은 것은? [straight]", "a": "곧장(똑바로)", "w": ["오른쪽으로", "왼쪽으로", "뒤로"]},
    {"q": "다음 빈칸에 알맞은 말은? \"It's ____ the police station.\"", "a": "next to", "w": ["next", "next in", "next at"]},
    {"q": "길을 물어볼 때 쓰는 표현이 *아닌* 것은?", "a": "I like swimming.", "w": ["Where is the museum?", "How can I get there?", "Is there a hospital near here?"]},

    # 3. 장래 희망 (Occupations)
    {"q": "다음 빈칸에 알맞은 말은? \"What do you want to ____?\"", "a": "be", "w": ["do", "go", "have"]},
    {"q": "다음 우리말을 영어로 바르게 옮긴 것은? \"나는 과학자가 되고 싶어.\"", "a": "I want to be a scientist.", "w": ["I want to be a doctor.", "I want to be a teacher.", "I want to be a baker."]},
    {"q": "다음 직업과 하는 일이 바르게 연결된 것은?", "a": "Baker - makes bread", "w": ["Doctor - catches thieves", "Artist - flies a plane", "Pilot - draws pictures"]},
    {"q": "다음 빈칸에 알맞은 말은? \"I like cooking. I want to be a ____.\"", "a": "cook", "w": ["vet", "singer", "police officer"]},
    {"q": "다음 중 직업을 나타내는 단어가 *아닌* 것은?", "a": "Future", "w": ["Designer", "Movie director", "Programmer"]},

    # 4. 날짜와 생일 (Months & Dates)
    {"q": "다음 빈칸에 알맞은 말은? \"When is your ____?\"", "a": "birthday", "w": ["name", "school", "lunch"]},
    {"q": "다음 날짜를 영어로 바르게 읽은 것은? [5월 1일]", "a": "May first", "w": ["May one", "May once", "May firth"]},
    {"q": "다음 중 '3월'을 뜻하는 단어는?", "a": "March", "w": ["May", "April", "June"]},
    {"q": "다음 빈칸에 알맞은 말은? \"My birthday is ____ October 9th.\"", "a": "on", "w": ["in", "at", "of"]},
    {"q": "다음 중 서수(순서) 표현이 *틀린* 것은?", "a": "threeth", "w": ["first", "second", "third"]},

    # 5. 비교급 (Comparatives)
    {"q": "다음 빈칸에 알맞은 말은? \"The elephant is ____ than the dog.\"", "a": "bigger", "w": ["big", "biggest", "more big"]},
    {"q": "다음 우리말을 영어로 바르게 옮긴 것은? \"민수는 지호보다 키가 더 커.\"", "a": "Minsu is taller than Jiho.", "w": ["Minsu is tall than Jiho.", "Minsu is tallest than Jiho.", "Minsu is more tall than Jiho."]},
    {"q": "다음 빈칸에 알맞은 말은? \"Who is ____, you or Tom?\"", "a": "faster", "w": ["fast", "fastest", "more fast"]},
    {"q": "다음 중 비교급 형태가 *잘못된* 것은?", "a": "good - gooder", "w": ["heavy - heavier", "big - bigger", "strong - stronger"]},
    {"q": "다음 문장의 뜻으로 알맞은 것은? \"This box is heavier than that one.\"", "a": "이 상자는 저것보다 더 무겁다.", "w": ["이 상자는 저것보다 더 가볍다.", "이 상자는 저것보다 더 크다.", "이 상자는 저것보다 더 작다."]},

    # 6. 미래형 (Future Tense)
    {"q": "다음 빈칸에 알맞은 말은? \"What ____ you going to do this summer?\"", "a": "are", "w": ["do", "did", "will"]},
    {"q": "다음 대화의 응답으로 알맞은 것은? A: What will you do tomorrow? B: ______", "a": "I will go hiking.", "w": ["I went hiking.", "I go hiking.", "I am hiking."]},
    {"q": "다음 문장에서 미래를 나타내는 표현이 *아닌* 것은?", "a": "yesterday", "w": ["tomorrow", "next week", "this weekend"]},
    {"q": "다음 우리말을 영어로 바르게 옮긴 것은? \"나는 축구를 할 거야.\"", "a": "I am going to play soccer.", "w": ["I play soccer.", "I played soccer.", "I playing soccer."]},
    
    # 7. 전화 및 기타 (Telephone & Misc)
    {"q": "다음 전화 통화 표현 중 알맞지 *않은* 것은?", "a": "I am hang up.", "w": ["Can I speak to Minji?", "This is Minji speaking.", "Who is calling, please?"]},
    {"q": "다음 빈칸에 알맞은 말은? \"May I ____ to Jinu?\"", "a": "speak", "w": ["talks", "speaking", "speaks"]},
    {"q": "전화를 받을 때 \"접니다.\"를 영어로 바르게 표현한 것은?", "a": "This is he/she speaking.", "w": ["I am speaking.", "Here is me.", "It is me."]},
    {"q": "다음 빈칸에 알맞은 말은? \"Why are you ____?\"", "a": "sad", "w": ["happy", "book", "desk"]},
    {"q": "다음 대화의 응답으로 알맞은 것은? A: Why are you happy? B: ______ I passed the test.", "a": "Because", "w": ["So", "But", "And"]},
    {"q": "다음 단어의 우리말 뜻이 *잘못* 연결된 것은?", "a": "Run - 자다", "w": ["Eat - 먹다", "Sleep - 자다", "Study - 공부하다"]},
    
    # 8. 수량 및 조동사 (Quantity & Modals)
    {"q": "다음 문장의 빈칸에 들어갈 말은? \"How ____ apples do you want?\"", "a": "many", "w": ["much", "long", "old"]},
    {"q": "다음 빈칸에 알맞은 말은? \"How ____ is this bag?\"", "a": "much", "w": ["many", "big", "long"]},
    {"q": "가격을 묻는 표현으로 알맞은 것은?", "a": "How much is it?", "w": ["How many is it?", "How old is it?", "How tall is it?"]},
    {"q": "다음 중 셀 수 *없는* 명사는?", "a": "water", "w": ["apple", "book", "cup"]},
    {"q": "다음 빈칸에 알맞은 말은? \"You ____ help your mom.\"", "a": "should", "w": ["shouldn't", "don't", "not"]},
    {"q": "다음 우리말을 영어로 바르게 옮긴 것은? \"너는 일찍 자야 해.\"", "a": "You should go to bed early.", "w": ["You can go to bed early.", "You may go to bed early.", "You go to bed early."]},
    {"q": "충고하는 말을 할 때 쓰는 조동사는?", "a": "should", "w": ["will", "do", "are"]},
    {"q": "다음 중 짝지어진 단어의 관계가 나머지와 *다른* 것은?", "a": "Happy - Glad (비슷)", "w": ["Hot - Cold (반대)", "Big - Small (반대)", "Tall - Short (반대)"]},
    {"q": "다음 빈칸에 알맞은 말은? \"She ____ a teacher.\"", "a": "is", "w": ["are", "am", "be"]},
    {"q": "다음 문장의 올바른 부정문은? \"He likes pizza.\"", "a": "He doesn't like pizza.", "w": ["He don't like pizza.", "He not likes pizza.", "He isn't like pizza."]},
    {"q": "다음 중 3인칭 단수 주어는?", "a": "She", "w": ["I", "You", "We"]},
    {"q": "다음 빈칸에 알맞은 말은? \"They ____ playing soccer now.\"", "a": "are", "w": ["is", "am", "was"]},
    {"q": "다음 중 진행형(~하는 중이다) 문장은?", "a": "I am reading a book.", "w": ["I read a book.", "I will read a book.", "I readed a book."]},
    {"q": "다음 빈칸에 알맞은 말은? \"Can you ____ me?\"", "a": "help", "w": ["helps", "helping", "helped"]},
    {"q": "다음 대화의 빈칸에 알맞은 말은? A: Thank you very much. B: ______.", "a": "You're welcome.", "w": ["That's too bad.", "I'm sorry.", "Yes, please."]}
]

# CSV 생성 함수
def create_csv_file(filename="6학년_영어_문제은행.csv"):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "grade", "subject", "q", "a", "w1", "w2", "w3"])
        
        for idx, item in enumerate(quiz_db, 1):
            row = [
                6000 + idx,   # ID (6001부터 시작)
                6,            # 학년
                "english",    # 과목
                item["q"],    # 문제
                item["a"],    # 정답
                item["w"][0], # 오답1
                item["w"][1], # 오답2
                item["w"][2]  # 오답3
            ]
            writer.writerow(row)
            
    print(f"'{filename}' 파일이 생성되었습니다! (총 {len(quiz_db)}문제)")

if __name__ == "__main__":
    create_csv_file()