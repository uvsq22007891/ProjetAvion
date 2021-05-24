import tkinter as tk 
from timeit import default_timer
import random as rd

HEIGHT = 750
WIDTH = 175
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 30
c=0

avion = []
for i in range(30) :
    for j in range(7):
        if j != 3 :
            avion.append([i,j,0])


def creer_avion():
    canvas.grid()
    for i in range(7):
        for j in range(30):
            if i == 3:
                 color = "red"
            else:
                color = "blue"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

def creer_passager():
    x0,y0,x1,y1 = 88,12,93,17
    cercle = canvas.create_oval(x0,y0,x1,y1,width=1,fill="black")
    return cercle


def temps():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure(text_clock, text=str_time)
    racine.after(1000, temps)

def bas(i):
    global c
    dx, dy = 0 , 25
    #On deplace la balle :
    canvas.move(passager1,dx,dy)
    if c == i :
        return
    #On repete cette fonction
    racine.after(5000,bas,i)
    c += 1 

def gauche(i):
    global d
    dx, dy = -25 , 0
    #On deplace la balle :
    canvas.move(passager1,dx,dy)
    #On repete cette fonction
    if d == i :
        return
    racine.after(5000,gauche,i)
    d += 1

def droite(i):
    global d
    dx, dy = 25 , 0
    #On deplace la balle :
    canvas.move(passager1,dx,dy)
    #On repete cette fonction
    if d == i :
        return
    racine.after(5000,droite,i)
    d += 1

def r():
    global avion ,c,d
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

def random_bagage():
    bagage = rd.randint(2)
    return bagage



racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)

creer_avion()
passager1 = creer_passager()
start = default_timer()
text_clock = canvas.create_text(40, 20)
temps()
r()


racine.mainloop() # Lancement de la boucle principale