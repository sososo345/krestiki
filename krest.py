import random

game = [
    ['','',''],
    ['','',''],
    ['','','']
]
def movingsucces(game,s,x,y):
    if game[x][y]=="":
        game[x][y]= s
    else:
        move-=1
    return game,move
def moved(move):
    for i in range(3):
        if game[i][0]==  game[i][1]== game[i][2]!="":
            print ("win")
            return False   
        elif game[0][i]==  game[1][i]== game[2][i]!="":
            print("win")
            return False
        else:
            return True
    if game[0][0]==game[1][1]==game[2][2]=='':
        print('win')
        return False
    else:
        return True
    if move>=9:
        print('nikto ne veigral')
        return False
def main(game):
    flag=True
    move=0
    while flag:
        x = int(input())
        y = int(input())
        if move%2==0:
            game,move = movingsucces(game,"x",x,y,move)
        else:
            game,move = movingsucces(game,"0",x,y,move)
        flag = moved(game)
        move +=1
main(game)

        

            

    
