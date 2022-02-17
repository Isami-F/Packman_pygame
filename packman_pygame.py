# 捕食モード、残基リトライ、敵の動き方、ユーザビリティの向上


import pygame
from pygame.locals import *
import sys
import random

# map_data 21*22
data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 3, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 3, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 1, 3, 0, 0, 1, 3, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 3, 0, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 2, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 3, 0, 3, 1, 0, 3, 0, 1, 3, 0, 3, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 3, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 3, 0, 3, 0, 0, 1, 3, 0, 3, 0, 3, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 3, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],    
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

l_data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
          [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],    
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

(w, h) = (30*20, 22*20)      # ウインドウサイズ


# x,yが円の左上座標であることに留意
def p_move(x, y, lx, ly, direct, p_direct, flag):
    if flag == 1:
        # 左移動
        if direct == "L":
            x = x - 1
            if x < 0:   # 左の画面外の処理
                x = 400
            lx = x // 20
            # 曲がりやすいように補正処理
            i = y % 20
            if p_direct == "U":
                if 0 < i and i <= 5:
                    y = y - i                    
                elif i >= 15:
                    y = y + (20 - i)
                    ly = y // 20
            elif p_direct == "D":
                if 0 < i and i <= 5:
                    y = y - i
                    ly = (y+19) // 20
                elif i >= 15:
                    y = y + (20 - i)                        
        # 右移動                                        
        elif direct == "R":
            x = x + 1
            if (x+19) == 21*20:   # 右の画面外の処理
                x = 0
            lx = (x+19) // 20
            # 曲がりやすいように補正処理
            i = y % 20
            if p_direct == "U":
                if 0 < i and i <= 5:
                    y = y - i
                elif i >= 15:
                    y = y + (20 - i)
                    ly = y // 20
            elif p_direct == "D":
                if 0 < i and i <= 5:
                    y = y - i
                    ly = (y+19) // 20
                elif i >= 15:
                    y = y + (20 - i)
        # 上移動        
        elif direct == "U":
            y = y - 1
            ly = y // 20
            # 曲がりやすいように補正処理
            i = x % 20
            if p_direct == "L":
                if 0 < i and i <= 5:
                    x = x - i                    
                elif i >= 15:
                    x = x + (20 - i)
                    lx = x // 20
            elif p_direct == "R":
                if 0 < i and i <= 5:
                    x = x - i
                    lx = (x+19) // 20
                elif i >= 15:
                    x = x + (20 - i)
        # 下移動
        elif direct == "D":
            y = y + 1
            ly = (y+19) // 20
            # 曲がりやすいように補正処理
            i = x % 20
            if p_direct == "L":
                if 0 < i and i <= 5:
                    x = x - i                    
                elif i >= 15:
                    x = x + (20 - i)
                    lx = x // 20
            elif p_direct == "R":
                if 0 < i and i <= 5:
                    x = x - i
                    lx = (x+19) // 20
                elif i >= 15:
                    x = x + (20 - i)

        # 壁に当たる判定     厳しすぎて曲がれない::+-5まで補正
        if data[ly][lx] == 1:
            if direct == "L":
                x = x + 1
                lx = lx + 1                    
            elif direct == "R":
                x = x - 1
                lx = lx - 1        
            elif direct == "U":
                y = y + 1
                ly = ly + 1
            elif direct == "D":
                y = y - 1
                ly = ly - 1
        # 壁抜け対策
        else:
            if direct == "L": 
                if y % 20 != 0:                        
                    x = x + 1
                    lx = lx + 1
            elif direct == "R":
                if y % 20 != 0:
                    x = x - 1
                    lx = lx - 1
            elif direct == "U":
                if x % 20 != 0:
                    y = y + 1
                    ly = ly + 1
            elif direct == "D":
                if x % 20 != 0:
                    y = y - 1
                    ly = ly - 1

    return x, y, lx, ly, direct, p_direct, flag


