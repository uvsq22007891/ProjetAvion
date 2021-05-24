import tkinter as tk
from timeit import default_timer
import random as rd

#####################################################
# BI TD 4
# Ruben AMOYAL
# Michel ALAND
# Antony MONCLER
# Claude LOUEMBET
"https://github.com/uvsq22007891/ProjetAvion"
#####################################################

HEIGHT = 750
WIDTH = 175
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 30


#fonction qui attribut 180 place a 180 passager
def attribut_place():
    
    #initialise une liste de 180 passager avec [x,y,bagage]
    place=list(range(180))

    for i in range (180):

        place[i]=[0,0,0]

        #attribut une coordonée x
        if place[i][0]==0:
            place[i][0]=rd.randint(1,6)

        #attribut une coordonée y
        if place[i][1]==0:
            place[i][1]=rd.randint(1,30)

        #attribut un nombre de bagage
        if (place[i][0] != 0) and (place[i][1] != 0):
            place[i][2]=rd.randint(0,2)

        # si les coordonées sont déjà prisent dans la liste place alors on la rechange
        if (place[i][0] in place) and (place[i][1] in place):
            place[i][0]=rd.randint(1,6)
            place[i][1]=rd.randint(1,30)
            
    return place

#interface graphique des siège de l'avion 
def simuler_avion():

    canvas.grid()
    for i in range(7):

        for j in range(30):

            #le couloir
            if i == 3:
                 color = "white"

            #les place
            else:
                color = "blue"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

#créer un point (représentant un passager)
def passager():
    x0,y0,x1,y1 = 88,12,93,17
    cercle = canvas.create_oval(x0,y0,x1,y1,width=1,fill="black")
    return cercle

#créer un timer 
def temps():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure(text_clock, text=str_time)
    racine.after(1000, temps)

#déplacement vers le bas
def bas(i):
    global c
    dx, dy = 0 , 25
    #On deplace le passager
    canvas.move(passager1,dx,dy)
    if c == i :
        return
    #On repete cette fonction
    racine.after(1000,bas,i)
    c += 1 

#déplacement vers la gauche
def gauche(i):
    global d
    dx, dy = -25 , 0
    #On deplace le passager
    canvas.move(passager1,dx,dy)
    #On repete cette fonction
    if d == i :
        return
    racine.after(1000,gauche,i)
    d += 1

#déplacement vers la droite
def droite(i):
    global d
    dx, dy = 25 , 0
    #On deplace le passager
    canvas.move(passager1,dx,dy)
    #On repete cette fonction
    if d == i :
        return
    racine.after(1000,droite,i)
    d += 1

#regroupement des divers mouvement que doit réaliser un passager
def mouvement():
    global place ,c,d
    d=0
    c=0
    p = [6,5]
    vari,varj = p[0],p[1]

    if c != vari :
        bas(vari)
        c += 1
    
    if c >= vari :
        while d != varj:
            if varj > 3:
                droite(varj-4)
            if varj <= 3:
                gauche(varj)
            d += 1

#donne une couleur a un passager
def couleur(place):
    global c,d
    for i in range (180) :

        if place[i][2]==0:
            canvas.itemconfigure(passager1, color='orange')
        if place[i][2]==1:
            canvas.itemconfigure(passager1, color='red')
        if place[i][2]==2:
            canvas.itemconfigure(passager1, color='red')
        if place[i][0]==d:
            canvas.itemconfigure(passager1, color='green')


racine = tk.Tk() # Création de la fenêtre racine

canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)

#cree les sièges de l'avion (rouge = couloir, bleu = siège) 
simuler_avion()

# simule un passager avec un point
passager1 = passager()

#commence le décompte du temps
start = default_timer()
text_clock = canvas.create_text(40, 20)
temps()

#commence l'attribution des places pour i passager (ici i = 180)
place=attribut_place()
#commence a faire bouger le passager1
mouvement()

racine.mainloop() # Lancement de la boucle principale






##########################################################################################################################
#essaie pour attribuer les places d'un passager
import random as rd

place = [[False]*7 for i in range (31)]
lp=[]

class Passenger :
        global place,lp
        def __init__(self,numerox,numeroy,bagage):
            self.numerox = numerox
            self.numeroy = numeroy
            self.bagage = bagage
            
            if place[self.numeroy][self.numerox]== True:
                lp.append([self.numerox,self.numeroy,self.bagage])
            self.lp = lp
        
        def get_numerox(self):
            return self.numerox
        
        def get_numeroy(self):
            return self.numeroy

        def get_bagage(self):
            return self.bagage 

        def get_lp(self):
            return self.lp



compteur = 181
def attribuer_place():

    global compteur, place
    while compteur !=0:
        #creer un passager avec nbx ,nby , bagage
        Passenger1 = Passenger(rd.randint(0,6),rd.randint(0,30),rd.randint(0,2))

        x = Passenger1.get_numerox()
        y = Passenger1.get_numeroy()

        #si la place n'est pas attribuer

        if place[y][x] == False:
            place[y][x] = True
        #on enleve un passager
            compteur -= 1

        if place[y][3] == True:
            place[y][x] = False
            compteur +=1

    return Passenger1.get_lp()

print(attribuer_place())
#########################################################################################################################################

#####################################################################################################################################
#essaie pour attribuer les places d'un passager
import random as rd 

place = [[1,2,3,4,5,6] for i in range (30)]
passager1 = []

def attribut_place(passager,pl):

        #attribut ranger y
        passager.append(rd.randint(1,30))

        #attribut ranger x
        passager.append(rd.randint(1,6))

        #attribut nb bagage 
        passager.append(rd.randint(0,2))

        #supprime le ticket pour ne pas reattribuer le meme a un autre passager
        pl[passager[0] - 1][passager[1] - 1]= "none"
        coordy = passager1[0]
        coordx = passager1[1] 
        print(coordy,coordx)
        print("le nombre de bagage",passager1[2])
        print("votre place est ",coordy,coordx)
    
        return passager,pl

def callback(fonction):
    fonction
    

    

for i in range(180):
    place = attribut_place(passager1,place)
print(place)
