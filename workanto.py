import tkinter as tk 

HEIGHT = 1500
WIDTH = 350
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 30

def avion():
    canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
    canvas.grid()
    for i in range(7):
        for j in range(30):
            if i == 3:
                 color = "red"
            else:
                color = "blue"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

racine = tk.Tk() # Création de la fenêtre racine
avion()
racine.mainloop() # Lancement de la boucle principale