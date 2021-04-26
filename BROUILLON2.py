import random as rd 


passager1 = []

def attribut_place():
    global passager1
    place = [[1,2,3,4,5,6] for i in range (30)]
    while 
        passager1.append(rd.randint(1,30))
        passager1.append(rd.randint(1,6))
        passager1.append(rd.randint(0,2))
        place [passager1[0] - 1][passager1[1] - 1]= "none"
        coordy = passager1[0]
        coordx = passager1[1] 
        print(coordy,coordx)
        print("le nombre de bagage",passager1[2])
        print("votre place est ",coordy,coordx)
    
        return place


place = attribut_place()
print(place)
