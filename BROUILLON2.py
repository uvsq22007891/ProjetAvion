import random as rd 

place = [[1,2,3,4,5,6] for i in range (30)]
passager1 = []

def attribut_place(passager,pl):

        #attribut ranger y
        passager.append(rd.randint(1,30))

        #attribut ranger x
        passager.append(rd.randint(1,6))

        #attribut nb bagage 
        passager.append(rd.randint(0,2))

        #supprime le ticket pour ne pas reattribuer le meme a un autre passager
        pl[passager[0] - 1][passager[1] - 1]= "none"
        coordy = passager1[0]
        coordx = passager1[1] 
        print(coordy,coordx)
        print("le nombre de bagage",passager1[2])
        print("votre place est ",coordy,coordx)
    
        return passager,pl

def callback(fonction):
    fonction
    

    

for i in range(180):
    place = attribut_place(passager1,place)
print(place)
