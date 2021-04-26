import random as rd

place = [[0]*7 for i in range(30)]

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

def liste_passager():
    for i in range(7):
        for j in range(30):
            passenger = Passenger(rd.randint(1,7),rd.randint(1,30),rd.randint(0,2))
            if place[passenger.numerox()][passenger.numeroy()]==1:
                 passenger = Passenger(rd.randint(1,7),rd.randint(1,30),rd.randint(0,2))
            else:
                place[i][j] = 1
    print(place)
    print(passenger.get_numerox())