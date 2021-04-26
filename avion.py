import tkinter as tk

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

def mouv(event):
    pass
def temps():
    pass

def passager():
    pass

def random_siege():
    pass
def random_bagage():
    pass


racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
avion()

racine.mainloop() # Lancement de la boucle principale