import random, sys, time

WIDTH = 70
PAUSE_TIME = 0.05

print("Hlboka jaskyna")
print("Stlac Crtl-C pre zastavenie")
time.sleep(2)

leftSirka = 20
medzeraWidth = 10

while True:
    #zobrazenie segmentu pre tunel
    rightWidth = WIDTH - medzeraWidth - leftSirka
    print(("#" * leftSirka) + (" " * medzeraWidth) + ("#" * rightWidth))

    #prekontroluj ci doslo k staleceniu crtl+C pre zastavenie
    try:
        time.sleep(PAUSE_TIME)
    except KeyboardInterrupt:
        sys.exit() #ked je ctrl+C stlacene v tomto case ukonci program
    
    #uprav sirku lavej strany
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftSirka > 1:
        leftSirka = leftSirka -1 #posunutie sirky o 1 do lava    
    elif diceRoll == 2 and leftSirka + medzeraWidth < WIDTH-1:
        leftSirka = leftSirka + 1 #pridaj 1 k sirke na lavu stranu
    else:
        pass #nerob nic, nedojde k zmene lavej strane

    #upravenie medzery v kazdom vykresleni programu. 
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and medzeraWidth > 1:
        medzeraWidth = medzeraWidth - 1 #zniz sirku medzery
    elif diceRoll == 2 and leftSirka + medzeraWidth < WIDTH - 1:
        medzeraWidth = medzeraWidth +1 #zvacsenie medzery o 1
    else:
        pass #nedojde k ziadnej zmene co sa tyka sirky jaskyne
