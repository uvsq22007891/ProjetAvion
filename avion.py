#####################################################
# BI TD 4
# Ruben AMOYAL
# Michel ALAND
# Antony MONCLER
# Claude LOUEMBET
"https://github.com/uvsq22007891/ProjetAvion"
#####################################################

import tkinter as tk
from timeit import default_timer


HEIGHT = 750
WIDTH = 175
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 30
place = [[0]*7 for i in range(30)]


def avion():
    canvas.grid()
    for i in range(7):
        for j in range(30):
            if i == 3:
                 color = "red"
            else:
                color = "blue"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

def passager():
    x0,y0 = 88,12
    canvas.create_oval(x0,y0,x0+5,y0+5,width=1,fill="black")
    

def mouv(event):
    pass

def temps():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure(text_clock, text=str_time)
    racine.after(1000, temps)

def random_siege():
    pass
def random_bagage():
    pass


racine = tk.Tk() # Création de la fenêtre racine

canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)

#cree les places de l'avion
avion()

# simule un passager avec un point
passager()

start = default_timer()
text_clock = canvas.create_text(40, 20)
temps()

racine.mainloop() # Lancement de la boucle principale