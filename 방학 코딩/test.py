import tkinter as tk
import random

# 게임 로직
rsp = ['바위', '가위', '보']
wins = 0
draws = 0
loses = 0

# 가위바위보 결과 판단 함수
def play_game(player_p):
    global wins, draws, loses
    ai_p = random.choice(rsp)
    
    if player_p == ai_p:
        draws += 1
        result_label.config(text=f'플레이어: {player_p}, AI: {ai_p}\n비겼습니다.')
    elif (player_p == '바위' and ai_p == '가위') or (player_p == '가위' and ai_p == '보') or (player_p == '보' and ai_p == '바위'):
        wins += 1
        result_label.config(text=f'플레이어: {player_p}, AI: {ai_p}\n이겼습니다.')
    else:
        loses += 1
        result_label.config(text=f'플레이어: {player_p}, AI: {ai_p}\n졌습니다.')

    score_label.config(text=f"승: {wins}, 무: {draws}, 패: {loses}")

# 게임을 종료하는 함수
def exit_game():
    root.quit()

# tkinter 기본 설정
root = tk.Tk()
root.title("가위바위보 게임")
root.geometry("300x300")

# 설명 레이블
label = tk.Label(root, text="가위 바위 보 중 하나를 선택하세요", font=("Helvetica", 14))
label.pack(pady=20)

# 결과 표시 레이블
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# 점수 표시 레이블
score_label = tk.Label(root, text=f"승: {wins}, 무: {draws}, 패: {loses}", font=("Helvetica", 12))
score_label.pack(pady=10)

# 버튼 생성
button_rock = tk.Button(root, text="바위", command=lambda: play_game('바위'), width=10)
button_rock.pack(pady=5)

button_scissors = tk.Button(root, text="가위", command=lambda: play_game('가위'), width=10)
button_scissors.pack(pady=5)

button_paper = tk.Button(root, text="보", command=lambda: play_game('보'), width=10)
button_paper.pack(pady=5)

# 종료 버튼
exit_button = tk.Button(root, text="종료", command=exit_game, width=10)
exit_button.pack(pady=20)

# tkinter 메인 루프 실행
root.mainloop()