def e_move(x, y, lx, ly, direct, p_direct, l_direct, flag):
    if flag == 1:
        # 左移動
        if direct == "L":
            x = x - 1
            if x < 0:   # 左の画面外の処理
                x = 400
            lx = x // 20                       
        # 右移動                                        
        elif direct == "R":
            x = x + 1
            if (x+19) == 21*20:   # 右の画面外の処理
                x = 0
            lx = (x+19) // 20
        # 上移動        
        elif direct == "U":
            y = y - 1
            ly = y // 20
        # 下移動
        elif direct == "D":
            y = y + 1
            ly = (y+19) // 20

        # 壁に当たる判定     
        if data[ly][lx] == 1:
            if direct == "L":
                x = x + 1
                lx = lx + 1                    
            elif direct == "R":
                x = x - 1
                lx = lx - 1        
            elif direct == "U":
                y = y + 1
                ly = ly + 1
            elif direct == "D":
                y = y - 1
                ly = ly - 1
            l_direct.append(p_direct)
            p_direct = direct
            l_direct.remove(p_direct)
            direct = random.choice(l_direct)    # 方向転換
            #print(l_direct)
        # T字路
        elif data[ly][lx] == 3:
            if direct == "L":
                if x == lx * 20:
                    l_direct.append(p_direct)
                    p_direct = direct
                    l_direct.remove(p_direct)
                    direct = random.choice(l_direct)
            elif direct == "R":
                if x == lx * 20:
                    l_direct.append(p_direct)
                    p_direct = direct
                    l_direct.remove(p_direct)
                    direct = random.choice(l_direct)
            elif direct == "U":
                if y == ly * 20:
                    l_direct.append(p_direct)
                    p_direct = direct
                    l_direct.remove(p_direct)
                    direct = random.choice(l_direct)
            elif direct == "D":
                if y == ly * 20:
                    l_direct.append(p_direct)
                    p_direct = direct
                    l_direct.remove(p_direct)
                    direct = random.choice(l_direct)


        # 壁抜け対策
        else:
            if direct == "L": 
                if y % 20 != 0:                        
                    x = x + 1
                    lx = lx + 1
            elif direct == "R":
                if y % 20 != 0:
                    x = x - 1
                    lx = lx - 1
            elif direct == "U":
                if x % 20 != 0:
                    y = y + 1
                    ly = ly + 1
            elif direct == "D":
                if x % 20 != 0:
                    y = y - 1
                    ly = ly - 1

    return x, y, lx, ly, direct, p_direct, l_direct, flag



