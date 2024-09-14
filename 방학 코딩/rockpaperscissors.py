import random

rsp = ['바위', '가위', '보']
wins = 0
draws = 0
loses = 0

while True:
    ai_p = random.choice(rsp)
    player_p = input("가위 바위 보 중 하나를 선택하세요: ")

    if player_p == ai_p:
        draws += 1
        print(f'플레이어: {player_p}, AI: {ai_p}') 
        print("비겼습니다.")

    elif (player_p == '바위' and ai_p == '가위') or (player_p == '가위' and ai_p == '보') or (player_p == '보' and ai_p == '바위'):
        wins += 1
        print(f'플레이어: {player_p}, AI: {ai_p}') 
        print("이겼습니다.")
    
    else:
        loses += 1
        print(f'플레이어: {player_p}, AI: {ai_p}') 
        print("졌습니다.")

    restart = input("한판 더 하시겠습니까? (y/n): ").lower()
    if restart != 'y':
        print(f"최종 결과: {wins}승 {draws}무 {loses}패")
        break
