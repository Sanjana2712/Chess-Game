import random
n=int(input("Enter number of players: "))
names=[]
flag=True
ans=input("Do you want to enter player names? (y/n): ")
if(ans=="y" or ans=="yes" or ans=="Yes" or ans=="Y" or ans=="YES" or ans=="yf"):
    for i in range(n):
        names.append(input("Enter Player "+str(i+1)+"'s name: "))
else:
    for i in range(n):
        names.append("Player "+str(i+1))
if(ans=="yf" or ans=="nf"):
    flag=False
pos=[1 for i in range(n)]
snakes={34:7,21:3,51:12,59:40,93:52,96:76,98:6}
ladders={4:25, 10:32, 22:58, 26:65, 46:88,48:91, 62:81}
winner=n
while(max(pos)!=100):
    i=0
    while(i<n):
        if(flag):
            x=input()
        dice=random.randint(1,6)
        print("\n"+names[i]+ " rolled a "+str(dice))
        pos[i]+=dice
        if(pos[i]<100):
            if(pos[i] in snakes.keys()):
                print("Oops, "+names[i]+" went down a snake from " +str(pos[i])+" to "+ str(snakes[pos[i]]))
                pos[i]=snakes[pos[i]]
            if(pos[i] in ladders.keys()):
                print("Yayy, "+names[i]+" went up a ladder from " +str(pos[i])+" to "+ str(ladders[pos[i]]))
                pos[i]=ladders[pos[i]]
            print(names[i]+" is now at "+str(pos[i]))
        elif(pos[i]>100):
            print("Sorry, "+names[i]+" can't go any further")
            pos[i]-=dice
        else:
            print(names[i]+" is now at "+str(pos[i]))
            winner=i
            print("\nYayy, "+names[winner]+ " won the game!")
            break
        i+=1
ans=input("\nDo you want to view the final positions? (y/n): ")
if(ans=="y" or ans=="yes" or ans=="Yes" or ans=="Y" or ans=="YES"):
    print("\nFinal positions:")
    for i in range(n):
        print(str(pos[i])+ " : "+names[i])
print("\nWinner: "+names[winner])
print("\nThe game has ended! Thank you for playing!")
