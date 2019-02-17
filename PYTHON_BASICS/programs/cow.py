import random 
unk=str(random.randint(100,500))
print(unk)

while 1:
       inputNum=input('enter any three digie number  :')
       cow_bull=[0,0]
       for i in range(3):
              if unk[i]==inputNum[i]:
                   cow_bull[0] +=1
              if unk[i]!=inputNum[i]:
                   cow_bull[1] +=1
       if cow_bull[0]==3:
               print('"you win" unlock the number :',unk)
               break
       else:
            print('"try again" lock the number :***')
            print('cow:',cow_bull[0],'bull   ',cow_bull[1] )
              
              
       
