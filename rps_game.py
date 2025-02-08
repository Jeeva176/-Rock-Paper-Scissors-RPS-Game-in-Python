import random
import sys
from enum import Enum

def rps():
    game_count=0
    player_count=0

    def play_rps():
        nonlocal game_count
        nonlocal player_count
    class RPS(Enum):
        BOOK =1
        PEN =2
        NOTE=3
    print(RPS(2)) 
    print(RPS.PEN) 
    print(RPS.NOTE.value)  
    print(RPS)
    #playagain=True
    #while playagain:
    #def rps():
    player_cnt=0
    python_cnt=0
    game_count=1 

    playerchoice=input(f'Enter.... \n1 for book \n 2 for pen \n3 for note')
        
    for game_count in range(1,12):
        print(f'\n game count:{game_count}')

        
    if playerchoice not in['1','2','3']:
        print(f'you must enter:1,2,3')
        return play_rps

    print(playerchoice)
    player=int(playerchoice)
    print(type(player))

    if player<1 or player>3:
        sys.exit('you must enter 1,2,3')

    computerchoice=random.choice("123")
    computer=int(computerchoice)
    print('you choose'  + playerchoice+".")
    print('python choose' + computerchoice+'.')


    def game_play(player,computer):
        nonlocal game_count
        nonlocal player_cnt
        nonlocal python_cnt
        if player==1 and computer==3:
            player_cnt+=1
            print('welcome')
        elif player==2 and  computer==1:
            player_cnt+=1
            print('yon won 2nd') 
        elif player==3 and computer==2:
            player_cnt+=1
            print('you won 3rd')
        elif player==computer:
            print('tie game')    
        else:
            python_cnt+=1
            print('python wins')
        game_play(player,computer)        

        game_result=game_play(player,computer)    
        print(game_result)
        game_result()    


    #nonlocal game_count
   # global python_cnt
    player_cnt+=1
    python_cnt+=1
    game_count+=1
    print(f"GAME:",str(game_count))
    print(f"PLAYER:",str(player_cnt))
    print(f"PYTHON1:",str(python_cnt))
    

    #print('you choose'  +int(RPS(2)) +".")
    print(f'python choose' +str(RPS(player)).replace('RPS.',' ') +'.')

    print(f'you choose' + str(RPS(player)).replace('RPS.',' ')+'.')
        
    print(f'you choose' + str(RPS(player))+".")
    print(f'you choose' + str(RPS(computer))+".")

    while True:

        playagain=input(f"\n play again! \ny for yes \n q for quit \n")
        print(playagain)
        if playagain.lower() not in ['y','q']:
            continue
        else:
            break

    if playagain.lower()=='y':
        return play_rps()  
    
    else:
     print(f'thank you')
    playagain=False 
    sys.exit("BYE!") 
    return play_rps()

play=rps()
play()

#print(__name__)
if __name__ =='__main__':

 import argparse

parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

args = parser.parse_args()    

rock_papers=rps()
rock_papers()