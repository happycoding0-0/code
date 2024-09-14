import tkinter as tk
import random

# 가위바위보와 묵찌빠 게임 관련 데이터
a = ['가위', '바위', '보']
b = ['묵', '찌', '빠']
c = {'바위': '묵', '가위': '찌', '보': '빠'}
주도권 = None

# 가위바위보 승자 판단 함수
def 가위바위보_승자(player_p, ai_p):
    if (player_p == '바위' and ai_p == '가위') or (player_p == '가위' and ai_p == '보') or (player_p == '보' and ai_p == '바위'):
        return 'player'
    elif (ai_p == '바위' and player_p == '가위') or (ai_p == '가위' and player_p == '보') or (ai_p == '보' and player_p == '바위'):
        return 'ai'
    else:
        return 'draw'

# 가위바위보 시작
def start_rps(player_p):
    global 주도권
    ai_p = random.choice(a)
    승자 = 가위바위보_승자(player_p, ai_p)
    
    if 승자 == 'player':
        result_label.config(text=f'플레이어: {player_p}, AI: {ai_p}\n플레이어가 가위바위보에서 이겼습니다! 묵찌빠로 넘어갑니다.')
        주도권 = 'player'
        묵찌빠_단계()
    elif 승자 == 'ai':
        result_label.config(text=f'플레이어: {player_p}, AI: {ai_p}\nAI가 가위바위보에서 이겼습니다! 묵찌빠로 넘어갑니다.')
        주도권 = 'ai'
        묵찌빠_단계()
    else:
        result_label.config(text=f'플레이어: {player_p}, AI: {ai_p}\n비겼습니다. 게임을 다시 시작하세요.')

# 묵찌빠 단계
def 묵찌빠_단계():
    action_label.config(text=f"{주도권.capitalize()}가 공격합니다! 묵, 찌, 빠 중 선택하세요:")
    button_rock.config(text="묵", command=lambda: 묵찌빠_결과('묵'))
    button_scissors.config(text="찌", command=lambda: 묵찌빠_결과('찌'))
    button_paper.config(text="빠", command=lambda: 묵찌빠_결과('빠'))

# 묵찌빠 결과 확인
def 묵찌빠_결과(player_p1):
    global 주도권
    ai_p1 = random.choice(b)
    
    if player_p1 == ai_p1:
        if 주도권 == 'player':
            result_label.config(text=f'플레이어: {player_p1}, AI: {ai_p1}\n플레이어가 최종 승리했습니다!')
        else:
            result_label.config(text=f'플레이어: {player_p1}, AI: {ai_p1}\nAI가 최종 승리했습니다!')
        # 게임이 끝났을 때 버튼을 비활성화
        disable_buttons()
    else:
        if (player_p1 == '묵' and ai_p1 == '찌') or (player_p1 == '찌' and ai_p1 == '빠') or (player_p1 == '빠' and ai_p1 == '묵'):
            주도권 = 'player'
            result_label.config(text=f'플레이어: {player_p1}, AI: {ai_p1}\n플레이어가 주도권을 가져갑니다!')
        else:
            주도권 = 'ai'
            result_label.config(text=f'플레이어: {player_p1}, AI: {ai_p1}\nAI가 주도권을 가져갑니다!')
        
        묵찌빠_단계()

# 버튼 비활성화
def disable_buttons():
    button_rock.config(state="disabled")
    button_scissors.config(state="disabled")
    button_paper.config(state="disabled")

# tkinter 기본 설정
root = tk.Tk()
root.title("가위바위보 & 묵찌빠 게임")
root.geometry("350x400")

# 설명 레이블
action_label = tk.Label(root, text="가위, 바위, 보 중 하나를 선택하세요", font=("Helvetica", 14))
action_label.pack(pady=20)

# 결과 표시 레이블
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# 버튼 생성 (가위바위보용)
button_rock = tk.Button(root, text="바위", command=lambda: start_rps('바위'), width=10)
button_rock.pack(pady=5)

button_scissors = tk.Button(root, text="가위", command=lambda: start_rps('가위'), width=10)
button_scissors.pack(pady=5)

button_paper = tk.Button(root, text="보", command=lambda: start_rps('보'), width=10)
button_paper.pack(pady=5)

# tkinter 메인 루프 실행
root.mainloop()
