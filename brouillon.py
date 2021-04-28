import random as rd

place = [[0]*31 for i in range (8)]
print(place)

class Passenger :

        def __init__(self,numerox,numeroy,bagage):
            self.numerox = numerox
            self.numeroy = numeroy
            self.bagage = bagage
            print("bienvenue au passager", "place", numerox,numeroy,"avec nb bagage",bagage)
        
        def get_numerox(self):
            return self.numerox
        
        def get_numeroy(self):
            return self.numeroy

        def get_bagage(self):
            return self.bagage 

#le nombre de passager
compteur = 200

while compteur !=0:
    #creer un passager avec nbx ,nby , bagage
    Passenger1 = Passenger(rd.randint(0,7),rd.randint(0,30),rd.randint(0,2))

    x = Passenger1.get_numerox()
    y = Passenger1.get_numeroy()

    #si la place n'est pas attribuer

    if place[x][y] == 0:
        place[x][y] = 1
    #on enleve un passager
        compteur -= 1

    if place[4][y] == 1:
        place[4][y] = 0
        compteur +=1

    #si la place est attribuer
    if place[x][y]==1:
        Passenger1 = Passenger(rd.randint(0,7),rd.randint(0,30),rd.randint(0,2))

for i in range(8):

    print(place[i], "\n")