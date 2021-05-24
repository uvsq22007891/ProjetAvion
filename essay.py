from tkinter import *

def deplacement():
    global dx, dy
    if canvas.coords(balle1)[3]>400:
        dy=-1*dy
    #On deplace la balle :
    canvas.move(balle1,dx,dy)
    #On repete cette fonction
    tk.after(1000,deplacement)

#Coordonnees de la balle:
Pos_X=60
Pos_Y=10
dx=0
dy=25

#On cree une fenetre et un canvas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

#On cree une balle:
balle1 = canvas.create_oval(Pos_X,Pos_Y,Pos_X+20,Pos_Y+20,fill='red')
deplacement()

#On lance la boucle principale:
tk.mainloop()