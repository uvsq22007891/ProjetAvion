import random as rd

avion=list(range(180))

def attribut_place():
    for i in range (180):
        avion[i]=[0,0,0]

        if avion[i][0]==0:
            avion[i][0]=rd.randint(1,6)

        if avion[i][1]==0:
            avion[i][1]=rd.randint(1,30)

        if (avion[i][0] != 0) and (avion[i][1] != 0):
            avion[i][2]=rd.randint(0,2)

        if (avion[i][0] in avion) and (avion[i][1] in avion):
            avion[i][0]=rd.randint(1,6)
            avion[i][1]=rd.randint(1,30)
