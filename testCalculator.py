from mymodule import Calc
t=0
input1 = float(input("enter a number"))
input2 = float(input("enter a number"))
c=Calc(input1,input2)
print("enter option 1.add 2.sub 3.mul 4.div")
t = int(input("enter option"))
try:
        if(t==1):
            print(c.add())
        elif(t==2):
            print(c.sub())
        elif(t==3):
            print(c.mul())
        elif(t==4):
            print(c.div())
        else:
            exit(1)
except ValueError as e:
    print("enter valiod option")
    
    
               


               
