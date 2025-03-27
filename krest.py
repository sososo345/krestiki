import random

game = [
    ['{ }','{ }','{ }'],
    ['{ }','{ }','{ }'],
    ['{ }','{ }','{ }']
]
def main():
    flag=True
    move=0
    while flag:
        x,y = input()
        if move%2==0:
            game,move = def3 (game"x",x,y,move)
        else:
            game,move = def3 (game"x",x,y,move)
        flag = def2(game)
        move +=1
def moving ():
    if game[x][y]=="":
        game[x][y]= s
    else:
        move-=1
    return game,move