def main():
    (p_x, p_y) = (10*20, 16*20)         # プレイヤーの初期位置
    (p_lx, p_ly) = (10, 16)             # マップリストにおけるプレイヤーの位置
    p_direct = "L"                      # プレイヤーの動く方向
    p_p_direct = "L"                    # プレイヤーの１つ前に動いていた別方向
    
    (e1_x, e1_y) = (10*20, 8*20)         # 敵の初期位置
    (e1_lx, e1_ly) = (10, 8)             # マップリストにおける敵の初期位置
    e1_direct = "R"                      # 敵の動く方向
    e1_p_direct = "R"                    # 敵の1つ前に動いていた別方向
    l_e1_direct = ["L", "L", "R", "R", "U", "U", "U", "D", "D"]   # 敵の動く方向選択用リスト
    
    (e2_x, e2_y) = (11*20, 10*20)         # 敵の初期位置
    (e2_lx, e2_ly) = (11, 10)             # マップリストにおける敵の初期位置
    e2_direct = "L"                      # 敵の動く方向
    e2_p_direct = "L"                    # 敵の1つ前に動いていた別方向
    l_e2_direct = ["L", "L", "R", "R", "U", "U", "U", "D", "D"]   # 敵の動く方向選択用リスト

    (e3_x, e3_y) = (9*20, 10*20)         # 敵の初期位置
    (e3_lx, e3_ly) = (9, 10)             # マップリストにおける敵の初期位置
    e3_direct = "R"                      # 敵の動く方向
    e3_p_direct = "R"                    # 敵の1つ前に動いていた別方向
    l_e3_direct = ["L", "L", "R", "R", "U", "U", "D", "D", "D"]   # 敵の動く方向選択用リスト

    (e4_x, e4_y) = (10*20, 10*20)         # 敵の初期位置
    (e4_lx, e4_ly) = (10, 10)             # マップリストにおける敵の初期位置
    e4_direct = "U"                      # 敵の動く方向
    e4_p_direct = "U"                    # 敵の1つ前に動いていた別方向
    l_e4_direct = ["L", "L", "L", "R", "R", "U", "D", "D", "D"]   # 敵の動く方向選択用リスト
    
    flag = 0                            # ゲームスタート用フラッグ
    F = 0                               # プレイヤーの移動方向わかりやすいよう交互に描画用フラッグ
    f = 0                               # 10数秒ごとに描画
    q = 0                               # 
        
    pygame.init()
    pygame.display.set_mode((w, h))
    pygame.display.set_caption("Packman")
    screen = pygame.display.get_surface()
    # テキスト
    x = 0
    font1 = pygame.font.SysFont(None, 40)
    text1 = font1.render("Score", True, (255, 0, 0))
    
    font2 = pygame.font.SysFont(None, 30)
    text2 = font1.render(str(x), True, (255, 255, 255))


    c = 0
    C = 0
    
    # マップ作成
    screen.fill((0, 0, 0))    # 画面の背景色
    screen.blit(text1, (21*20+10, 10))
    
    for a in range(len(data)):
        for b in range(len(data[0])):
            if data[a][b] == 1:
                pygame.draw.rect(screen, (100, 150, 210), Rect(b*20, a*20, 20, 20))
                pygame.draw.rect(screen, (0, 100, 210), Rect(b*20, a*20, 20, 20), width = 1)
    # 外枠
    pygame.draw.rect(screen, (255, 255, 255), Rect(0, 0, 21*20, 22*20), width = 3)
    pygame.draw.rect(screen, (0, 0, 0), Rect(0, 10*20, 20, 20))
    pygame.draw.rect(screen, (0, 0, 0), Rect(20*20+10, 10*20, 20, 20))
    
 
    while (True):
        pygame.display.update()   # 画面更新
        pygame.time.wait(12)      # 更新時間間隔

        # 真ん中の仕切り
        pygame.draw.rect(screen, (255, 255, 255), Rect(10*20, 9*20+7, 20, 6))

        # テキスト表示
        pygame.draw.rect(screen, (0, 0, 0), Rect(25*20, 2*20, 100, 50))
        screen.blit(text2, (25*20+5, 2*20+5))
        
        
        # クリア判定
        if C == 5:
            break
        
        # 失敗判定
        if q == 1:
            break
        
        c = 0
        for a in range(len(data)):
            for b in range(len(data[0])):
                # 白い点（えさ？）描画
                if l_data[a][b] == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (b*20+7, a*20+7, 6, 6))
                    pygame.draw.ellipse(screen, (255, 255, 255), (b*20+7, a*20+7, 6, 6))
                    c = c + 1
                elif l_data[a][b] == 2:
                    pygame.draw.rect(screen, (0, 0, 0), (b*20+7, a*20+7, 6, 6))
                    l_data[a][b] == 1
        if c == 0:
            C = C + 1
        
        # プレイヤー描画用座標
        p_L_1 = [[p_x+7, p_y+3], [p_x+10, p_y+2], [p_x+16, p_y+4], [p_x+18, p_y+10],[p_x+16, p_y+16], [p_x+10, p_y+18], [p_x+7, p_y+17], [p_x+10, p_y+10]] 
        p_L_2 = [[p_x+3, p_y+7], [p_x+7, p_y+3 ], [p_x+10, p_y+2], [p_x+16, p_y+4], [p_x+18, p_y+10],[p_x+16, p_y+16], [p_x+10, p_y+18], [p_x+7, p_y+17],
                 [p_x+3, p_y+13], [p_x+10, p_y+10]]
        p_R_1 = [[p_x+13, p_y+3], [p_x+10, p_y+2], [p_x+4, p_y+4], [p_x+2, p_y+10],[p_x+4, p_y+16], [p_x+10, p_y+18], [p_x+13, p_y+17], [p_x+10, p_y+10]] 
        p_R_2 = [[p_x+17, p_y+7], [p_x+13, p_y+3 ], [p_x+10, p_y+2], [p_x+4, p_y+4], [p_x+2, p_y+10],[p_x+4, p_y+16], [p_x+10, p_y+18], [p_x+13, p_y+17],
                 [p_x+17, p_y+13], [p_x+10, p_y+10]]        
        p_U_1 = [[p_x+17, p_y+7], [p_x+18, p_y+10], [p_x+16, p_y+16], [p_x+10, p_y+18],[p_x+4, p_y+16], [p_x+2, p_y+10], [p_x+3, p_y+7], [p_x+10, p_y+10]] 
        p_U_2 = [[p_x+13, p_y+3], [p_x+17, p_y+7], [p_x+18, p_y+10], [p_x+16, p_y+16], [p_x+10, p_y+18],[p_x+4, p_y+16], [p_x+2, p_y+10], [p_x+3, p_y+7],
                 [p_x+7, p_y+3], [p_x+10,p_y+10]] 
        p_D_1 = [[p_x+17, p_y+13], [p_x+18, p_y+10], [p_x+16, p_y+4], [p_x+10, p_y+2],[p_x+4, p_y+4], [p_x+2, p_y+10], [p_x+3, p_y+13], [p_x+10, p_y+10]] 
        p_D_2 = [[p_x+13, p_y+17], [p_x+17,p_y+13], [p_x+18, p_y+10], [p_x+16, p_y+4], [p_x+10, p_y+2],[p_x+4, p_y+4], [p_x+2, p_y+10], [p_x+3, p_y+13],
                 [p_x+7, p_y+17], [p_x+10,p_y+10]]
        # 描画処理
        if F == 0:
            pygame.draw.rect(screen, (0, 0, 0), (p_x+2, p_y+2, 16, 16))
            pygame.draw.rect(screen, (0, 0, 0), (e1_x+2, e1_y+2, 16, 16))
            pygame.draw.rect(screen, (0, 0, 0), (e2_x+2, e2_y+2, 16, 16))
            pygame.draw.rect(screen, (0, 0, 0), (e3_x+2, e3_y+2, 16, 16))
            pygame.draw.rect(screen, (0, 0, 0), (e4_x+2, e4_y+2, 16, 16))
            
            pygame.draw.ellipse(screen, (255, 255, 0), (p_x+2, p_y+2, 16, 16))       # プレイヤー
            pygame.draw.ellipse(screen, (255, 0, 0), (e1_x+2, e1_y+2, 16, 16))       # 敵1
            pygame.draw.ellipse(screen, (130, 255, 50), (e2_x+2, e2_y+2, 16, 16))    # 敵2
            pygame.draw.ellipse(screen, (0, 255, 255), (e3_x+2, e3_y+2, 16, 16))     # 敵3
            pygame.draw.ellipse(screen, (175, 100, 200), (e4_x+2, e4_y+2, 16, 16))   # 敵4
            
        elif F == 1:
            f += 1
            if f % 10 == 9:   # 10処理ごとに描画変更
                F = 2
                f = 0
            pygame.draw.rect(screen, (0, 0, 0), (p_p_x, p_p_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e1_x, p_e1_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e2_x, p_e2_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e3_x, p_e3_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e4_x, p_e4_y, 20, 20))
            if p_direct == "L":
                pygame.draw.polygon(screen, (255,255,0), p_L_1)
            elif p_direct == "R":
                pygame.draw.polygon(screen, (255,255,0), p_R_1)
            elif p_direct == "U":
                pygame.draw.polygon(screen, (255,255,0), p_U_1)
            elif p_direct == "D":
                pygame.draw.polygon(screen, (255,255,0), p_D_1)
            
            pygame.draw.ellipse(screen, (255, 0, 0), (e1_x+2, e1_y+2, 16, 16))      # 敵1
            pygame.draw.ellipse(screen, (130, 255, 50), (e2_x+2, e2_y+2, 16, 16))   # 敵2
            pygame.draw.ellipse(screen, (0, 255, 255), (e3_x+2, e3_y+2, 16, 16))    # 敵3
            pygame.draw.ellipse(screen, (175, 100, 200), (e4_x+2, e4_y+2, 16, 16))  # 敵4
            
        elif F == 2:
            f += 1
            if f % 10 == 9:   # 10処理ごとに描画変更
                F = 1
                f = 0
            pygame.draw.rect(screen, (0, 0, 0), (p_p_x, p_p_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e1_x, p_e1_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e2_x, p_e2_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e3_x, p_e3_y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (p_e4_x, p_e4_y, 20, 20))
            if p_direct == "L":
                pygame.draw.polygon(screen, (255,255,0), p_L_2)
            elif p_direct == "R":
                pygame.draw.polygon(screen, (255,255,0), p_R_2)
            elif p_direct == "U":
                pygame.draw.polygon(screen, (255,255,0), p_U_2)
            elif p_direct == "D":
                pygame.draw.polygon(screen, (255,255,0), p_D_2)

            pygame.draw.ellipse(screen, (255, 0, 0), (e1_x+2, e1_y+2, 16, 16))      # 敵1
            pygame.draw.ellipse(screen, (130, 255, 50), (e2_x+2, e2_y+2, 16, 16))   # 敵2
            pygame.draw.ellipse(screen, (0, 255, 255), (e3_x+2, e3_y+2, 16, 16))    # 敵3
            pygame.draw.ellipse(screen, (175, 100, 200), (e4_x+2, e4_y+2, 16, 16))  # 敵4
            
            

        # 移動座標処理、x,yが円の左上座標であることに留意
        p_p_x,  p_p_y = p_x, p_y
        p_e1_x,  p_e1_y = e1_x, e1_y
        p_e2_x,  p_e2_y = e2_x, e2_y
        p_e3_x,  p_e3_y = e3_x, e3_y
        p_e4_x,  p_e4_y = e4_x, e4_y
        
        p_x,p_y,p_lx, p_ly,p_direct,p_p_direct,flag = p_move(p_x,p_y,p_lx,p_ly,p_direct,p_p_direct,flag)
        e1_x,e1_y,e1_lx,e1_ly,e1_direct,e1_p_direct,l_e1_direct,flag = e_move(e1_x,e1_y,e1_lx,e1_ly,e1_direct,e1_p_direct,
                                                                        l_e1_direct,flag)
        e2_x,e2_y,e2_lx,e2_ly,e2_direct,e2_p_direct,l_e2_direct,flag = e_move(e2_x,e2_y,e2_lx,e2_ly,e2_direct,e2_p_direct,
                                                                        l_e2_direct,flag)
        e3_x,e3_y,e3_lx,e3_ly,e3_direct,e3_p_direct,l_e3_direct,flag = e_move(e3_x,e3_y,e3_lx,e3_ly,e3_direct,e3_p_direct,
                                                                        l_e3_direct,flag)
        e4_x,e4_y,e4_lx,e4_ly,e4_direct,e4_p_direct,l_e4_direct,flag = e_move(e4_x,e4_y,e4_lx,e4_ly,e4_direct,e4_p_direct,
                                                                        l_e4_direct,flag)

        # 接触判定
        if abs(p_x - e1_x) <= 5 and abs(p_y - e1_y) <= 5:
            q = 1
        elif abs(p_x - e2_x) <= 5 and abs(p_y - e2_y) <= 5:
            q = 1
        elif abs(p_x - e3_x) <= 5 and abs(p_y - e3_y) <= 5:
            q = 1
        elif abs(p_x - e4_x) <= 5 and abs(p_y - e4_y) <= 5:
            q = 1

        if q == 1:
            pygame.draw.rect(screen, (255, 255, 255), Rect(7*20, 9*20, 7*20, 3*20))
            font3 = pygame.font.SysFont(None, 60)
            text3 = font3.render("Fale", True, (255, 155, 0))
            screen.blit(text3, (8*20+5, 9*20+10))

        # スコア
        if 0 in l_data[p_ly]:
            if l_data[p_ly][p_lx] == 0:
                x = x + 10
                l_data[p_ly][p_lx] = 2
                text2 = font1.render(str(x), True, (255, 255, 255))
        
        # キーイベント
        for event in pygame.event.get():
            # マスクリックでスタート
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                flag = 1
                F = 1

            # 終了用の処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # キーボード入力の処理
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT:
                    p_p_direct = p_direct
                    p_direct = "L" 
                if event.key == K_RIGHT:
                    p_p_direct = p_direct
                    p_direct = "R"
                if event.key == K_UP:
                    p_p_direct = p_direct
                    p_direct = "U"
                if event.key == K_DOWN:
                    p_p_direct = p_direct
                    p_direct = "D"
        # クリア判定
        if C == 4:
            pygame.draw.rect(screen, (255, 255, 255), Rect(7*20, 9*20, 7*20, 3*20))
            font3 = pygame.font.SysFont(None, 60)
            text3 = font3.render("Clear", True, (255, 155, 0))
            screen.blit(text3, (7*20+10, 9*20+10))
            c = -1


    while (True):
        # キーイベント
        for event in pygame.event.get():
            # 終了用の処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()
    
