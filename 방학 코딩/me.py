a = ['가위', '바위', '보']
b = ['묵', '찌', '빠']
c = {'바위':'묵' , '가위': '찌' , '보':'빠'}


import random

print("안내면 진다 가위 바위 보")
ai_p = random.choice(a)
player_p = input('가위,바위,보 중 하나 선택')

if (player_p == '바위' and ai_p == '가위' ) or (player_p == '가위' and ai_p == '보') or (player_p == '보' and ai_p== '바위'):
    print( 'player:', player_p , ' AI:', ai_p)
    print(c.values(player_p))
    print(c.values(player_p))
    player_p1 = input('묵, 찌, 빠 중 하나를 선택하세요:')
    ai_p1= random.choice(b)
    if (player_p1 == ai_p1 ) :
        print('player', player_p1 , 'AI', ai_p1)
        print('이겼습니다.')
    elif(ai_p == '바위' and player_p == '가위' ) or (ai_p == '가위' and player_p == '보') or (ai_p == '보' and player_p== '바위'):
        print( 'player:', player_p , ' AI:', ai_p)
        print(c.values(ai_p))
        print(c.values(ai_p))
        player_p1 = input('묵, 찌, 빠 중 하나를 선택하세요:')
        ai_p1= random.choice(b)
        if (ai_p1 == player_p1):
            print('player', player_p1 , 'AI', ai_p1)
            print('졌습니다.')    
    elif (ai_p1 == '묵' and player_p1 == '찌' ) or (ai_p1 == '찌' and player_p1 == '빠') or (ai_p1 == '빠' and player_p1== '묵'):
        print('player', player_p1 , 'AI', ai_p1)
        print(ai_p1)         
        print(ai_p1)
                 
    

    

