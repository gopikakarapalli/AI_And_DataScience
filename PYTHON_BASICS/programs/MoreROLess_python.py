from random  import randint
ranNum=randint(1,100)
print(ranNum)
count=1

while 1:
      inputNum=int(input("Enter your number"))
      if ranNum == inputNum:
            print("Entred number is correct ")
            print("you are try in %d times "%(count))
            break
      elif ranNum < inputNum:
            print("Entred number is more then genrated number")
      else:
            print("Entred number is less then genrated number")
      count +=1
      



      
            
      
      
      
            
      
