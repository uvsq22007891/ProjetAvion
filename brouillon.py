import random as rd

place = [[0]*7 for i in range(30)]

class Passenger :

        def __init__(self,numerox,numeroy,bagage):
            self.numerox = numerox
            self.numeroy = numeroy
            self.bagage = bagage
            print("bienvenue au passager", "place", numerox,numeroy,"avec nb bagage",bagage)
def liste_passager():
    for i in range(7):
        for j in range(30):
            passenger = passenger(i,j,rd.randint(0,2))
            place[i][j] = 1
    print(place)
    pass