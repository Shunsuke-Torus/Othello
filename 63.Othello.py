"""

https://gimon-sukkiri.jp/othello-reversi/
https://ruby-de-free.net/wp/how-to-make-othello-program-using-python-1/
https://ruby-de-free.net/wp/how-to-make-othello-program-using-python-0/
https://qiita.com/sasaco/items/fdb9771c146cb877b183

オセロ通常
↓
ダメージオセロ(角を持つと枚数が-3されるみたいな。)

オセロ
9*9の81枚を生成
空、黒、白,壁 = 0,1,-1,2
それぞれの色が挟まったときその色になる

ボードを表現する2次元配列：RawBoard
手番数を表す変数：Turns
現在の手番の石の色を表す変数：CurrentColor

1ターンの挙動
自分のターン
↓
石の場所を選定
↓
石が置けるのか確認→➀
↓ok
石を置く→➁
↓
挟まった石を逆の色の石に変化させる→➂
↓
相手のターン


➀入力座標が8*8の盤面内にあるか　and　すでに座標に石が置かれていないか and 石を置くとき、ひっくり返す石が1つ以上あるか

➁指定された座標に石を置く

➂以前の➀でreturnしたx,yの座標を用いる→石を置く地点からx,y座標までを自身の石にする　 
"""
import numpy as np

black = 1
white = -1
size = 8
#def main ():
    
class Board (object):
    
    def __init__(self):#初期設定
        self.table = np.zeros((size,size))
        
        self.table[3][4] = self.table[4][3] = black #黒
        self.table[3][3] = self.table[4][4] = white #白
        self.table = self.table.astype(int)
        
        self.move = black #初手
        print(self.table)
        
    def change(self):#ターン変更　黒→白,白→黒
        self.move *=-1
    
    def check_table_first(self,x,y):
        if x == None or y == None:
            return False
        elif  0 <= x < size and 0 <= y < size:
            return True
        else:
            return False
        
    def check_table_second(self,x,y):#firstがTrueの時確認する　and条件
        if self.table[x][y] != 0:
            return False
        else:
            return True
        
    def check_table_third(self,x,y):
        for dx in range(-1,2):
            for dy in range(-1,2):
                print(F"self.table[{x + dx}][{y + dy}]>>{self.table[x + dx][y + dy]}")
                if dx == dy == 0:
                    continue
                elif self.check_table_first(self,x+dx,y+dy) == False:
                    return False,dx,dy
                elif self.table[x+dx][y+dy] == 0 :
                    continue
                else:
                    return self.reverse_judge(self,x,y,dx,dy)
                    
    def reverse_judge(self,x,y,dx,dy):#座標に敵石があるか否か + その先に自身の石があるか否か
        length = 0
        if self.table[ x + dx][ y + dy] == -self.move:#一方の石である時 true
            while self.table[ x + dx][ y + dy] == -self.move:
                if self.check_table_first(self,x,y) == True :
                    x += dx
                    y += dy
                    length += 1
                    if self.table[ x + dx][ y + dy] == -self.move:
                        continue
                    else:
                        return length,dx,dy
                else:
                    return False,dx,dy  
        else:
            return False,dx,dy
    
    def check_table_all(self,x,y):
        if self.check_table_first(self,x,y) == False:
            return False
        elif self.check_table_second(self,x,y) == False:
            return False
        elif self.check_table_third(self,x,y)[0] == False:
            return False
        else:
            return True
            
    
    def reverse_stone(self,x,y):
        length,dx,dy = self.check_table_third(self,x,y)
        
        if abs(dx-x) > 0 and abs(dy-y) > 0:
            for i in range(abs(dx-x)):
                for j in range(abs(dy-y)):
                    self.table[i][j] *= -1
        
        if abs(dx-x) > 0 or abs(dy-y) > 0:
            if abs(dx-x) > 0: #abs(dy-y) = 0:
                
            elif abs(dy-y) > 0: #abs(dx-x) = 0:
                
        
        
        
        
    def put_a_stone(self,x,y):
        if self.check_table_all(self,x,y) == True:
            self.table[x][y] = self.move
            
            
    
    
    
def main():    
    board = Board()

if __name__ == '__main__':
    main()
     

