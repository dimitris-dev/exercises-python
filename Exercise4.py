import random

deck1=[]
deck2=[]
xartia = []

p1_wins=0
p2_wins=0
draws=0

figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]




print("Blackjack game! ")
print("Enter a number for a game mode: (1 gia kanoniko paixnidi, 2 gia paixnidi me peiragmeni trapoula)")
mode=int(input())
if mode==1:
    for k in range(100):

        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)

        player1=[]
        sum1=0
        while sum1<16:
            sum1=0
            player1.append(xartia.pop())
            for card in player1:
                if card[0] in figures:
                    sum1=sum1+10
                else:
                    sum1=sum1+card[0]
        if sum1>21:
             p2_wins+=1
        else:
            player2=[]
            sum2=0
            while sum2<16:
                sum2=0
                player2.append(xartia.pop())
                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]
            if sum2>21:
                sum2=0
            if sum1>sum2:
                p1_wins+=1
            elif sum2>sum1:
                p2_wins+=1
            else:
                draws+=1
    print("After 100 games statistics: %d wins for Player1, %d wins for Player2 and %d draws (Normal game)" %(p1_wins,p2_wins,draws)) 
elif mode==2:
    for k in range(100):

        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)


        for a in xartia:
            if (a[0]==10 or a[0] =='K' or a[0] =='Q' or a[0] =='J'):
                deck1.append([a[0],a[1]])

        for b in xartia:
            if (b[0]!=10 and b[0] !='K' and b[0] !='Q' and b[0] !='J'):
                deck2.append([b[0],b[1]])

        player1=[]
        sum1=0
        while sum1<16:
            sum1=0
            player1.append(deck1.pop())
            for card in player1:
                if card[0] in figures:
                    sum1=sum1+10
                else:
                    sum1=sum1+card[0]
        if sum1>21:
             p2_wins+=1
        else:
            player2=[]
            sum2=0
            while sum2<16:
                sum2=0
                player2.append(deck2.pop())
                #print (player2)
                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]
            if sum2>21:
                sum2=0
            if sum1>sum2:
                p1_wins+=1
            elif sum2>sum1:
                p2_wins+=1
            else:
                draws+=1
    print("After 100 games statistics: %d wins for Player1, %d wins for Player2 and %d draws (Peiragmeno game)" %(p1_wins,p2_wins,draws))        