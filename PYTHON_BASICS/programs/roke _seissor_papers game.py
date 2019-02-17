print('-------------roke ,seissor,papers game------------')
print('choose any one--> roke ,seissor,paper')
player1=input('enter player 1 choose')
player2=input('enter player 2 choose')
if (player1 == player2):
    print('game tie---> player1 ='+ player1 +'     player2'+ player2) 
elif(player1=='roke' and player2=='seissor' or player1=='seissor' and player2=='paper' or player1=='paper' and player2=='roke'):
    print('game wins by plyer1 : '+ player1 +'     player2 : '+ player2)
else:
    print('game wins by plyer2 :'+ player1 +'     player2  : '+ player2)
