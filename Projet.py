def copy_matrice(m):
    nouvmatrice=[]
    for i in m:
        nouvmatrice.append(i[:])
    return nouvmatrice
    
def display_map(m,d):
    L=copy_matrice(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            L[i][j]=d[m[i][j]]
    return L

map = [[0,0,0,1,1],[0,0,0,0,1],[1,1,0,0,0],[0,0,0,0,0]]
dico = {0:' ',1:'#'}
#print(display_map(map, dico))

def create_perso(depart):
    return {"char": "o", "x": depart[0], "y": depart[1]}

personnage = create_perso((3, 2))
#print(personnage)

def display_map_and_char(m,d,p):
    L=display_map(m, d)
    L[p["y"]][p["x"]]=p["char"]
    return L

def affichage (m):
    for i in m:
        for j in i:
            print (j, end=' ')
        print()
        
#print(display_map_and_char(map,dico,personnage))
    
#Ex 2.3

def update_p(letter,p):
    if letter=="z":
        if not(p["y"]==0):
            p["y"]-=1
    if letter=="q":
        if not(p["x"]==0):
            p["x"]-=1
    if letter=="s":
        if not(p["y"]==3):
            p["y"]+=1
    if letter=="d":
        if not(p["x"]==4):
            p["x"]+=1
    return p

affichage(display_map_and_char(map, dico, personnage))

while True: 
    personnage = update_p(input("z,q,s ou d?"), personnage)
    affichage(display_map_and_char(map, dico, personnage))




