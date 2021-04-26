import random as rd 

ligne = [1,2,3,4,5,6]
siege= [ligne] * 30

passager1=[]

def attribut_place():
    global siege
    passager1.append(rd.randint(1,30))
    passager1.append(rd.randint(1,6))
    for j in range(31):
        for i in range (7):
            if passager1[0] == j :
                if passager1[1] == i:
                    coordy=j
                    coordx=i
                    siege[j][i]= 0
                    print(siege[j][i])
                    return coordy,coordx
                    
attribut_place()
print(attribut_place())
print(passager1[0],passager1[1])
print(siege)