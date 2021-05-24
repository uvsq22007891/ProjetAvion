import tkinter as tk 
from timeit import default_timer
import random as rd

HEIGHT = 750
WIDTH = 175
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 30

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

def mouvement(y):

    if y != 0 :
        dx,dy=0,25
        y = y-1
        canvas.move(passager1,dx,dy)
        canvas.after(1000, mouvement(y))
        





racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)

creer_avion()
passager1 = creer_passager()

start = default_timer()
text_clock = canvas.create_text(40, 20)
temps()
mouvement(27)

racine.mainloop() # Lancement de la boucle principale

