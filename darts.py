winner = False

def checkwin(tbl):
    length = len(tbl)
    for i in range(length):
        if tbl[i][1] == 0:
            return tbl[i][0]
    return False

def showlist(tbl):
    length = len(tbl)
    print("---- Punktestand ----")
    for i in range(length):
        print(tbl[i][0] + ": " + str(tbl[i][1]))
    print("---------------------")
    

print("Wilkommen in Julians Dart Welt (Python Edition)!")
print()
print()
print()
gamemodechecker = input("Welchen Spielmodus möchtest du spielen [1 = 301 | 2 = 501]: ")
gamemode = 301
errorloop = True
plylist = []

if gamemodechecker == "1":
    print("Du spielst mit 301 Punkten!")
else:
    print("Du spielst mit 501 Punkten!")
    gamemode = 501
print()
print()
print()

while errorloop:
    plycount = input("Wie viele Spieler gibt es: ")
    try:
        plycount = int(plycount)
        break
    except:
        print("Bitte gib eine Zahl ein!")

for i in range(plycount):
    usrname = input("Gib den Namen für Spieler " + str(i + 1) + " ein: ")
    result = [usrname, gamemode]
    plylist.append(result)

print()
print()
print()
print()
while checkwin(plylist) == False:
    for i in range(len(plylist)):
        if checkwin(plylist) != False:
            break
        score = plylist[i][1]
        zwscore = 0
        print(plylist[i][0] + " ist jetzt dran!")
        print()
        print("Bitte gibt die geworfenen Punkte ein:")
        for num in range(3):
            re = int(input(str(num + 1) + ". Wurf: "))
            zwscore = zwscore + re
            if score - zwscore < 0:
                print("Überworfen! Der nächste ist dran!")
                break
            elif score - zwscore == 0:
                break
        
        if score - zwscore == 0:
            score = 0
        elif score - zwscore < 0:
            score = score
        else:
            score = score - zwscore
        plylist[i][1] = score
        showlist(plylist)
    if checkwin(plylist) != False:
        break

winner = checkwin(plylist)
print()
showlist(plylist)
print()
print("Der Gewinner ist: " + winner + "!")