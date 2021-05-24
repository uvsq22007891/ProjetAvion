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