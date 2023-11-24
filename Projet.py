from random import randint
    
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

def create_map_and_char(m,d,p):
    L=display_map(m, d)
    L[p["y"]][p["x"]]=p["char"]
    return L

def display(m):
    for i in m:
        for j in i:
            print (j, end='')
        print()
        
#print(create_map_and_char(map,dico,personnage))
    
#Ex 2.3

def update_p(letter,p,m):
    if (letter=="z") and (p["y"]>0) and (m[p["y"]-1][p["x"]] != '#'):
            p["y"]-=1
    if (letter=="q") and (p["x"]>0) and (m[p["y"]][p["x"]-1] != '#'):
            p["x"]-=1
    if (letter=="s") and (p["y"]<len(m)-1) and (m[p["y"]+1][p["x"]] != '#'):
            p["y"]+=1
    if (letter=="d") and (p["x"]<len(m[0])-1) and (m[p["y"]][p["x"]+1] != '#'):
            p["x"]+=1
    return p


def create_objects(nombre_objet,m):
    s=[]
    while len(s)<nombre_objet:
        n=randint(0,4)
        k=randint(0,3)
        if m[k][n]!='#' and ((n,k) not in s):
            s.append((n,k))
    return s


def create_map_char_and_objects(m,d,p,s):
    L=create_map_and_char(m,d,p)
    for i,j in s:
        L[j][i]="."
    return L
    

map_perso=create_map_and_char(map, dico, personnage)
objects=create_objects(4,map_perso)
map_perso_objects=create_map_char_and_objects(map, dico, personnage,objects)
display(map_perso_objects)

while True: 
    personnage = update_p(input("z,q,s ou d?"), personnage,map_perso)
    map_perso=create_map_char_and_objects(map, dico, personnage,objects)
    display(map_perso)
