import random

a = ['가위', '바위', '보']
b = ['묵', '찌', '빠']
c = {'바위': '묵', '가위': '찌', '보': '빠'}

def 가위바위보_승자(player_p, ai_p):
    if (player_p == '바위' and ai_p == '가위') or (player_p == '가위' and ai_p == '보') or (player_p == '보' and ai_p == '바위'):
        return 'player'
    elif (ai_p == '바위' and player_p == '가위') or (ai_p == '가위' and player_p == '보') or (ai_p == '보' and player_p == '바위'):
        return 'ai'
    else:
        return 'draw'

# 가위바위보 시작
print("안내면 진다! 가위 바위 보")
ai_p = random.choice(a)
player_p = input('가위, 바위, 보 중 하나를 선택하세요: ')

# 가위바위보 결과 확인
승자 = 가위바위보_승자(player_p, ai_p)

if 승자 == 'player':
    print(f'플레이어: {player_p}, AI: {ai_p}')
    print('플레이어가 가위바위보에서 이겼습니다! 묵찌빠로 넘어갑니다.')
    주도권 = 'player'
elif 승자 == 'ai':
    print(f'플레이어: {player_p}, AI: {ai_p}')
    print('AI가 가위바위보에서 이겼습니다! 묵찌빠로 넘어갑니다.')
    주도권 = 'ai'
else:
    print(f'플레이어: {player_p}, AI: {ai_p}')
    print('비겼습니다. 게임을 다시 시작하세요.')
    exit()

# 묵찌빠 단계
while True:
    if 주도권 == 'player':
        print(f"플레이어가 주도권을 가집니다. 공격!")
    else:
        print(f"AI가 주도권을 가집니다. 공격!")

    player_p1 = input('묵, 찌, 빠 중 하나를 선택하세요: ')
    ai_p1 = random.choice(b)
    print(f'플레이어: {player_p1}, AI: {ai_p1}')

    if player_p1 == ai_p1:
        # 똑같은 걸 냈을 때 승부가 결정됨
        if 주도권 == 'player':
            print('플레이어가 최종 승리했습니다!')
        else:
            print('AI가 최종 승리했습니다!')
        break
    else:
        # 주도권 변경
        if (player_p1 == '묵' and ai_p1 == '찌') or (player_p1 == '찌' and ai_p1 == '빠') or (player_p1 == '빠' and ai_p1 == '묵'):
            주도권 = 'player'
            print("플레이어가 주도권을 가져갑니다!")
        else:
            주도권 = 'ai'
            print("AI가 주도권을 가져갑니다!")
