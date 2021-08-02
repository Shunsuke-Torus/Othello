"""

https://gimon-sukkiri.jp/othello-reversi/
https://ruby-de-free.net/wp/how-to-make-othello-program-using-python-1/
https://ruby-de-free.net/wp/how-to-make-othello-program-using-python-0/
https://qiita.com/sasaco/items/fdb9771c146cb877b183
https://mojitoba.com/2020/01/10/python_type_error/

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
    
    #初期設定
    def __init__(self):
        self.table = np.zeros((size,size))
        
        self.table[3][4] = self.table[4][3] = black #黒
        self.table[3][3] = self.table[4][4] = white #白
        self.table = self.table.astype(int)
        self.turn = 1 #n手目
        self.move = black #初手
        #print(self.table)
        
    #ターン変更　黒→白,白→黒    
    def change(self):
        self.move *=-1
    
    #➀-1
    def check_table_first(self,x,y):#機能してない
        if x == None or y == None:
            return False
        elif  0 <= x < size and 0 <= y < size:
            return True
        else:
            return False
    #➀-2   
    def check_table_second(self,x,y):#firstがTrueの時確認する　and条件
        if self.table[x][y] != 0:
            return False
        else:
            return True
    #➀-3    
    def check_table_third(self,x,y):
        count = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                #print(F"self.table[{x + dx}][{y + dy}]>>{self.table[x + dx][y + dy]}")
                count += 1
                if dx == dy == 0:
                    continue
                elif self.check_table_first(x+dx,y+dy) == False:
                    continue
                elif self.table[x+dx][y+dy] == 0 :#reverse_judgeに持っていく
                    if count == 9:
                        return False
                    continue
                elif self.reverse_judge(x,y,dx,dy) == False:
                    continue
                else:
                    return True
    #➀-3-judge             
    def reverse_judge(self,x,y,dx,dy):#座標に敵石があるか否か + その先に自身の石があるか否か
        if self.check_table_first(x,y) == False:
            return False
        length = 0
        if self.check_table_first(x+dx,y+dy):         
            if self.table[ x + dx][ y + dy] == -self.move:#一方の石である時 true
                while self.table[ x + dx][ y + dy] == -self.move:#黒なら白
                    #print(F"self.table[{x + dx}][{y + dy}]>>{self.table[x + dx][y + dy]}")
                    if self.check_table_first(x,y) == True :
                        x += dx
                        y += dy
                        length += 1
                        if self.table[ x + dx][ y + dy] == -self.move:
                            continue
                        elif self.table[ x + dx][ y + dy] == 0 :
                            return False
                        else:
                            return length
                    else:
                        return False  
            else:
                return False
        else:
            return False
    #➀ Total
    def check_table_all(self,x,y):
        if self.check_table_first(x,y) == False:
            return False
        elif self.check_table_second(x,y) == False:
            return False
        elif self.check_table_third(x,y) == False:
            return False
        else:
            return True
            
    #反転
    def reverse_stone(self,x,y):
        for dx in (-1,0,1):#-1,0,1
            for dy in (-1,0,1): 
                #print(F"dx>>{dx},dy>>{dy}")
                length =  self.reverse_judge(x,y,dx,dy)
                if length == None:
                    length = 0
                if length > 0:
                    for l in range(length):
                        k = l+1
                        self.table[x+dx*k][y+dy*k] *= -1
    #表示  
    def display(self):
        print("==="*10)
        print(self.table)
                   
        
    #石を置く    
    def put_a_stone(self,x,y):
        if self.check_table_all(x,y) : #== True
            self.table[x][y] = self.move
            self.turn += 1
            self.reverse_stone(x,y)
            self.change()
            return True
        else:
            return False
#main    
def main():
    while (Board.turn <= 64):
        Board.display()
        x = int(input("x>>"))
        y = int(input("y>>"))
        Board.put_a_stone(y,x)#逆だった

if __name__ == '__main__':
    Board = Board()
    main()
     

