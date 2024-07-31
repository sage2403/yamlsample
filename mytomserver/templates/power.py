import math
import time

print("Welcome to the power calculator")
time.sleep(1.5)

x=int(input("enter number:"))
y=int(input("enter power:"))
def fun(x,y):
 print(x,"raised to the power of",y,"is", int(math.pow(x,y)))
 
 return

fun(x,y)
time.sleep(1.5)
cont=input("do you want to continue?(yes/no)1:")

while (cont!="yes"):
    
  if (cont=="no"):
   print("thanks, bye1!!!!!")
   time.sleep(3)
   break
    
  else:
    
   print("Invalid response1")
   cont=input("do you want to continue?(yes/no)2:")
 
while (cont=="yes"):
        
        x=int(input("enter number:"))
        y=int(input("enter power:"))
        fun(x,y)
        time.sleep(1.5)
        cont=input("do you want to continue?(yes/no)3:")
        if (cont=="no"):
            print("thanks, bye2!!!!!")
            time.sleep(3)
            break
        
        else:
              while (cont!="yes"):
                 print("Invalid response2")
                 cont=input("do you want to continue?(yes/no)4:")
                 if (cont=="no"):
                    print("thanks, bye3!!!!!")
                    time.sleep(3)
                    break
        


    




  
